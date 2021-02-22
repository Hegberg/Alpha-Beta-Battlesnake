

def print_board(data, board):

    snake_index = 0
    for snake in board['snakes']:
        if (snake['id'] == data['you']['id']):
            break
        snake_index += 1

    print("My snake: " + str(snake_index))

    for i in range(board['height'] - 1, -1, -1):
        for j in range(0, board['width'], 1):

            found_snake = False
            for k in range(len(board['snakes'])):
                #head
                if ({'x': j, 'y': i} == board['snakes'][k]['body'][0]):
                    print(str(k), end =">")
                    found_snake = True
                    break
                #tail
                elif ({'x': j, 'y': i} == board['snakes'][k]['body'][len(board['snakes'][k]['body']) - 1]):
                    print(str(k), end =")")
                    found_snake = True
                    break
                #body
                elif ({'x': j, 'y': i} in board['snakes'][k]['body']):
                    print(str(k), end =" ")
                    found_snake = True
                    break
            
            if (found_snake):
                continue
            
            if ({'x': j, 'y': i} in board['food']):
                print("$", end =" ")
            else:
                print("-", end =" ")

        print(" ")