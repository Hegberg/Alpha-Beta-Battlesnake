import time
import os

from algorithms.get_move import get_move

if __name__ == '__main__':

    start = time.time()

    #Killed self going left
    data = {'game': {'id': '22aa4c5b-b139-40ff-8de6-e2531fa0fbf9', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 164, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_6tXpdVmCf7VrQtxtk4RcwYTc', 'name': 'Git Adder (2)', 'latency': '75', 'health': 90, 'body': [{'x': 3, 'y': 7}, {'x': 3, 'y': 6}, {'x': 3, 'y': 5}, {'x': 4, 'y': 5}, {'x': 5, 'y': 5}, {'x': 6, 'y': 5}, {'x': 7, 'y': 5}, {'x': 8, 'y': 5}, {'x': 9, 'y': 5}, {'x': 10, 'y': 5}, {'x': 10, 'y': 6}, {'x': 10, 'y': 7}, {'x': 9, 'y': 7}, {'x': 9, 'y': 8}], 'head': {'x': 3, 'y': 7}, 'length': 14, 'shout': ''}, {'id': 'gs_D8Y8PhF8cJ87xgytkbvw6ptH', 'name': 'Head Hunter', 'latency': '71', 'health': 95, 'body': [{'x': 0, 'y': 4}, {'x': 0, 'y': 3}, {'x': 0, 'y': 2}, {'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}, {'x': 3, 'y': 1}, {'x': 4, 'y': 1}, {'x': 5, 'y': 1}, {'x': 6, 'y': 1}, {'x': 7, 'y': 1}, {'x': 8, 'y': 1}, {'x': 8, 'y': 2}, {'x': 8, 'y': 3}, {'x': 7, 'y': 3}, {'x': 6, 'y': 3}, {'x': 5, 'y': 3}], 'head': {'x': 0, 'y': 4}, 'length': 17, 'shout': ''}, {'id': 'gs_m4m7ybyjk9gm4YRHPB3Wx8WK', 'name': 'Shielded_Woodland', 'latency': '242', 'health': 54, 'body': [{'x': 1, 'y': 5}, {'x': 1, 'y': 4}, {'x': 2, 'y': 4}, {'x': 2, 'y': 5}, {'x': 2, 'y': 6}, {'x': 1, 'y': 6}], 'head': {'x': 1, 'y': 5}, 'length': 6, 'shout': ''}], 'food': [{'x': 6, 'y': 2}, {'x': 4, 'y': 0}, {'x': 10, 'y': 10}, {'x': 2, 'y': 9}], 'hazards': []}, 'you': {'id': 'gs_m4m7ybyjk9gm4YRHPB3Wx8WK', 'name': 'Shielded_Woodland', 'latency': '242', 'health': 54, 'body': [{'x': 1, 'y': 5}, {'x': 1, 'y': 4}, {'x': 2, 'y': 4}, {'x': 2, 'y': 5}, {'x': 2, 'y': 6}, {'x': 1, 'y': 6}], 'head': {'x': 1, 'y': 5}, 'length': 6, 'shout': ''}}

    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'left'):
        print("Test Scenario Failed surviving: " + str(elapsed_time))
    elif(elapsed_time > 0.450):
        print('move: ' + str(move))
        print("Test Scenario Failed by time: " + str(elapsed_time))
    else:
        print("Test Scenario passed with time: " + str(elapsed_time))
    start = time.time()
    print("---------------------------------")
    
    print("Time elsapsed: " + str(elapsed_time))