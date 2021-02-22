import time
import copy
import math
import threading

from algorithms.common import print_board

class AlphaBeta(object):
    def __init__(self, data):
        self.data = data
        #max time before shunting out of search
        #self.max_time = 0.375
        self.max_time = 0.390
        self.bfs_max_time = 0.370
        #self.bfs_max_time = 0.085
        if (data['turn'] <= 1):
            self.bfs_max_time = 0.320

        self.include_time_reduction = True

        self.tie_value = 0.01
        #self.tie_value = -1.0
        #self.suicide_value = -0.7
        #self.suicide_value = -1.00
        self.suicide_value = -0.999999

        #need this value to be < tie value so can compete for center food on small board
        self.eat_when_free_space_value = 0.95
        #how much space i need compared to body to eat freely 
        self.space_needed_to_freely_eat = 2.0

        #with these modifiers space worth -0.4 to 0.4, instead of -0.5 to 0.5
        #other factors worth -0.2 to 0.2,
        self.space_total_modifier = 1.0
        #self.space_total_modifier = 0.8
        #self.space_total_modifier = 1.3
        self.other_factors_total_modifier = 0.0
        self.food_control_modifier = 0.5
        #self.food_control_modifier = 0.6
        #self.food_control_modifier = 0.35

        #if early start of game, try to blob hard and fast
        #if (self.data['turn'] < 50):
        #    self.space_total_modifier = 0.8
        #    self.other_factors_total_modifier = 1.75

        #not used
        #value given for space if can at min, get to own tail without being killed
        self.tail_follow_value = -0.45 * self.space_total_modifier

        #smake gets value between 0.25 to -0.25 based on snake size in comparison to others
        self.size_eval_modifier = -0.10 * self.other_factors_total_modifier

        self.area_too_small_modifier = -0.3 #not used

        #when start getting lower on health start favouring food tiles, lower number for less snakes since less competition
        self.health_cutoff_for_modifier = 25

        #associated values below used only when health cutoff active 
        # ----------
        #if can't get to food with health left -2 then most likely can't get there in time to not starve
        self.eat_distance_modifier = -0.2 * self.other_factors_total_modifier
        #less food on board, get more greaddy with eating it
        self.number_of_food_modifier = -0.2 * self.other_factors_total_modifier
        # ----------
        """
        if (len(self.data['board']['snakes']) == 2):
            self.health_cutoff_for_modifier = 25
        elif (len(self.data['board']['snakes']) > 2):
            self.health_cutoff_for_modifier = 40
        else:
            self.health_cutoff_for_modifier = 10
        """

        self.smallest_snake_len = self.data['board']['snakes'][0]['length']
        for i in range(1, len(self.data['board']['snakes'])):
            if (self.data['board']['snakes'][i]['length'] < self.smallest_snake_len):
                self.smallest_snake_len = self.data['board']['snakes'][i]['length']
        
        # -0.0 to -0.30, only ever get to 3/4 of value because of health cutoof modifier and associated code
        #value
        #self.hunger_eval_multiplier = -0.25
        #self.hunger_eval_modifier = (self.hunger_eval_multiplier * len(self.data['board']['snakes'])) - (self.hunger_eval_multiplier * 2.0)
        self.hunger_eval_modifier = -0.10 * self.other_factors_total_modifier
        self.food_proximity_modifier = 0.10 * self.other_factors_total_modifier
        self.food_proximity_max_dist = 10

        #len larger than width before goes from greedy to caring more for space
        self.value_switch_modifier = 2

        self.alpha_start = -1.0
        self.beta_start = 1.0

        #large max depths, really mostly on time to bust me out of loops
        #self.max_depth = 2
        self.max_depth = 10 - (len(self.data['board']['snakes']))
        #if only 2 snakes go DEEP, otherwise stay lower
        if (len(self.data['board']['snakes']) == 2):
            #for dfs use 12, bfs use 20
            #self.max_depth = 12
            self.max_depth = 20

        #self.max_depth = 1

        self.max_depth_hit = 100

        self.bfs_alpha_value_depth = [-1.0, self.max_depth]
        #self.bfs_alpha_value_depth = -1.0

        #tuple of board, depth, alpha, beta
        self.breadth_first_search_evaluate_queue = []
        self.breadth_first_search_max_min_queue = []
        self.breadth_first_search_value_dict = {}
        self.breadth_first_search_highest_value = -1.0
        self.depth_first_search_highest_value = -1.0

        self.occupied_tiles = {}
        self.occupied_tiles = self.get_occupied_tiles(self.data['board'])

        self.start_time = time.time()
        self.end_time = 0
        self.elapsed_time = 0

        self.default_eval_time = 0.00045
        #smaller allows more depth per tree
        self.predicted_time_modifier = 0.25
        #larger allows more time per child
        self.predicted_child_time_modifier = 3.2

        #best boards from current to future with optimal outcome
        self.best_boards = [{}] * self.max_depth
        self.best_values = [-1.1] * self.max_depth
        self.best_depth = [0] * self.max_depth
        self.nodes_evaluated = [0] * self.max_depth
        self.best_value_at_depth = [-1.0] * self.max_depth
        self.predictive_nodes = [0] * self.max_depth

        self.base_boards = []
        

    def alpha_beta_breadth_first_search_loop_with_threads(self, board, depth, alpha, beta):
        
        self.breadth_first_search_evaluate_queue.append((board, depth, alpha, beta))

        active_threads = []

        while(len(self.breadth_first_search_evaluate_queue) > 0 or threading.active_count() > 1):
            #nothing in queue need to wait for a thread to finish first
            while (len(self.breadth_first_search_evaluate_queue) == 0 and len(active_threads) > 1):
                active_threads[0].join()
                active_threads.pop(0)
                #if no more active threads break out of loop
                if (len(active_threads) == 0):
                    break
            if (len(self.breadth_first_search_evaluate_queue) > 0):
                eval_params = self.breadth_first_search_evaluate_queue.pop(0)
                x = threading.Thread(target=self.alpha_beta_board_eval, args=(eval_params[0], eval_params[1], eval_params[2], eval_params[3]))
                x.start()
                active_threads.append(x)
            #self.alpha_beta_board_eval(eval_params[0], eval_params[1], eval_params[2], eval_params[3])
            #print("active threads: " + str(len(active_threads)) + " threading_active: " + str(threading.active_count()) + " bfs queue: " + str(len(self.breadth_first_search_evaluate_queue)))
        
        final_val = 0.0

        while(len(self.breadth_first_search_max_min_queue)):
            min_max_params = self.breadth_first_search_max_min_queue.pop(0)
            #print("--------Max Min Queue Loop--------")
            final_val = self.alpha_beta_max_min(min_max_params[0], min_max_params[1], min_max_params[2], min_max_params[3], min_max_params[4])

        return final_val

    def alpha_beta_breadth_first_search_loop(self, board, depth, alpha, beta):
        
        self.breadth_first_search_evaluate_queue.append((board, depth, alpha, beta))

        while(len(self.breadth_first_search_evaluate_queue) > 0):
            #nothing in queue need to wait for a thread to finish first
            eval_params = self.breadth_first_search_evaluate_queue.pop(0)
            self.alpha_beta_board_eval(eval_params[0], eval_params[1], eval_params[2], eval_params[3])

                
        final_val = -1.0

        while(len(self.breadth_first_search_max_min_queue)):
            min_max_params = self.breadth_first_search_max_min_queue.pop(0)
            #print("--------Max Min Queue Loop--------")
            final_val = self.alpha_beta_max_min(min_max_params[0], min_max_params[1], min_max_params[2], min_max_params[3], min_max_params[4])

        return final_val

    #get children and eval for bfs
    def alpha_beta_board_eval(self, board, depth, alpha, beta):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        if (depth == 0 or (self.elapsed_time > self.bfs_max_time and depth < self.max_depth)):
            return None

        occupied_tiles = self.get_occupied_tiles(board)
        new_boards = self.create_new_board_states(board, occupied_tiles)

        if (self.elapsed_time > self.bfs_max_time):
            return None

        #for new boards, go through ones with variations of my moves
        #have my moves as dictionary key
        #evaluate them
        #for each of my possible moves, get my min eval
        #for all my moves, get max eval of the min evaluations

        #contatins my_value, board, all_snake_values, depth of my value
        move_evaluations = {}

        for new_board in new_boards:

            my_snake = None

            #grab my body in new board
            for snake in new_board['snakes']:
                if (snake['id'] == self.data['you']['id']):
                    my_snake = snake
                    break

            #my snake not present on board, it died somehow
            if (my_snake == None):
                if (not "no_snake" in move_evaluations):
                    move_evaluations["no_snake"] = []
                #print(new_board)
                new_board_copy = copy.deepcopy(new_board)
                move_evaluations["no_snake"].append([-1.0, new_board_copy, {self.data['you']['id']: -1.0}, 0, {self.data['you']['id']: 0.0}])
                continue
            
            #check if body exists already or need to add it
            if (not str(my_snake) in move_evaluations):
                move_evaluations[str(my_snake)] = []

            #get evaluation for board, append to move evaluations for that move
            snake_values, snake_depths = self.evaluate_board_state(new_board, my_snake['id'], depth - 1)

            new_board_copy = copy.deepcopy(new_board)

            #if turn > 0 or less than 3 snakes, add opponent moves normally
            #else only add 1 move to free up computation for very early open turn 0
            #otherwise won't gobble close food
            if (self.data['turn'] > 0
                or len(self.data['board']['snakes']) < 3):
                move_evaluations[str(my_snake)].append([snake_values[self.data['you']['id']], new_board_copy, snake_values, snake_depths[self.data['you']['id']], snake_depths])
            elif (len(move_evaluations[str(my_snake)]) == 0):
                move_evaluations[str(my_snake)].append([snake_values[self.data['you']['id']], new_board_copy, snake_values, snake_depths[self.data['you']['id']], snake_depths])

        #list of child boards and values as tuples
        max_min_child_list = []

        #list of min value of child boards used to find max for alpha
        min_child_values = []

        #list of possible future -1 evals
        death_evaulate_queue = []

        child_index = 0

        min_move_values = []

        if (depth < self.max_depth_hit):
            self.max_depth_hit = depth

        for key in move_evaluations:

            max_min_child_list.append([])

            min_value_for_move = 1.0
            beta = 1.0

            for values_and_board in move_evaluations[key]:

                #if only me and started with more than just me, all opponents dead so put value to 1 as long as not -1
                if ( (len(values_and_board[1]['snakes']) == 1 and len(self.data['board']['snakes']) > 1)
                    and not values_and_board[0] == -1.0):
                    values_and_board[0] = 1.0
                #else if only 1 opponent and his value -1, set mine to 1 as long as my value not -1, since winning no matter my position if not dead
                elif ( len(values_and_board[1]['snakes']) == 2
                    and not values_and_board[0] == -1.0):
                    for value_key in values_and_board[2]:
                        if (value_key == self.data['you']['id']):
                            continue
                        elif (values_and_board[2][value_key] == -1.0):
                            values_and_board[0] = 1.0
                            #find opponenets space value, if > 0 add it to values_and_depths[3]
                            for key in values_and_board[4]:
                                if (key == self.data['you']['id']):
                                    continue
                                if (values_and_board[4][key] > 0):
                                    values_and_board[3] += values_and_board[4][key]
                                    break
                            break

                if (values_and_board[0] < min_value_for_move):
                    min_value_for_move = values_and_board[0]

                #if it is me with a -1 or 1, don't even bother continuing line, so skip to next possible board
                if (values_and_board[0] == -1.0 or values_and_board[0] == 1.0 or 
                    values_and_board[0] == self.eat_when_free_space_value or 
                    values_and_board[0] == self.suicide_value or values_and_board[0] == self.tie_value):
                    
                    self.breadth_first_search_value_dict[str(values_and_board[1])] = [values_and_board[0], depth - values_and_board[3], values_and_board[2]]
                    max_min_child_list[len(max_min_child_list) - 1].append([values_and_board[0], depth - values_and_board[3], values_and_board[1], values_and_board[2]])

                    if (depth - 2 > 0):
                        self.nodes_evaluated[depth - 2] += 1

                    #if no higher value than -1, add this board to be possible evaluated, if still present on board
                    if (self.breadth_first_search_highest_value == -1.0 and
                        not key == "no_snake"):
                        death_evaulate_queue.append((values_and_board[1], depth - 1, alpha, beta))

                    continue

                #if snake has eval of -1, just remove it from next possible snake boards
                for v_b_key in values_and_board[2]:
                    if (values_and_board[2][v_b_key] == -1.0 and values_and_board[4][v_b_key] == 0):
                        for remove_snake in values_and_board[1]['snakes']:
                            if (remove_snake['id'] == v_b_key):
                                values_and_board[1]['snakes'].remove(remove_snake)

                #TODO_NOt_possible_bfs
                #Implement alpha beta here somehow
                #beta = copy.deepcopy(min(beta, values_and_board[0]))

                self.nodes_evaluated[depth - 1] += 1

                #append board and then value 
                max_min_child_list[len(max_min_child_list) - 1].append([values_and_board[0], depth, values_and_board[1], values_and_board[2]])

                #check beta here
                beta = min(beta, values_and_board[0])
                if (beta <= self.bfs_alpha_value_depth[0] - 0.3):
                    self.breadth_first_search_value_dict[str(values_and_board[1])] = [values_and_board[0], depth - values_and_board[3], values_and_board[2]]
                    break
                self.breadth_first_search_evaluate_queue.append((values_and_board[1], depth - 1, alpha, beta))

            min_values_and_board = self.get_min_board_value(max_min_child_list[len(max_min_child_list) - 1])
            min_child_values.append(min_values_and_board)
            child_index += 1

            if (min_value_for_move > self.breadth_first_search_highest_value):
                self.breadth_first_search_highest_value = values_and_board[0]

            min_move_values.append(min_value_for_move)

        #if new depth replace alpha
        if (depth < self.bfs_alpha_value_depth[1]):
            self.bfs_alpha_value_depth = self.get_max_board_value(min_child_values)
        else:
            possible_alpha = self.get_max_board_value(min_child_values)
            if (possible_alpha[0] > self.bfs_alpha_value_depth[0]):
                self.bfs_alpha_value_depth = [possible_alpha[0], possible_alpha[1]]


        if (alpha > self.best_value_at_depth[depth - 1]):
            self.best_value_at_depth[depth - 1] = alpha

        #self.nodes_evaluated[depth - 1] += 1

        if (len(max_min_child_list) > 0 and 
            len(max_min_child_list[0]) > 0):
            self.breadth_first_search_max_min_queue.insert(0, (board, max_min_child_list, depth, alpha, beta))

        #if all -1.0 values, add children to investigate as long as still present on that board
        if (self.breadth_first_search_highest_value == -1.0):
            for death_eval in death_evaulate_queue:
                self.breadth_first_search_evaluate_queue.append((death_eval[0], death_eval[1], death_eval[2], death_eval[3]))

    #determine max min for each step for bfs
    def alpha_beta_max_min(self, board, min_max_child_list, depth, alpha, beta):

        #If taking too long to calculate, shut out of deepest eval

        #Shut out of deepest eval that did not finish, makes it so some half evals aren't taken into consideration
        #unless all evals are -1, in that case use anything can find
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        if (self.include_time_reduction and
            (self.max_depth_hit > 1) and (self.max_depth_hit == depth) and 
            (self.elapsed_time > self.bfs_max_time) and self.breadth_first_search_highest_value > -1.0):
            return None

        min_child_values_depths_board_list = []
        
        for i in range(len(min_max_child_list)):

            values_depths_board_list = min_max_child_list[i]

            #if board has a value from farther depth, take that value over current value
            for values_depths_board in values_depths_board_list:

                if (str(values_depths_board[2]) in self.breadth_first_search_value_dict):
                    value_and_depth = self.breadth_first_search_value_dict[str(values_depths_board[2])]
                    values_depths_board[0] = value_and_depth[0]
                    values_depths_board[1] = value_and_depth[1]
                    values_depths_board[3] = value_and_depth[2] #opponent values

            if (len(values_depths_board_list) > 0):
                #get min evaluation of my move with all opponent moves
                min_values_depths_board = self.get_min_board_value(values_depths_board_list)
                self.breadth_first_search_value_dict[str(min_values_depths_board[2])] = [min_values_depths_board[0], min_values_depths_board[1], min_values_depths_board[3]]
                min_child_values_depths_board_list.append(min_values_depths_board)


        #get max evaluations of all my moves
        #max eval is tuple of value and board corresponding to that value
        max_eval = None
        if (not len(min_child_values_depths_board_list) == 0):
            max_eval = self.get_max_board_value(min_child_values_depths_board_list)

        if (not max_eval == None):
            #Dict value of current board set to max value found
            self.breadth_first_search_value_dict[str(board)] = [max_eval[0], max_eval[1], max_eval[3]]

            #This is incorrect, saying value of child board = to value of max of current board
            #self.breadth_first_search_value_dict[str(max_eval[0])] = max_eval[1]
            
            self.best_boards[self.max_depth - depth] = max_eval[2]
            self.best_values[self.max_depth - depth] = max_eval[0]
            self.best_depth[self.max_depth - depth] = max_eval[1]

            return max_eval[0]

        return None

    #basically min but takes depth into account
    def get_min_board_value(self, values_depths_board_list):
        if (len(values_depths_board_list) == 0):
            return None
        min_value_depth_board = values_depths_board_list[0]
        for i in range(1, len(values_depths_board_list)):
            #smaller value
            if (values_depths_board_list[i][0] < min_value_depth_board[0]):
                min_value_depth_board = values_depths_board_list[i]
            #same value but small depth (too kill me quickly)
            #higher depth value means less depth traversed
            elif(values_depths_board_list[i][0] == min_value_depth_board[0]
                and values_depths_board_list[i][1] > min_value_depth_board[1]):
                min_value_depth_board = values_depths_board_list[i]
    

        return min_value_depth_board

    #basically max but takes depth into account
    def get_max_board_value(self, values_depths_board_list):
        if (len(values_depths_board_list) == 0):
            return None
        max_value_depth_board = values_depths_board_list[0]

        #if only two snakes on board, 
        # and my value > tie and < 1, 
        # and my size >= 2 compared to them
        # instead of taking my max, reduce opponents
        opponents_min = 1.0
        opponents_min_index = 0
        my_min = 1.0
        max_opponent_amount = 0
        for i in range(1, len(values_depths_board_list)):
            if (values_depths_board_list[i][0] < my_min):
                my_min = values_depths_board_list[i][0]
            #only two snakes, find opposing snakes lowest value
            if (len(values_depths_board_list[i][3]) == 2):
                for snake_value_key in values_depths_board_list[i][3]:
                    #looking for opposing snake so skip my value in here
                    if (snake_value_key == self.data['you']['id']):
                        continue
                    if (values_depths_board_list[i][3][snake_value_key] < opponents_min):
                        opponents_min = values_depths_board_list[i][3][snake_value_key]
                        opponents_min_index = i
                        break
            #check to make sure all boards have two opponents
            if (len(values_depths_board_list[i][3]) > max_opponent_amount):
                max_opponent_amount = len(values_depths_board_list[i][3])

            #larger 
            #or suicide vs loss, choose whichever has higher depth
            if (values_depths_board_list[i][0] > max_value_depth_board[0] and
                not (values_depths_board_list[i][0] <= self.suicide_value and max_value_depth_board[0] <= self.suicide_value)):
                max_value_depth_board = values_depths_board_list[i]
            #higher depth value means less depth traversed
            #same large value but larger depth (too avoid short suicides), unless 1.0, than shortest to win fast
            elif((values_depths_board_list[i][0] == max_value_depth_board[0] or 
                (values_depths_board_list[i][0] <= self.suicide_value and max_value_depth_board[0] <= self.suicide_value))
                and values_depths_board_list[i][1] > max_value_depth_board[1]
                and (values_depths_board_list[i][0] > -1.0 or values_depths_board_list[i][0] > self.suicide_value)):
                max_value_depth_board = values_depths_board_list[i]
            elif((values_depths_board_list[i][0] == max_value_depth_board[0] or 
                (values_depths_board_list[i][0] <= self.suicide_value and max_value_depth_board[0] <= self.suicide_value))
                and values_depths_board_list[i][1] < max_value_depth_board[1]
                and (values_depths_board_list[i][0] == -1.0 or values_depths_board_list[i][0] == self.suicide_value)):
                max_value_depth_board = values_depths_board_list[i]
            #else if both suicide and depth on smae level, choose suicide
            elif((values_depths_board_list[i][0] == max_value_depth_board[0] or 
                (values_depths_board_list[i][0] <= self.suicide_value and max_value_depth_board[0] <= self.suicide_value))
                and values_depths_board_list[i][1] == max_value_depth_board[1]
                and (values_depths_board_list[i][0] == self.suicide_value and max_value_depth_board[0] == -1.0)):
                max_value_depth_board = values_depths_board_list[i]

        #if only 2 snakes and
        #my snake min is < 1 but > tie
        #take move that minimizes opponent value
        
        if (max_opponent_amount == 2 and
            my_min < 1.0 and my_min > self.tie_value):
            #make sure size >=2 relatively before getting aggresive
            my_snake_size = 0
            opponent_snake_size = 0
            for snake in values_depths_board_list[opponents_min_index][2]['snakes']:
                if (snake_value_key == self.data['you']['id']):
                    my_snake_size = snake['length']
                else:
                    opponent_snake_size = snake['length']
            if (my_snake_size >= opponent_snake_size + 2):
                max_value_depth_board = values_depths_board_list[opponents_min_index]

        return max_value_depth_board

        
    def evaluate_board_state(self, board, self_id, depth):
        #values dict of snake ids as keys and their values as items
        values = {}
        depths = {}

        #init values of the snakes
        for snake in board['snakes']:
            values[snake['id']] = 0.0
            depths[snake['id']] = 0

        collision_values = self.evaluate_board_collisions(board)
        for value_key in collision_values:
            #if snake is going to collide in some way (non 0 value), change it's evaluation to respective value
            if (not collision_values[value_key] == 0.0):
                values[value_key] = collision_values[value_key]

        #if value == 1.0, or -1.0, or tie, skip rest of evaluation
        #add 1 to depth, so a win or death at a certian depth is equivalent to a space death
        if (values[self_id] == 1.0 or values[self_id] == -1.0 or values[self_id] == self.tie_value or values[self_id] == self.suicide_value):
            depths[self_id] += 1
            return values, depths

        # -0.5 to 0.5 by default
        #spacing_values = self.evaluate_board_spacing(board)
        spacing_values, my_space_available = self.evaluate_board_spacing(board)

        for value_key in spacing_values:
            #for opposing snakes, don't modify value if already "untouchable" value
            if ((values[value_key] == 1.0 or values[value_key] == -1.0 or values[value_key] == self.tie_value or values[value_key] == self.suicide_value)):
                continue
            values[value_key] = spacing_values[value_key]

        #if value == 1.0, or -1.0, skip rest of evaluation
        if (values[self_id] == 1.0 or values[self_id] == -1.0):
            return values, depths

        #health_values = self.evaluate_board_health(board, depth)
        health_values = self.evaluate_board_health(board, depth, my_space_available)

        for value_key in health_values:
            if ((values[value_key] == 1.0 or values[value_key] == -1.0 or values[value_key] == self.tie_value or values[value_key] == self.suicide_value)):
                continue
            
            #if snake is going to starve, change it's evaluation to lowest possible
            if (health_values[value_key] == -1.0):
                values[value_key] = health_values[value_key]

                #if only opposing snake, and starving to death, and my value is greater than -0.5 (so not dying to space)
                #than if they starve out I win, so my value should be 1 since killing them
                if ((not value_key == self_id) and (len(board['snakes']) == 2) and (values[self_id] > -0.5)):
                    values[self_id] = 1.0

            elif (health_values[value_key] == 1.0 or health_values[value_key] == self.eat_when_free_space_value):
                values[value_key] = health_values[value_key]
            
            #else if value not defualt of 0, and value not already -1, add modified eating eval to encourage food
            elif (not health_values[value_key] == 0.0 and not values[value_key] == -1.0):
                values[value_key] += health_values[value_key]

        for value_key in values:
            if (values[value_key] < -1.0):
                values[value_key] = -1.0

        return values, depths

    def evaluate_snake_size(self, board):
        values = {}
        #size as key, snake ids with the size as value
        snake_sizes = []

        for snake in board['snakes']:
            values[snake['id']] = 0.0
            snake_sizes.append((snake['length'], snake['id']))
        
        snake_sizes.sort(key=lambda tup: tup[0], reverse = True)

        largest_length = snake_sizes[0][0]
        
        largest_difference = largest_length - self.smallest_snake_len
        for i in range(len(snake_sizes)):
            #all snakes are same length, so don't modify value
            if (largest_difference == 0):
                continue
            snake_difference = snake_sizes[i][0] - self.smallest_snake_len
            #gives value between -1 and 1, -1 -> -0.3, 1 -> 0.3
            ratio = ((snake_difference / largest_difference) - 0.5) * 2.0
            values[snake_sizes[i][1]] = ratio * self.size_eval_modifier

        return values

    def evaluate_board_collisions(self, board):
        values = {}

        #check if collision between head of snakes, if so larger one gets 1 value, smaller gets -1

        #collision place as key, snakes colliding id's as list 
        collision_placements = {}

        for snake in board['snakes']:

            values[snake['id']] = 0.0
            
            #check if key already exists, if not add it
            #if does exist, add id as collision partner

            #if snake head pos as key exists in dict
            if (str(snake['body'][0]) in collision_placements):
                collision_placements[str(snake['body'][0])].append((snake['id'], snake['length']))
            else:
                collision_placements[str(snake['body'][0])] = [(snake['id'], snake['length'])]

        #check if multiple id's exist for a head placement, if so a collision and modify values
        for key in collision_placements:
            if (len(collision_placements[key]) > 1):
                #collision detected, find largest snake,
                #if tie and only 2 snakes, set value as 0.99 (slightly less than real win)
                #otherwise set value as -1, (0 maybe) for a tie

                largest_snakes = [collision_placements[key][0]]
                smaller_snakes = []

                for i in range(1, len(collision_placements[key])):
                    if (collision_placements[key][i][1] > largest_snakes[0][1]):
                        for small_snake in largest_snakes:
                            smaller_snakes.append(small_snake)
                        largest_snakes = [collision_placements[key][i]]
                    elif (collision_placements[key][i][1] == largest_snakes[0][1]):
                        largest_snakes.append(collision_placements[key][i])
                    else:
                        smaller_snakes.append(collision_placements[key][i])

                #set all the small snake values to dead
                for i in range(len(smaller_snakes)):
                    values[smaller_snakes[i][0]] = -1.0

                #set largest snake value to 1
                if (len(largest_snakes) == 1):
                    values[largest_snakes[0][0]] = 1.0
                #if only 2 snakes on board and can go for tie with kill
                elif (len(board['snakes']) == 2):
                    values[largest_snakes[0][0]] = self.tie_value
                    values[largest_snakes[1][0]] = self.tie_value
                #if only 2 colliding, set to suicide value
                elif (len(largest_snakes) == 2):
                    values[largest_snakes[0][0]] = self.suicide_value
                    values[largest_snakes[1][0]] = self.suicide_value
                else:
                    for i in range(len(largest_snakes)):
                        values[largest_snakes[i][0]] = -1.0

        return values

    def evaluate_board_health(self, board, depth, my_space_available):
        values = {}

        for snake in board['snakes']:
            #check to make sure eating food on turn 2 if possible
            #if on turn 2 and health not 100
            if (snake['health'] <= 0):
                values[snake['id']] = -1.0

                #value of 0 to 1 based off how hungry you are, times eat multiplier
                #values[snake['id']] = self.hunger_eval_modifier * ((100.0 - snake['health']) / 100.0)
            #if low on health and distance to food is > health, will be dead to get there, so value -1
            #otherwise degrade value by distance to food if there is food on board
            elif(len(board['food']) >= 1
                and snake['health'] < self.health_cutoff_for_modifier):
                smallest_distance = self.health_cutoff_for_modifier
                for food in board['food']:
                    distance = abs(snake['body'][0]['x'] - food['x']) + abs(snake['body'][0]['y'] - food['y'])
                    if (distance < smallest_distance):
                        smallest_distance = distance
                #if distance too far snake is dead
                if (smallest_distance > snake['health']):
                    values[snake['id']] = -1.0
                #else give linear modifier of eat being low
                else:
                    values[snake['id']] = ((self.health_cutoff_for_modifier - snake['health']) / self.health_cutoff_for_modifier) * self.eat_distance_modifier

                    #take amount of food into account
                    #1 snake or less per food
                    if (len(board['food']) - len(board['snakes']) <= 0):
                        values[snake['id']] += self.number_of_food_modifier
                    elif (len(board['food']) - len(board['snakes']) < len(board['snakes'])):
                        values[snake['id']] += self.number_of_food_modifier / 2

                    #values[snake['id']] += (1.0 - ( (len(board['food']) - len(board['snakes'])) / len(board['snakes']) )) * self.number_of_food_modifier

            else:
                values[snake['id']] = 0.0

                #reduces value based on hunger
                values[snake['id']] += self.hunger_eval_modifier * ((100.0 - snake['health']) / 100.0)
                
                #between half of hunger eval modifier and negative half
                #so 0.2 to -0.2
                #values[snake['id']] = (abs(self.hunger_eval_modifier) / 2.0) - self.hunger_eval_modifier * ((100.0 - snake['health']) / 100.0)

        return values

    def evaluate_board_spacing(self, board):
        values = {}

        #init values of the snakes
        for snake in board['snakes']:
            values[snake['id']] = 0
        #get spacing value, purely space snake has
        spacing_matrix = []
        snake_spaces = {}

        for i in range(board['width']):
            row = []
            for j in range(board['height']):
                row.append("0")
            spacing_matrix.append(row)
        
        #get snake tiles to start flood fill from, got from largest to smallest snakes
        snake_sizes_and_starts = []

        #add current bodies to board
        self_snake = None
        for snake in board['snakes']:
            #skip first body part so start occuping at head
            #include self here so board adds body to board
            head = True
            for body_part in snake['body']:
                if (head):
                    head = False
                    continue
                
                spacing_matrix[body_part['x']][body_part['y']] = "-1"

            #add all but self, then go through and add self where >= len of next snake
            if (snake['id'] == self.data['you']['id']):
                self_snake = snake
                continue
            snake_sizes_and_starts.append((snake['length'],(snake['body'][0]['x'],snake['body'][0]['y']), snake['id']))

        snake_sizes_and_starts.sort(key=lambda tup: tup[0], reverse = True)

        #add self manually but before snake of same size
        added_self = False
        for i in range(len(snake_sizes_and_starts)):
            if (self_snake['length'] >= snake_sizes_and_starts[i][0]):
                snake_sizes_and_starts.insert(i, (self_snake['length'],(self_snake['body'][0]['x'],self_snake['body'][0]['y']), self_snake['id']))
                break

        if (not added_self):
            snake_sizes_and_starts.append((self_snake['length'],(self_snake['body'][0]['x'],self_snake['body'][0]['y']), self_snake['id']))

        #need tile order, but to also mark tile as a certian snakes, so mark not as number but as the snake id
        tile_order_queue = []

        for i in range(len(snake_sizes_and_starts)):
            tile_order_queue.append((snake_sizes_and_starts[i][1][0],snake_sizes_and_starts[i][1][1],snake_sizes_and_starts[i][2]))

            snake_spaces[snake_sizes_and_starts[i][2]] = -1


        while (len(tile_order_queue) > 0):
            #update board with latest tile
            #add new possible tiles to queue
            #update snake_spaces

            tile = tile_order_queue.pop(0)

            #check if other snake already occupied tile
            if (not spacing_matrix[tile[0]][tile[1]] == "0"):
                continue
            
            spacing_matrix[tile[0]][tile[1]] = tile[2]

            snake_spaces[tile[2]] += 1

            #can go to tile to left
            if (tile[0] > 0 and spacing_matrix[tile[0] - 1][tile[1]] == "0"):
                tile_order_queue.append((tile[0] - 1, tile[1], tile[2]))

            #can go to tile to right
            if (tile[0] < self.data['board']['width'] - 1 and spacing_matrix[tile[0] + 1][tile[1]] == "0"):
                tile_order_queue.append((tile[0] + 1, tile[1], tile[2]))

            #can go to tile to down
            if (tile[1] > 0 and spacing_matrix[tile[0]][tile[1] - 1] == "0"):
                tile_order_queue.append((tile[0], tile[1] - 1, tile[2]))

            #can go to tile to up
            if (tile[1] < self.data['board']['height'] - 1 and spacing_matrix[tile[0]][tile[1] + 1] == "0"):
                tile_order_queue.append((tile[0], tile[1] + 1, tile[2]))

            
        for snake in board['snakes']:
            values[snake['id']] = snake_spaces[snake['id']] / (board['width'] * board['height'])

        space_available = snake_spaces[self.data['you']['id']]
        
        return values, space_available

    def space_eval_add_children(self, tile, tile_order_queue, visisted_tiles, spacing_matrix, snake_sizes, food_controlled, tile_heads):#, collision_win):
        #can go to tile to left
        tile_heads[str((tile[0], tile[1]))] = []
        if (tile[0] > 0 and visisted_tiles[str((tile[0] - 1, tile[1]))][0] == False):
            tile_order_queue.append((tile[0] - 1, tile[1], tile[2], tile[3] + 1))
            if (spacing_matrix[tile[0] - 1][tile[1]] == "0"):
                tile_heads[str((tile[0], tile[1]))].append((tile[0] - 1, tile[1]))


        #can go to tile to right
        if (tile[0] < self.data['board']['width'] - 1 and visisted_tiles[str((tile[0] + 1, tile[1]))][0] == False):
            tile_order_queue.append((tile[0] + 1, tile[1], tile[2], tile[3] + 1))
            if (spacing_matrix[tile[0] + 1][tile[1]] == "0"):
                tile_heads[str((tile[0], tile[1]))].append((tile[0] + 1, tile[1]))

        #can go to tile to down
        if (tile[1] > 0 and visisted_tiles[str((tile[0], tile[1] - 1))][0] == False):
            tile_order_queue.append((tile[0], tile[1] - 1, tile[2], tile[3] + 1))
            if (spacing_matrix[tile[0]][tile[1] - 1] == "0"):
                tile_heads[str((tile[0], tile[1]))].append((tile[0], tile[1] - 1))

        #can go to tile to up
        if (tile[1] < self.data['board']['height'] - 1 and visisted_tiles[str((tile[0], tile[1] + 1))][0] == False):
            tile_order_queue.append((tile[0], tile[1] + 1, tile[2], tile[3] + 1))
            if (spacing_matrix[tile[0]][tile[1] + 1] == "0"):
                tile_heads[str((tile[0], tile[1]))].append((tile[0], tile[1] + 1))

    def check_to_remove_tile_head(self, x, y, og_x, og_y, snake_id, depth, tile_heads, spacing_matrix, tile_order_queue, visisted_tiles, snake_spaces, remaining_snake_spaces, add_child = False, child_id = "None"):
        #if tile exists to space beside, and same snake that is trying (and failing) to occupy new tile
        if (x >= 0 and x < self.data['board']['width']
            and y >= 0 and y < self.data['board']['height']
            and spacing_matrix[x][y] == snake_id):
            #if tile head does not exist in dict, return out
            if (not str((x, y)) in tile_heads):
                return
            #if tile was head, remove it
            if ((og_x, og_y) in tile_heads[str((x, y))]):
                tile_heads[str((x, y))].remove((og_x, og_y))

                if (add_child):
                #add tile in queue for larger snake, in case all other snake heads destroyed
                    tile_order_queue.append((x, y, child_id, depth + 1))

            if (len(tile_heads[str((x, y))]) == 0):
                #no more heads, open tile
                spacing_matrix[x][y] = "0"
                #since space open, add to remaining spaces
                remaining_snake_spaces += 1
                #set as no longer visited
                visisted_tiles[str((x,y))] = [False,0]
                #since remove tile from board, remove this snake trying to access this tile in space queue
                if ((x, y, snake_id, depth) in tile_order_queue):
                    tile_order_queue.remove((x, y, snake_id, depth))

                # add as snake space, since it would still move here to die, count as a space so depth is accurate in counting tiles to die
                #only do it for first instance of tile being destroyed though, not childrens tiles
                if (add_child):
                    snake_spaces[snake_id] += 1

                #no more heads and this tile being destroyed, so remove from a head from previous tile
                #check tiles around if owned by same owner and have this as a head, remove it

                x2 = x - 1
                y2 = y
                #check all tiles around newly removed head tile, to remove this tile as head from them
                self.check_to_remove_tile_head(x2, y2, x, y, snake_id, depth, tile_heads, spacing_matrix, tile_order_queue, visisted_tiles, snake_spaces, remaining_snake_spaces)

                x2 = x + 1
                y2 = y
                #check all tiles around newly removed head tile, to remove this tile as head from them
                self.check_to_remove_tile_head(x2, y2, x, y, snake_id, depth, tile_heads, spacing_matrix, tile_order_queue, visisted_tiles, snake_spaces, remaining_snake_spaces)

                x2 = x
                y2 = y - 1
                #check all tiles around newly removed head tile, to remove this tile as head from them
                self.check_to_remove_tile_head(x2, y2, x, y, snake_id, depth, tile_heads, spacing_matrix, tile_order_queue, visisted_tiles, snake_spaces, remaining_snake_spaces)

                x2 = x
                y2 = y + 1
                #check all tiles around newly removed head tile, to remove this tile as head from them
                self.check_to_remove_tile_head(x2, y2, x, y, snake_id, depth, tile_heads, spacing_matrix, tile_order_queue, visisted_tiles, snake_spaces, remaining_snake_spaces)


    def create_new_board_states(self, board, occupied_tiles):
        #list of all board states, have each snake go through each one
        #and find best eval of all of them
        new_boards = [copy.deepcopy(board)]

        #create dict for snakes and thier tails to keep if they eat
        #key is snake id, item is tail
        snake_tails = {}

        dead_snakes = []

        #id of snakes to evaluate if > 3
        closest_snakes = []

        added_moves = 1
        #max child boards 27, 3x3x3x1
        if (self.data['turn'] == 0):
            #my snake, and closest snake, all possible moves (so 2 player mode don't lose out on starting duel moves)
            allowed_child_board_limit = 16
        else:
            allowed_child_board_limit = 27

        #if more than 3 snakes, just only evaluate closest 2 snakes
        #if (len(board['snakes']) > 3):
        #list of dist and id tuples
        head = None
        my_snake = None
        my_snake_index = 0
        for snake_index in range(len(board['snakes'])):
            if (board['snakes'][snake_index]['id'] == self.data['you']['id']):
                head = board['snakes'][snake_index]['body'][0]
                break
        for snake_index in range(len(board['snakes'])):
            #skip self
            if (board['snakes'][snake_index]['id'] == self.data['you']['id']):
                my_snake = board['snakes'][snake_index]
                my_snake_index = snake_index
                continue
            distance = abs(board['snakes'][snake_index]['body'][0]['x'] - head['x']) + abs(board['snakes'][snake_index]['body'][0]['y'] - head['y'])

            closest_snakes.append((distance, board['snakes'][snake_index]['id'], board['snakes'][snake_index], snake_index))

        closest_snakes.sort(key = lambda t: t[0])
        #add myself onto closest snake first, so start evaluating snakes based on me, than closest to farthest from me
        snake_list = []
        snake_indexs = []
        snake_list.append(my_snake)
        snake_indexs.append(my_snake_index)
        for snake_index in range(len(closest_snakes)):
            snake_list.append(closest_snakes[snake_index][2])
            snake_indexs.append(closest_snakes[snake_index][3])

        #make a copy of existing boards, for each add a copy with snakes possible moves on top
        for snake_list_index in range(len(snake_list)):
            #add first possible move on top of existing boards
            #if more possible boards, duplicate them first and add
            #to add move, remove tail of snake and add new x,y as head

            snake_index = snake_indexs[snake_list_index]


            possible_moves = []

            #get possible moves for snake
            if (board['snakes'][snake_index]['id'] == self.data['you']['id']):
                snake_heads = []
                for snake in board['snakes']:
                    if (not snake['id'] == self.data['you']['id']):
                        snake_heads.append(snake['body'][0])
                possible_moves = self.get_possible_moves(board['snakes'][snake_index], occupied_tiles, snake_heads)
            else:
                possible_moves = self.get_possible_moves(board['snakes'][snake_index], occupied_tiles)

            #if no moves, snake crashes and dies, so delete body
            #if it is my body return out right away and in main alpha beta loop, 
            #give any snake that has no body eval -1.0 in main alpha beta loop,
            #if i have no possible moves since no snake, give me eval of -1 and pop return out of main alpha beta loop with value -1.0
            #print(possible_moves)
            if (len(possible_moves) == 0):
                #print("snake index removing: " + str(snake_index))
                dead_snakes.append(snake_index)
                #go back to start of prior for loop
                continue

            while (added_moves * len(possible_moves) > allowed_child_board_limit):
                possible_moves.pop()

            added_moves = added_moves * len(possible_moves)

            snake_tail_if_eats = None

            #at least one move, so add it to existing boards
            for new_board in new_boards:
                #get snake need to modify
                #snake_tail_if_eats = new_board['snakes'][snake_index]['body'].pop()
                new_board['snakes'][snake_index]['body'].pop()

                snake_tail_if_eats = new_board['snakes'][snake_index]['body'][-1]

                snake_tails[new_board['snakes'][snake_index]['id']] = snake_tail_if_eats

                new_board['snakes'][snake_index]['body'].insert(0, {"x": possible_moves[0][0], "y": possible_moves[0][1]})
                
            #if more than 1 move, make copy of board states and edit head of snake to new move
            additional_boards = []
            for i in range(1, len(possible_moves)):
                for new_board in new_boards:
                    #make copy of board
                    additional_board = copy.deepcopy(new_board)

                    #modify board to have different move
                    additional_board['snakes'][snake_index]['body'][0]['x'] = possible_moves[i][0]
                    additional_board['snakes'][snake_index]['body'][0]['y'] = possible_moves[i][1]

                    #add new board
                    additional_boards.append(additional_board)
                    
            for additional_board in additional_boards:
                new_boards.append(additional_board)

        dead_snakes.sort(reverse=True)

        for snake_index in dead_snakes:
            for new_board in new_boards:
                del new_board['snakes'][snake_index]

        #go through boards a second time, if any of the snake heads on the board is now on a food, remove the food
        #update snakes that are eating the food
        for food_board in new_boards:
            #keep track of food consumed on this board
            food_to_remove = []

            #update every snake consuming a food
            for food_snake in food_board['snakes']:
                if (food_snake['body'][0] in food_board['food']):
                    if (not food_snake['body'][0] in food_to_remove):
                        food_to_remove.append(food_snake['body'][0])

                    food_snake['body'].append(snake_tails[food_snake['id']])
                    food_snake['length'] += 1
                    food_snake['health'] = 100
                elif ('hazrads' in food_board and
                    food_snake['body'][0] in food_board['hazards']):
                    food_snake['health'] -= 16
                else:
                    food_snake['health'] -= 1

            #remove consumed foods from board
            for food in food_to_remove:
                food_board['food'].remove(food)

        #if first children to create, set as base boards to grab move from if somehow other grabbing move fails
        if (len(self.base_boards) == 0):
            self.base_boards += new_boards

        return new_boards

    #get tiles snake can move to and return them
    def get_possible_moves(self, snake, occupied_tiles, opponenet_snake_heads = None):
        possible_moves = []
        if (snake['body'][0]['x'] + 1 < self.data['board']['width'] 
        and (str(snake['body'][0]['x'] + 1) + ' ' + str(snake['body'][0]['y'])) not in occupied_tiles):
            possible_moves.append((snake['body'][0]['x'] + 1, snake['body'][0]['y']))

        if (snake['body'][0]['x'] - 1 >= 0 
        and (str(snake['body'][0]['x'] - 1) + ' ' + str(snake['body'][0]['y'])) not in occupied_tiles):
            possible_moves.append((snake['body'][0]['x'] - 1, snake['body'][0]['y']))

        if (snake['body'][0]['y'] + 1 < self.data['board']['height'] 
        and (str(snake['body'][0]['x']) + ' ' + str(snake['body'][0]['y'] + 1)) not in occupied_tiles):
            possible_moves.append((snake['body'][0]['x'], snake['body'][0]['y'] + 1))

        if (snake['body'][0]['y'] - 1 >= 0
        and (str(snake['body'][0]['x']) + ' ' + str(snake['body'][0]['y'] - 1)) not in occupied_tiles):
            possible_moves.append((snake['body'][0]['x'], snake['body'][0]['y'] - 1))
        
        #order tiles by how close to opponent heads, explore paths closer to opposing snakes first
        if (snake['id'] == self.data['you']['id']):
            possible_moves_and_dist = []
            dist = 100
            for move in possible_moves:
                shortest_dist = 100
                for opponenet_head in opponenet_snake_heads:
                    dist = math.sqrt( ((move[0] - opponenet_head['x']) ** 2) + ((move[1] - opponenet_head['y']) ** 2) )
                    if (dist < shortest_dist):
                        shortest_dist = dist
                possible_moves_and_dist.append((move, shortest_dist))

            possible_moves_and_dist.sort(key=lambda t: t[1])

            final_moves = []
            for move_dist in possible_moves_and_dist:
                final_moves.append(move_dist[0])

            return final_moves

        return possible_moves

    def get_occupied_tiles(self, board):
        occupied_tiles = {}
        for snake in board['snakes']:
            #grab all of snakes besides the tail
            for i in range(len(snake['body']) - 1):
                occupied_tiles[(str(snake['body'][i]['x']) + ' ' + str(snake['body'][i]['y']))] = 1

        return occupied_tiles

    def get_move_from_new_board(self, board):
        #find own snake in new board
        next_move = None
        for snake in board['snakes']:
            if (snake['id'] == self.data['you']['id']):
                #find where branches off from current to new snake
                #find move required to switch to that board state
                move_index = 0
                for i in range(len(snake['body'])):
                    if (snake['body'][i]['x'] == self.data['you']['body'][0]['x'] and snake['body'][i]['y'] == self.data['you']['body'][0]['y']):
                        #print('found old head')
                        #print(snake['body'][i])
                        #this is current head, so go one back in new snake to get proper move
                        move_index = i - 1
                        break
                
                if (move_index >= 0 and move_index < len(snake['body'])):
                    next_move = snake['body'][move_index]

                break
        
        #if valid next move, find the direction to get there
        if (not next_move == None):
            #print("Best board: " + str (board))
            #print(next_move)
            #to the right
            if (next_move['x'] > self.data['you']['body'][0]['x']):
                return 'right'

            #to the left
            elif (next_move['x'] < self.data['you']['body'][0]['x']):
                return 'left'

            #to the top
            if (next_move['y'] > self.data['you']['body'][0]['y']):
                return 'up'

            #to the bottom
            elif (next_move['y'] < self.data['you']['body'][0]['y']):
                return 'down'
        else:
            return None