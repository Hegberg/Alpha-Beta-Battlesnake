import time
import os

from algorithms.get_move import get_move

if __name__ == '__main__':

    tests_passed = 0
    start = time.time()
    
    #should not go left and die, probably down is best
    data = {'game': {'id': '329b5665-21be-4597-8809-0315d51c539b', 'timeout': 500}, 'turn': 33, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_dRwcPMk9f9tw67rBgb4qWVGf', 'name': 'Nessegrev-flood', 'health': 86, 'body': [{'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 4, 'y': 1}, {'x': 3, 'y': 1}, {'x': 2, 'y': 1}, {'x': 2, 'y': 2}], 'head': {'x': 5, 'y': 2}, 'length': 6, 'shout': ''}, {'id': 'gs_v68JVdmr7dw8j4WmMVxhJQS6', 'name': 'Head Hunter', 'health': 97, 'body': [{'x': 8, 'y': 1}, {'x': 7, 'y': 1}, {'x': 6, 'y': 1}, {'x': 6, 'y': 2}, {'x': 6, 'y': 3}, {'x': 5, 'y': 3}], 'head': {'x': 8, 'y': 1}, 'length': 6, 'shout': ''}, {'id': 'gs_MC8tDDKXjMS9mTGYfWWh8dSK', 'name': 'Git Adder (2)', 'health': 93, 'body': [{'x': 6, 'y': 7}, {'x': 6, 'y': 8}, {'x': 6, 'y': 9}, {'x': 5, 'y': 9}, {'x': 4, 'y': 9}, {'x': 4, 'y': 8}, {'x': 4, 'y': 7}, {'x': 4, 'y': 6}], 'head': {'x': 6, 'y': 7}, 'length': 8, 'shout': ''}, {'id': 'gs_7Jh8pSyYxh3rg4Cd6PKV6jRM', 'name': "Whitish's BlackHole", 'health': 69, 'body': [{'x': 7, 'y': 6}, {'x': 8, 'y': 6}, {'x': 9, 'y': 6}, {'x': 10, 'y': 6}], 'head': {'x': 7, 'y': 6}, 'length': 4, 'shout': ''}], 'food': [{'x': 5, 'y': 1}, {'x': 6, 'y': 0}, {'x': 2, 'y': 10}], 'hazards': []}, 'you': {'id': 'gs_7Jh8pSyYxh3rg4Cd6PKV6jRM', 'name': "Whitish's BlackHole", 'health': 69, 'body': [{'x': 7, 'y': 6}, {'x': 8, 'y': 6}, {'x': 9, 'y': 6}, {'x': 10, 'y': 6}], 'head': {'x': 7, 'y': 6}, 'length': 4, 'shout': ''}}

    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'left'):
        print("Test Case 1 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 1 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 1 passed with time: " + str(elapsed_time))
        tests_passed += 1

    start = time.time()
    print("---------------------------------")
    
    #should not go right and die
    data = {'game': {'id': '64ec0cf6-f2fe-4ed3-9c29-1ad2efde942e', 'timeout': 500}, 'turn': 6, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_KHXBrGGP7jmJXWvqvSGMmgk6', 'name': 'Nessegrev-flood', 'health': 99, 'body': [{'x': 8, 'y': 2}, {'x': 8, 'y': 3}, {'x': 8, 'y': 4}, {'x': 8, 'y': 5}, {'x': 8, 'y': 6}], 'head': {'x': 8, 'y': 2}, 'length': 5, 'shout': ''}, {'id': 'gs_R34SyTTbFB6xvHGWCBFDB3PS', 'name': 'Head Hunter', 'health': 96, 'body': [{'x': 5, 'y': 7}, {'x': 6, 'y': 7}, {'x': 7, 'y': 7}, {'x': 7, 'y': 8}], 'head': {'x': 5, 'y': 7}, 'length': 4, 'shout': ''}, {'id': 'gs_8TDWvQDdcrwWfHF96hg8SrWW', 'name': 'Git Adder (2)', 'health': 96, 'body': [{'x': 9, 'y': 1}, {'x': 8, 'y': 1}, {'x': 7, 'y': 1}, {'x': 7, 'y': 2}], 'head': {'x': 9, 'y': 1}, 'length': 4, 'shout': ''}, {'id': 'gs_MhjjfmwWJK3pGVwvVBbRPKHG', 'name': "Whitish's BlackHole", 'health': 94, 'body': [{'x': 6, 'y': 2}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}], 'head': {'x': 6, 'y': 2}, 'length': 3, 'shout': ''}], 'food': [{'x': 2, 'y': 0}, {'x': 5, 'y': 5}], 'hazards': []}, 'you': {'id': 'gs_MhjjfmwWJK3pGVwvVBbRPKHG', 'name': "Whitish's BlackHole", 'health': 94, 'body': [{'x': 6, 'y': 2}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}], 'head': {'x': 6, 'y': 2}, 'length': 3, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'right'):
        print("Test Case 2 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 2 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 2 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")


    #should not go down and die
    data = {'game': {'id': '4b44c8de-a7e7-432c-a57e-3ba2e12a70fc', 'timeout': 500}, 'turn': 16, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_BDSMxR8GXTXRJ4mqpS6mvctP', 'name': "Whitish's BlackHole", 'health': 84, 'body': [{'x': 9, 'y': 9}, {'x': 9, 'y': 10}, {'x': 8, 'y': 10}], 'head': {'x': 9, 'y': 9}, 'length': 3, 'shout': ''}, {'id': 'gs_KhhBXvXRWBHDTyHq4XhKPqWc', 'name': 'Git Adder (2)', 'health': 92, 'body': [{'x': 5, 'y': 7}, {'x': 4, 'y': 7}, {'x': 4, 'y': 6}, {'x': 3, 'y': 6}, {'x': 3, 'y': 5}], 'head': {'x': 5, 'y': 7}, 'length': 5, 'shout': ''}, {'id': 'gs_47QKcTyFTj3tXfB6tFfj9kcV', 'name': 'Head Hunter', 'health': 88, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 7}, {'x': 9, 'y': 7}, {'x': 9, 'y': 6}], 'head': {'x': 8, 'y': 8}, 'length': 4, 'shout': ''}, {'id': 'gs_9pgPD4wpfQRGPxJwcHbfMdyS', 'name': 'Nessegrev-flood', 'health': 86, 'body': [{'x': 6, 'y': 10}, {'x': 5, 'y': 10}, {'x': 5, 'y': 9}, {'x': 4, 'y': 9}], 'head': {'x': 6, 'y': 10}, 'length': 4, 'shout': ''}], 'food': [{'x': 10, 'y': 2}], 'hazards': []}, 'you': {'id': 'gs_BDSMxR8GXTXRJ4mqpS6mvctP', 'name': "Whitish's BlackHole", 'health': 84, 'body': [{'x': 9, 'y': 9}, {'x': 9, 'y': 10}, {'x': 8, 'y': 10}], 'head': {'x': 9, 'y': 9}, 'length': 3, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'down'):
        print("Test Case 3 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 3 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 3 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")

    #should not go left and die
    data = {'game': {'id': '5ff16f8d-9105-4c0b-b42f-8eaab1f5301e', 'timeout': 500}, 'turn': 26, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_fB9CJQSFdY9jGSfk6Q4WdcJX', 'name': 'Git Adder (2)', 'health': 82, 'body': [{'x': 3, 'y': 5}, {'x': 4, 'y': 5}, {'x': 4, 'y': 4}, {'x': 4, 'y': 3}, {'x': 4, 'y': 2}], 'head': {'x': 3, 'y': 5}, 'length': 5, 'shout': ''}, {'id': 'gs_BfPFRGKGFh633bGQwxXwHdmR', 'name': 'Head Hunter', 'health': 96, 'body': [{'x': 7, 'y': 3}, {'x': 6, 'y': 3}, {'x': 6, 'y': 4}, {'x': 6, 'y': 5}, {'x': 7, 'y': 5}], 'head': {'x': 7, 'y': 3}, 'length': 5, 'shout': ''}, {'id': 'gs_CCRBtM36WVQvqbQbMHb9wRBX', 'name': 'Nessegrev-flood', 'health': 98, 'body': [{'x': 9, 'y': 7}, {'x': 9, 'y': 8}, {'x': 9, 'y': 9}, {'x': 8, 'y': 9}, {'x': 7, 'y': 9}, {'x': 6, 'y': 9}], 'head': {'x': 9, 'y': 7}, 'length': 6, 'shout': ''}, {'id': 'gs_HvQtrBBWkfG39KcKSWVmgYk9', 'name': "Whitish's BlackHole", 'health': 76, 'body': [{'x': 8, 'y': 2}, {'x': 8, 'y': 3}, {'x': 9, 'y': 3}, {'x': 10, 'y': 3}], 'head': {'x': 8, 'y': 2}, 'length': 4, 'shout': ''}], 'food': [{'x': 10, 'y': 1}], 'hazards': []}, 'you': {'id': 'gs_HvQtrBBWkfG39KcKSWVmgYk9', 'name': "Whitish's BlackHole", 'health': 76, 'body': [{'x': 8, 'y': 2}, {'x': 8, 'y': 3}, {'x': 9, 'y': 3}, {'x': 10, 'y': 3}], 'head': {'x': 8, 'y': 2}, 'length': 4, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'left'):
        print("Test Case 4 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 4 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 4 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")

    #should not go down and die
    data = {'game': {'id': 'bf540c09-3688-46ca-b6ab-5e5181a0071e', 'timeout': 500}, 'turn': 49, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_kPwTqWW988kTjqSBJxxttpXY', 'name': "Whitish's BlackHole", 'health': 55, 'body': [{'x': 6, 'y': 9}, {'x': 5, 'y': 9}, {'x': 4, 'y': 9}, {'x': 3, 'y': 9}, {'x': 2, 'y': 9}], 'head': {'x': 6, 'y': 9}, 'length': 5, 'shout': ''}, {'id': 'gs_GBmpKGbVDWpgY3G637wx3MpP', 'name': 'Nessegrev-flood', 'health': 99, 'body': [{'x': 5, 'y': 8}, {'x': 5, 'y': 7}, {'x': 5, 'y': 6}, {'x': 6, 'y': 6}, {'x': 6, 'y': 5}, {'x': 6, 'y': 4}, {'x': 5, 'y': 4}, {'x': 4, 'y': 4}], 'head': {'x': 5, 'y': 8}, 'length': 8, 'shout': ''}, {'id': 'gs_VxPGXhc986vkTm64xVYRQFKP', 'name': 'Head Hunter', 'health': 55, 'body': [{'x': 0, 'y': 7}, {'x': 1, 'y': 7}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}], 'head': {'x': 0, 'y': 7}, 'length': 4, 'shout': ''}, {'id': 'gs_G73VwwrDqyMCwBKWV7vGtRyQ', 'name': 'Git Adder (2)', 'health': 97, 'body': [{'x': 7, 'y': 4}, {'x': 8, 'y': 4}, {'x': 9, 'y': 4}, {'x': 9, 'y': 5}, {'x': 9, 'y': 6}, {'x': 9, 'y': 7}, {'x': 8, 'y': 7}], 'head': {'x': 7, 'y': 4}, 'length': 7, 'shout': ''}], 'food': [{'x': 1, 'y': 10}, {'x': 0, 'y': 9}], 'hazards': []}, 'you': {'id': 'gs_kPwTqWW988kTjqSBJxxttpXY', 'name': "Whitish's BlackHole", 'health': 55, 'body': [{'x': 6, 'y': 9}, {'x': 5, 'y': 9}, {'x': 4, 'y': 9}, {'x': 3, 'y': 9}, {'x': 2, 'y': 9}], 'head': {'x': 6, 'y': 9}, 'length': 5, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'down'):
        print("Test Case 5 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 5 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 5 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")

    data = {'game': {'id': 'a5839c7f-d6e5-4f8c-bcd3-f35c6e8e36ed', 'timeout': 500}, 'turn': 17, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_gw4CWGFxMJ67hT3WH9DMGRtJ', 'name': 'Head Hunter', 'health': 97, 'body': [{'x': 5, 'y': 0}, {'x': 6, 'y': 0}, {'x': 7, 'y': 0}, {'x': 8, 'y': 0}, {'x': 8, 'y': 1}], 'head': {'x': 5, 'y': 0}, 'length': 5, 'shout': ''}, {'id': 'gs_SjqTFd83VXcV6wyJxXrQxv6J', 'name': 'Nessegrev-flood', 'health': 91, 'body': [{'x': 6, 'y': 3}, {'x': 7, 'y': 3}, {'x': 8, 'y': 3}, {'x': 8, 'y': 2}, {'x': 7, 'y': 2}], 'head': {'x': 6, 'y': 3}, 'length': 5, 'shout': ''}, {'id': 'gs_9tXRThhMWWGq7pT8Sq99ptRB', 'name': "Whitish's BlackHole", 'health': 83, 'body': [{'x': 5, 'y': 4}, {'x': 6, 'y': 4}, {'x': 7, 'y': 4}], 'head': {'x': 5, 'y': 4}, 'length': 3, 'shout': ''}, {'id': 'gs_ffXMtVpv6cPP4WvXQvjSHPB3', 'name': 'Git Adder (2)', 'health': 85, 'body': [{'x': 4, 'y': 3}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}, {'x': 3, 'y': 3}], 'head': {'x': 4, 'y': 3}, 'length': 4, 'shout': ''}], 'food': [{'x': 0, 'y': 0}], 'hazards': []}, 'you': {'id': 'gs_9tXRThhMWWGq7pT8Sq99ptRB', 'name': "Whitish's BlackHole", 'health': 83, 'body': [{'x': 5, 'y': 4}, {'x': 6, 'y': 4}, {'x': 7, 'y': 4}], 'head': {'x': 5, 'y': 4}, 'length': 3, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'left'):
        print("Test Case 6 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 6 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 6 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")

    data = {'game': {'id': 'a11662d3-e1df-4285-8710-a24cc84b7af6', 'timeout': 500}, 'turn': 48, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_CX4Q37qRtDtPS3HpYQTKqC8X', 'name': 'Head Hunter', 'health': 95, 'body': [{'x': 5, 'y': 7}, {'x': 5, 'y': 6}, {'x': 5, 'y': 5}, {'x': 6, 'y': 5}, {'x': 7, 'y': 5}, {'x': 7, 'y': 6}], 'head': {'x': 5, 'y': 7}, 'length': 6, 'shout': ''}, {'id': 'gs_6Vhcmrp8FQMMmkkSryhXJh4B', 'name': 'Nessegrev-flood', 'health': 95, 'body': [{'x': 1, 'y': 5}, {'x': 2, 'y': 5}, {'x': 2, 'y': 4}, {'x': 2, 'y': 3}, {'x': 2, 'y': 2}, {'x': 2, 'y': 1}, {'x': 3, 'y': 1}], 'head': {'x': 1, 'y': 5}, 'length': 7, 'shout': ''}, {'id': 'gs_hDPPVBTQw8wBVxbFSBgXGhD7', 'name': "Whitish's BlackHole", 'health': 60, 'body': [{'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 5, 'y': 9}, {'x': 5, 'y': 10}], 'head': {'x': 6, 'y': 8}, 'length': 4, 'shout': ''}, {'id': 'gs_67cSG66fyPbjKPWhyQPWmw8D', 'name': 'Git Adder (2)', 'health': 75, 'body': [{'x': 1, 'y': 7}, {'x': 1, 'y': 6}, {'x': 2, 'y': 6}, {'x': 2, 'y': 7}, {'x': 2, 'y': 8}], 'head': {'x': 1, 'y': 7}, 'length': 5, 'shout': ''}], 'food': [{'x': 10, 'y': 0}], 'hazards': []}, 'you': {'id': 'gs_hDPPVBTQw8wBVxbFSBgXGhD7', 'name': "Whitish's BlackHole", 'health': 60, 'body': [{'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 5, 'y': 9}, {'x': 5, 'y': 10}], 'head': {'x': 6, 'y': 8}, 'length': 4, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'down'):
        print("Test Case 7 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 7 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 7 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")

    #should not go down and die, up is best
    data = {'game': {'id': '409df039-c57f-4063-9211-feaa917c7692', 'timeout': 500}, 'turn': 140, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_wCByqP3ghYXQRcY4hRR8yg9X', 'name': 'Nessegrev-flood', 'health': 98, 'body': [{'x': 7, 'y': 5}, {'x': 8, 'y': 5}, {'x': 8, 'y': 6}, {'x': 9, 'y': 6}, {'x': 9, 'y': 7}, {'x': 9, 'y': 8}, {'x': 9, 'y': 9}, {'x': 9, 'y': 10}, {'x': 10, 'y': 10}, {'x': 10, 'y': 9}, {'x': 10, 'y': 8}, {'x': 10, 'y': 7}, {'x': 10, 'y': 6}, {'x': 10, 'y': 5}, {'x': 10, 'y': 4}], 'head': {'x': 7, 'y': 5}, 'length': 15, 'shout': ''}, {'id': 'gs_Xh3yV83Dk4tVfGFK7bwdFKdF', 'name': "Whitish's BlackHole", 'health': 90, 'body': [{'x': 0, 'y': 6}, {'x': 1, 'y': 6}, {'x': 1, 'y': 7}, {'x': 1, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 9}, {'x': 2, 'y': 10}, {'x': 3, 'y': 10}, {'x': 4, 'y': 10}], 'head': {'x': 0, 'y': 6}, 'length': 9, 'shout': ''}, {'id': 'gs_7JV9kYMWJXMmS6DrpgGXdmYW', 'name': 'Git Adder (2)', 'health': 90, 'body': [{'x': 1, 'y': 5}, {'x': 2, 'y': 5}, {'x': 3, 'y': 5}, {'x': 3, 'y': 6}, {'x': 3, 'y': 7}, {'x': 4, 'y': 7}, {'x': 5, 'y': 7}, {'x': 6, 'y': 7}, {'x': 6, 'y': 6}, {'x': 5, 'y': 6}, {'x': 4, 'y': 6}], 'head': {'x': 1, 'y': 5}, 'length': 11, 'shout': ''}], 'food': [{'x': 0, 'y': 5}], 'hazards': []}, 'you': {'id': 'gs_Xh3yV83Dk4tVfGFK7bwdFKdF', 'name': "Whitish's BlackHole", 'health': 90, 'body': [{'x': 0, 'y': 6}, {'x': 1, 'y': 6}, {'x': 1, 'y': 7}, {'x': 1, 'y': 8},  {'x': 2, 'y': 8}, {'x': 2, 'y': 9}, {'x': 2, 'y': 10}, {'x': 3, 'y': 10}, {'x': 4, 'y': 10}], 'head': {'x': 0, 'y': 6}, 'length': 9, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'down'):
        print("Test Case 8 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 8 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 8 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")
    
    #should not go left and die, right is best
    data = {'game': {'id': '409df039-c57f-4063-9211-feaa917c7692', 'timeout': 500}, 'turn': 140, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_wCByqP3ghYXQRcY4hRR8yg9X', 'name': 'Nessegrev-flood', 'health': 98, 'body': [{'x': 0, 'y': 3}, {'x': 1, 'y': 3}, {'x': 1, 'y': 4}, {'x': 1, 'y': 5}, {'x':1, 'y': 6}, {'x': 1, 'y': 7}, {'x': 2, 'y': 7}, {'x': 3, 'y': 7}, {'x': 4, 'y': 7}, {'x': 4, 'y': 8}, {'x': 5, 'y': 8}, {'x': 6, 'y': 8}, {'x': 7, 'y': 8}, {'x': 7, 'y': 9}, {'x': 6, 'y': 9}, {'x': 6, 'y': 10}, {'x': 5, 'y': 10}, {'x': 4, 'y': 10}], 'head': {'x': 0, 'y': 3}, 'length': 18, 'shout': ''}, {'id': 'gs_Xh3yV83Dk4tVfGFK7bwdFKdF', 'name': "Whitish's BlackHole", 'health': 90, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 2}, {'x': 2, 'y': 1}, {'x': 3, 'y': 1}], 'head': {'x': 1, 'y': 0}, 'length': 6, 'shout': ''}, {'id': 'gs_7JV9kYMWJXMmS6DrpgGXdmYW', 'name': 'Git Adder (2)', 'health': 90, 'body': [{'x': 9, 'y':4}, {'x': 9, 'y': 5}, {'x': 8, 'y': 5}, {'x': 8, 'y': 6}, {'x': 9, 'y': 6}, {'x': 9, 'y': 7}, {'x': 10, 'y': 7}, {'x': 10, 'y': 6}], 'head': {'x': 9, 'y': 4}, 'length': 8, 'shout': ''}], 'food': [{'x': 0, 'y': 0}], 'hazards': []}, 'you': {'id': 'gs_Xh3yV83Dk4tVfGFK7bwdFKdF', 'name': "Whitish's BlackHole", 'health': 90, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 2}, {'x': 2, 'y': 1}, {'x': 3, 'y': 1}], 'head': {'x': 1, 'y': 0}, 'length': 6, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (not move == 'right'):
        print("Test Case 9 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 9 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 9 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")
    
    data = {'game': {'id': '365806eb-5391-42bd-9553-a4a3de0ec5b8', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 144, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_88kYRYMyWFjwBSF4GxqhpVd7', 'name': 'BlackHole', 'latency': '0', 'health': 99, 'body': [{'x': 5, 'y': 7}, {'x': 4, 'y': 7}, {'x': 3, 'y': 7}, {'x': 2, 'y': 7}, {'x': 1, 'y': 7}, {'x': 1, 'y': 6}, {'x': 1, 'y': 5}, {'x': 2, 'y': 5}, {'x': 3, 'y': 5}, {'x': 4, 'y': 5}, {'x': 4, 'y': 6}, {'x': 5, 'y': 6}, {'x': 5, 'y': 5}, {'x': 5, 'y': 4}, {'x': 6, 'y': 4}], 'head': {'x': 5, 'y': 7}, 'length': 15, 'shout': ''}, {'id': 'gs_ptGhK3Cpq7QFhJPjtj3x98HM', 'name': 'Nessegrev-beta', 'latency': '282', 'health': 83, 'body': [{'x': 5, 'y': 3}, {'x': 6, 'y': 3}, {'x': 7, 'y': 3}, {'x': 8, 'y': 3}, {'x': 8, 'y': 4}, {'x': 8, 'y': 5}, {'x': 8, 'y': 6}, {'x': 9, 'y': 6}, {'x': 9, 'y': 7}, {'x': 8, 'y': 7}, {'x': 7, 'y': 7}, {'x': 6, 'y': 7}, {'x': 6, 'y': 8}, {'x': 6, 'y': 9}], 'head': {'x': 5, 'y': 3}, 'length': 14, 'shout': ''}], 'food': [{'x': 2, 'y': 10}, {'x': 9, 'y': 9}], 'hazards': []}, 'you': {'id': 'gs_88kYRYMyWFjwBSF4GxqhpVd7', 'name': 'BlackHole', 'latency': '0', 'health': 99, 'body': [{'x': 5, 'y': 7}, {'x': 4, 'y': 7}, {'x': 3, 'y': 7}, {'x': 2, 'y': 7}, {'x': 1, 'y': 7}, {'x': 1, 'y': 6}, {'x': 1, 'y': 5}, {'x': 2, 'y': 5}, {'x': 3, 'y': 5}, {'x': 4, 'y': 5}, {'x': 4, 'y': 6}, {'x': 5, 'y': 6}, {'x': 5, 'y': 5}, {'x': 5, 'y': 4}, {'x': 6, 'y': 4}], 'head': {'x': 5, 'y': 7}, 'length': 15, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (not move == 'up'):
        print("Test Case 10 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 10 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 10 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")
    
    data = {'game': {'id': '7f0d0029-d02a-4088-aa32-d2c09f3a50c8', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 145, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_xwptHy8qpwY3Yc8DQKMSqFD9', 'name': 'BlackHole', 'latency': '0', 'health': 82, 'body': [{'x': 3, 'y': 0}, {'x': 3, 'y': 1}, {'x': 3, 'y': 2}, {'x': 4, 'y': 2}, {'x': 5, 'y': 2}, {'x': 5, 'y': 3}, {'x': 6, 'y': 3}, {'x': 6, 'y': 4}, {'x': 6, 'y': 5}, {'x': 6, 'y': 6}, {'x': 5, 'y': 6}, {'x': 5, 'y': 5}, {'x': 5, 'y': 4}], 'head': {'x': 3, 'y': 0}, 'length': 13, 'shout': ''}, {'id': 'gs_SymJYfxSTFvxyxtWCjpXW3DD', 'name': 'Git Adder (2)', 'latency': '66', 'health': 88, 'body': [{'x': 2, 'y': 1}, {'x': 2, 'y': 2}, {'x': 2, 'y': 3}, {'x': 2, 'y': 4}, {'x': 2, 'y': 5}, {'x': 2, 'y': 6}, {'x': 2, 'y': 7}, {'x': 3, 'y': 7}, {'x': 4, 'y': 7}, {'x': 5, 'y': 7}, {'x': 5, 'y': 8}, {'x': 5, 'y': 9}, {'x': 5, 'y': 10}, {'x': 6, 'y': 10}, {'x': 7, 'y': 10}], 'head': {'x': 2, 'y': 1}, 'length': 15, 'shout': ''}], 'food': [{'x': 10, 'y': 3}, {'x': 0, 'y': 10}, {'x': 1, 'y': 8}, {'x': 1, 'y': 0}, {'x': 10, 'y': 6}, {'x': 0, 'y': 3}], 'hazards': []}, 'you': {'id': 'gs_xwptHy8qpwY3Yc8DQKMSqFD9', 'name': 'BlackHole', 'latency': '0', 'health': 82, 'body': [{'x': 3, 'y': 0}, {'x': 3, 'y': 1}, {'x': 3, 'y': 2}, {'x': 4, 'y': 2}, {'x': 5, 'y': 2}, {'x': 5, 'y': 3}, {'x': 6, 'y': 3}, {'x': 6, 'y': 4}, {'x': 6, 'y': 5}, {'x': 6, 'y': 6}, {'x': 5, 'y': 6}, {'x': 5, 'y': 5}, {'x': 5, 'y': 4}], 'head': {'x': 3, 'y': 0}, 'length': 13, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (not move == 'right'):
        print("Test Case 11 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 11 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 11 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")

    data = {'game': {'id': 'a2042d59-6a93-4026-b09d-ff56209f8c8a', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 383, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_BSFF36CFHT8QrBWF6X7QqS49', 'name': 'Git Adder (2)', 'latency': '73', 'health': 100, 'body': [{'x': 3, 'y': 10}, {'x': 2, 'y': 10}, {'x': 1, 'y': 10}, {'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}, {'x': 0, 'y': 6}, {'x': 0, 'y': 5}, {'x': 1, 'y': 5}, {'x': 2, 'y': 5}, {'x': 2, 'y': 6}, {'x': 3, 'y': 6}, {'x': 3, 'y': 7}, {'x': 3, 'y': 8}, {'x': 4, 'y': 8}, {'x': 4, 'y': 7}, {'x': 5, 'y': 7}, {'x': 6, 'y': 7}, {'x': 6, 'y': 8}, {'x': 7, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}, {'x': 9, 'y': 10}, {'x': 9, 'y': 9}, {'x': 9, 'y': 8}, {'x': 9, 'y': 7}, {'x': 9, 'y': 6}, {'x': 9, 'y': 5}, {'x': 8, 'y': 5}, {'x': 7, 'y': 5}, {'x': 6, 'y': 5}, {'x': 6, 'y': 5}], 'head': {'x': 3, 'y': 10}, 'length': 34, 'shout': ''}, {'id': 'gs_j6SFK8wBQrPrcbVwf37WMc8J', 'name': 'BlackHole', 'latency': '0', 'health': 57, 'body': [{'x': 10, 'y': 1}, {'x': 9, 'y': 1}, {'x': 8, 'y': 1}, {'x': 7, 'y': 1}, {'x': 6, 'y': 1}, {'x': 5, 'y': 1}, {'x': 4, 'y': 1}, {'x': 3, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 2}, {'x': 2, 'y': 3}, {'x': 3, 'y': 3}], 'head': {'x': 10, 'y': 1}, 'length': 12, 'shout': ''}], 'food': [{'x': 9, 'y': 0}, {'x': 5, 'y': 0}, {'x': 3, 'y': 0}, {'x': 7, 'y': 3}], 'hazards': []}, 'you': {'id': 'gs_j6SFK8wBQrPrcbVwf37WMc8J', 'name': 'BlackHole', 'latency': '0', 'health': 57, 'body': [{'x': 10, 'y': 1}, {'x': 9, 'y': 1}, {'x': 8, 'y': 1}, {'x': 7, 'y': 1}, {'x': 6, 'y': 1}, {'x': 5, 'y': 1}, {'x': 4, 'y': 1}, {'x': 3, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 2}, {'x': 2, 'y': 3}, {'x': 3, 'y': 3}], 'head': {'x': 10, 'y': 1}, 'length': 12, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (not move == 'up'):
        print("Test Case 12 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 12 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 12 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")

    data = {'game': {'id': '74c1d20f-6b7d-44b2-85d8-fed55b8141ab', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 233, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_Cw7pMSKDvjYJkYRxm4BFyKmB', 'name': 'BlackHole', 'latency': '0', 'health': 93, 'body': [{'x': 7, 'y': 4}, {'x': 6, 'y': 4}, {'x': 5, 'y': 4}, {'x': 4, 'y': 4}, {'x': 3, 'y': 4}, {'x': 2, 'y': 4}, {'x': 2, 'y': 3}, {'x': 1, 'y': 3}, {'x': 0, 'y': 3}, {'x': 0, 'y': 2}, {'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 2}], 'head': {'x': 7, 'y': 4}, 'length': 14, 'shout': ''}, {'id': 'gs_4943KqVyjGPXr4rBxKcHtdP3', 'name': 'Git Adder (2)', 'latency': '79', 'health': 69, 'body': [{'x': 6, 'y': 5}, {'x': 5, 'y': 5}, {'x': 4, 'y': 5}, {'x': 3, 'y': 5}, {'x': 2, 'y': 5}, {'x': 2, 'y': 6}, {'x': 2, 'y': 7}, {'x': 3, 'y': 7}, {'x': 4, 'y': 7}, {'x': 5, 'y': 7}, {'x': 6, 'y': 7}, {'x': 6, 'y': 8}, {'x': 7, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 7}, {'x': 8, 'y': 6}, {'x': 8, 'y': 5}, {'x': 8, 'y': 4}, {'x': 8, 'y': 3}, {'x': 8, 'y': 2}, {'x': 7, 'y': 2}, {'x': 7, 'y': 3}], 'head': {'x': 6, 'y': 5}, 'length': 22, 'shout': ''}], 'food': [{'x': 0, 'y': 0}, {'x': 9, 'y': 1}], 'hazards': []}, 'you': {'id': 'gs_Cw7pMSKDvjYJkYRxm4BFyKmB', 'name': 'BlackHole', 'latency': '0', 'health': 93, 'body': [{'x': 7, 'y': 4}, {'x': 6, 'y': 4}, {'x': 5, 'y': 4}, {'x': 4, 'y': 4}, {'x': 3, 'y': 4}, {'x': 2, 'y': 4}, {'x': 2, 'y': 3}, {'x': 1, 'y': 3}, {'x': 0, 'y': 3}, {'x': 0, 'y': 2}, {'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 2, 'y': 2}], 'head': {'x': 7, 'y': 4}, 'length': 14, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (not move == 'down'):
        print("Test Case 13 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 13 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 13 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")

    data = {'game': {'id': '4c8bd23e-eeb2-47c1-b468-188fdd0b2834', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 121, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_PvykvqvPDxVmbkBThxQWfvjM', 'name': 'Shielded_Woodland', 'latency': '465', 'health': 79, 'body': [{'x': 8, 'y': 3}, {'x': 9, 'y': 3}, {'x': 9, 'y': 2}, {'x': 8, 'y': 2}, {'x': 7, 'y': 2}, {'x': 7, 'y': 1}, {'x': 6, 'y': 1}, {'x': 6, 'y': 2}, {'x': 6, 'y': 3}, {'x': 7, 'y': 3}, {'x': 7, 'y': 4}, {'x': 7, 'y': 5}], 'head': {'x': 8, 'y': 3}, 'length': 12, 'shout': ''}, {'id': 'gs_pKJg7QV6Kr43WjH7BhrFXMP3', 'name': 'Head Hunter', 'latency': '76', 'health': 95, 'body': [{'x': 9, 'y': 0}, {'x': 8, 'y': 0}, {'x': 7, 'y': 0}, {'x': 6, 'y': 0}, {'x': 5, 'y': 0}, {'x': 4, 'y': 0}, {'x': 4, 'y': 1}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}, {'x': 2, 'y': 2}, {'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 4}], 'head': {'x': 9, 'y': 0}, 'length': 13, 'shout': ''}], 'food': [{'x': 10, 'y': 9}, {'x': 10, 'y': 8}, {'x': 8, 'y': 5}, {'x': 3, 'y': 5}], 'hazards': []}, 'you': {'id': 'gs_PvykvqvPDxVmbkBThxQWfvjM', 'name': 'Shielded_Woodland', 'latency': '465', 'health': 79, 'body': [{'x': 8, 'y': 3}, {'x': 9, 'y': 3}, {'x': 9, 'y': 2}, {'x': 8, 'y': 2}, {'x': 7, 'y': 2}, {'x': 7, 'y': 1}, {'x': 6, 'y': 1}, {'x': 6, 'y': 2}, {'x': 6, 'y': 3}, {'x': 7, 'y': 3}, {'x': 7, 'y': 4}, {'x': 7, 'y': 5}], 'head': {'x': 8, 'y': 3}, 'length': 12, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (not move == 'up'):
        print("Test Case 14 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 14 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 14 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")

    data = {'game': {'id': '51b8208d-016f-40a9-b908-76950d5b6916', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 54, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_qd4jrfR3XT9T3FG7XWgRGrBB', 'name': 'Shielded_Woodland', 'latency': '462', 'health': 94, 'body': [{'x': 0, 'y': 6}, {'x': 1, 'y': 6}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}, {'x': 1, 'y': 5}], 'head': {'x': 0, 'y': 6}, 'length': 5, 'shout': ''}, {'id': 'gs_mJ3Hw9GgmVpxH67yySx8VCFQ', 'name': 'Head Hunter', 'latency': '83', 'health': 92, 'body': [{'x': 3, 'y': 9}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}], 'head': {'x': 3, 'y': 9}, 'length': 6, 'shout': ''}, {'id': 'gs_8hvwf8cb8Txyp8cbKgSCkk39', 'name': 'Git Adder (2)', 'latency': '96', 'health': 83, 'body': [{'x': 5, 'y': 5}, {'x': 4, 'y': 5}, {'x': 3, 'y': 5}, {'x': 3, 'y': 4}, {'x': 4, 'y': 4}, {'x': 5, 'y': 4}, {'x': 6, 'y': 4}], 'head': {'x': 5, 'y': 5}, 'length': 7, 'shout': ''}, {'id': 'gs_YSVThRYWMGFjChJpMk8MjrjY', 'name': 'Nessegrev-beta', 'latency': '283', 'health': 93, 'body': [{'x': 6, 'y': 2}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}, {'x': 2, 'y': 2}, {'x': 1, 'y': 2}, {'x': 0, 'y': 2}], 'head': {'x': 6, 'y': 2}, 'length': 7, 'shout': ''}], 'food': [{'x': 8, 'y': 5}, {'x': 6, 'y': 6}, {'x': 4, 'y': 9}], 'hazards': []}, 'you': {'id': 'gs_qd4jrfR3XT9T3FG7XWgRGrBB', 'name': 'Shielded_Woodland', 'latency': '462', 'health': 94, 'body': [{'x': 0, 'y': 6}, {'x': 1, 'y': 6}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}, {'x': 1, 'y': 5}], 'head': {'x': 0, 'y': 6}, 'length': 5, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (not move == 'down'):
        print("Test Case 15 Failed surviving")
    elif(elapsed_time > 0.450):
        print("Test Case 15 Failed by time: " + str(elapsed_time))
    else:
        print("Test case 15 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")
    
    #This needs to be down, if up will die to proper play, should always be following tail down here and not going up
    data = {'game': {'id': '95c16ff5-0a66-4488-911c-5185c915f0ca', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 251, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_3hYgSK3X9cSFmR8mxD4cHKDY', 'name': 'Shielded_Woodland', 'latency': '255', 'health': 66, 'body': [{'x': 4, 'y': 7}, {'x': 3, 'y': 7}, {'x': 3, 'y': 8}, {'x': 3, 'y': 9}, {'x': 2, 'y': 9}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}, {'x': 3, 'y': 5}, {'x': 3, 'y': 4}, {'x': 4, 'y': 4}, {'x': 5, 'y': 4}, {'x': 5, 'y': 5}, {'x': 4, 'y': 5}, {'x': 4, 'y': 6}], 'head': {'x': 4, 'y': 7}, 'length': 16, 'shout': ''}, {'id': 'gs_TdH4RQQr48Sb4tgmSXxqRtgY', 'name': 'Git Adder (2)', 'latency': '93', 'health': 55, 'body': [{'x': 7, 'y': 2}, {'x': 7, 'y': 3}, {'x': 7, 'y': 4}, {'x': 7, 'y': 5}, {'x': 7, 'y': 6}, {'x': 7, 'y': 7}, {'x': 7, 'y': 8}, {'x': 6, 'y': 8}, {'x': 6, 'y': 9}, {'x': 6, 'y': 10}, {'x': 5, 'y': 10}, {'x': 5, 'y': 9}, {'x': 5, 'y': 8}, {'x': 5, 'y': 7}, {'x': 6, 'y': 7}, {'x': 6, 'y': 6}, {'x': 6, 'y': 5}, {'x': 6, 'y': 4}, {'x': 6, 'y': 3}, {'x': 6, 'y': 2}, {'x': 6, 'y': 1}, {'x': 5, 'y': 1}], 'head': {'x': 7, 'y': 2}, 'length': 22, 'shout': ''}], 'food': [{'x': 0, 'y': 10}, {'x': 0, 'y': 2}, {'x': 10, 'y': 3}, {'x': 1, 'y': 2}, {'x': 1, 'y': 0}, {'x': 10, 'y': 6}], 'hazards': []}, 'you': {'id': 'gs_3hYgSK3X9cSFmR8mxD4cHKDY', 'name': 'Shielded_Woodland', 'latency': '255', 'health': 66, 'body': [{'x': 4, 'y': 7}, {'x': 3, 'y': 7}, {'x': 3, 'y': 8}, {'x': 3, 'y': 9}, {'x': 2, 'y': 9}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}, {'x': 3, 'y': 5}, {'x': 3, 'y': 4}, {'x': 4, 'y': 4}, {'x': 5, 'y': 4}, {'x': 5, 'y': 5}, {'x': 4, 'y': 5}, {'x': 4, 'y': 6}], 'head': {'x': 4, 'y': 7}, 'length': 16, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (not move == 'down'):
        print("Test Case 16 Failed surviving: " + str(elapsed_time))
        raise ValueError("Test case 16 failed by move")
    elif(elapsed_time > 0.450):
        print("Test Case 16 Failed by time: " + str(elapsed_time))
        raise ValueError("Test case 16 failed by time")
    else:
        print("Test case 16 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")
    
    """
    #Bad test case, dead no matter what move
    
    #Why is this value not -1 from dieing when hitting wall
    data = {'game': {'id': '5a1a805d-1e1b-4e83-8e66-0117305f2f3e', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 252, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_tQwdRJbkrpGBD6GFrPR89Ttd', 'name': 'Shielded_Woodland', 'latency': '176', 'health': 95, 'body': [{'x': 2, 'y': 2}, {'x': 1, 'y': 2}, {'x': 0, 'y': 2}, {'x': 0, 'y': 3}, {'x': 0, 'y': 4}, {'x': 0, 'y': 5}, {'x': 0, 'y': 6}, {'x': 0, 'y': 7}, {'x': 0, 'y': 8}, {'x': 0, 'y': 9}, {'x': 0, 'y': 10}, {'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}, {'x': 1, 'y': 6}, {'x': 1, 'y': 5}], 'head': {'x': 2, 'y': 2}, 'length': 17, 'shout': ''}, {'id': 'gs_WqcfqvhfPMD737rCJKqdRx4b', 'name': 'Git Adder (2)', 'latency': '81', 'health': 66, 'body': [{'x': 5, 'y': 1}, {'x': 6, 'y': 1}, {'x': 7, 'y': 1}, {'x': 8, 'y': 1}, {'x': 9, 'y': 1}, {'x': 9, 'y': 2}, {'x': 9, 'y': 3}, {'x': 8, 'y': 3}, {'x': 7, 'y': 3}, {'x': 7, 'y': 2}, {'x': 6, 'y': 2}, {'x': 6, 'y': 3}, {'x': 6, 'y': 4}, {'x': 5, 'y': 4}, {'x': 4, 'y': 4}, {'x': 4, 'y': 3}, {'x': 3, 'y': 3}], 'head': {'x': 5, 'y': 1}, 'length': 17, 'shout': ''}, {'id': 'gs_Twv86PgkwBPmCY7PYYKvvXgY', 'name': 'Nessegrev-beta', 'latency': '282', 'health': 91, 'body': [{'x': 3, 'y': 5}, {'x': 3, 'y': 6}, {'x': 4, 'y': 6}, {'x': 4, 'y': 7}, {'x': 5, 'y': 7}, {'x': 6, 'y': 7}, {'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 4, 'y': 8}, {'x': 3, 'y': 8}, {'x': 3, 'y': 9}, {'x': 4, 'y': 9}, {'x': 5, 'y': 9}, {'x': 5, 'y': 10}, {'x': 6, 'y': 10}, {'x': 7, 'y': 10}, {'x': 8, 'y': 10}, {'x': 8, 'y': 9}, {'x': 8, 'y': 8}, {'x': 9, 'y': 8}], 'head': {'x': 3, 'y': 5}, 'length': 20, 'shout': ''}], 'food': [{'x': 2, 'y': 0}, {'x': 3, 'y': 0}, {'x': 2, 'y': 1}, {'x': 3, 'y': 7}], 'hazards': []}, 'you': {'id': 'gs_tQwdRJbkrpGBD6GFrPR89Ttd', 'name': 'Shielded_Woodland', 'latency': '176', 'health': 95, 'body': [{'x': 2, 'y': 2}, {'x': 1, 'y': 2}, {'x': 0, 'y': 2}, {'x': 0, 'y': 3}, {'x': 0, 'y': 4}, {'x': 0, 'y': 5}, {'x': 0, 'y': 6}, {'x': 0, 'y': 7}, {'x': 0, 'y': 8}, {'x': 0, 'y': 9}, {'x': 0, 'y': 10}, {'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}, {'x': 1, 'y': 6}, {'x': 1, 'y': 5}], 'head': {'x': 2, 'y': 2}, 'length': 17, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (not move == 'right'):
        print("Test Case 17 Failed surviving: " + str(elapsed_time))
        raise ValueError("Test case 17 failed by move")
    elif(elapsed_time > 0.450):
        print("Test Case 17 Failed by time: " + str(elapsed_time))
        raise ValueError("Test case 17 failed by time")
    else:
        print("Test case 17 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")
    """
    data = {'game': {'id': '61e5dff9-21b7-427c-abbc-c8da709f94f7', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 94, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_4kPXct7pXHXp7wGjRrgR6y7M', 'name': 'Git Adder (2)', 'latency': '98', 'health': 91, 'body': [{'x': 8, 'y': 4}, {'x': 7, 'y': 4}, {'x': 7, 'y': 3}, {'x': 8, 'y': 3}, {'x': 8, 'y': 2}, {'x': 9, 'y': 2}, {'x': 10, 'y': 2}, {'x': 10, 'y': 3}], 'head': {'x': 8, 'y': 4}, 'length': 8, 'shout': ''}, {'id': 'gs_cGJ4vfT3pHtbPm8F9SSTdgDT', 'name': 'Nessegrev-beta', 'latency': '281', 'health': 93, 'body': [{'x': 4, 'y': 2}, {'x': 4, 'y': 3}, {'x': 4, 'y': 4}, {'x': 3, 'y': 4}, {'x': 2, 'y': 4}, {'x': 1, 'y': 4}, {'x': 0, 'y': 4}, {'x': 0, 'y': 5}, {'x': 1, 'y': 5}, {'x': 1, 'y': 6}, {'x': 1, 'y': 7}, {'x': 0, 'y': 7}], 'head': {'x': 4, 'y': 2}, 'length': 12, 'shout': ''}, {'id': 'gs_GyGm4kJBpKPVdXSMxWfP99vK', 'name': 'Shielded_Woodland', 'latency': '451', 'health': 8, 'body': [{'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 5, 'y': 7}, {'x': 6, 'y': 7}], 'head': {'x': 6, 'y': 8}, 'length': 4, 'shout': ''}], 'food': [{'x': 9, 'y': 10}, {'x': 10, 'y': 9}, {'x': 4, 'y': 1}, {'x': 10, 'y': 1}], 'hazards': []}, 'you': {'id': 'gs_GyGm4kJBpKPVdXSMxWfP99vK', 'name': 'Shielded_Woodland', 'latency': '451', 'health': 8, 'body': [{'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 5, 'y': 7}, {'x': 6, 'y': 7}], 'head': {'x': 6, 'y': 8}, 'length': 4, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'down'):
        print("Test 18 Failed surviving: " + str(elapsed_time))
        raise ValueError("Test case 18 failed by move")
    elif(elapsed_time > 0.450):
        print("Test 18 Failed by time: " + str(elapsed_time))
        raise ValueError("Test case 18 failed by time")
    else:
        print("Test 18 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")
    
    data = {'game': {'id': '745fefcd-4a26-42ff-8c9c-ee47ea623350', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 33, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_rmDrMYPBgJHbbbyjmhKbrXbB', 'name': 'Nessegrev-beta', 'latency': '281', 'health': 81, 'body': [{'x': 8, 'y': 9}, {'x': 8, 'y': 8}, {'x': 7, 'y': 8}, {'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 4, 'y': 8}, {'x': 3, 'y': 8}], 'head': {'x': 8, 'y': 9}, 'length': 7, 'shout': ''}, {'id': 'gs_VxwxmVfcTTtRP9Q9Dfhg6V9b', 'name': 'Git Adder (2)', 'latency': '150', 'health': 98, 'body': [{'x': 9, 'y': 4}, {'x': 9, 'y': 3}, {'x': 9, 'y': 2}, {'x': 8, 'y': 2}, {'x': 7, 'y': 2}, {'x': 7, 'y': 3}], 'head': {'x': 9, 'y': 4}, 'length': 6, 'shout': ''}, {'id': 'gs_tfQgX8fTkbTycWQ7pW4kCmQB', 'name': 'Head Hunter', 'latency': '79', 'health': 94, 'body': [{'x': 5, 'y': 4}, {'x': 6, 'y': 4}, {'x': 7, 'y': 4}, {'x': 7, 'y': 5}, {'x': 7, 'y': 6}, {'x': 8, 'y': 6}], 'head': {'x': 5, 'y': 4}, 'length': 6, 'shout': ''}, {'id': 'gs_dtGtHTm4DxqvHWBPwvrVVvyP', 'name': 'Shielded_Woodland', 'latency': '0', 'health': 67, 'body': [{'x': 0, 'y': 3}, {'x': 1, 'y': 3}, {'x': 2, 'y': 3}], 'head': {'x': 0, 'y': 3}, 'length': 3, 'shout': ''}], 'food': [{'x': 8, 'y': 10}, {'x': 2, 'y': 0}, {'x': 9, 'y': 10}, {'x': 0, 'y': 2}], 'hazards': []}, 'you': {'id': 'gs_dtGtHTm4DxqvHWBPwvrVVvyP', 'name': 'Shielded_Woodland', 'latency': '0', 'health': 67, 'body': [{'x': 0, 'y': 3}, {'x': 1, 'y': 3}, {'x': 2, 'y': 3}], 'head': {'x': 0, 'y': 3}, 'length': 3, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'left'):
        print("Test Case 19 Failed surviving: " + str(elapsed_time))
        raise ValueError("Test case 19 failed by move")
    elif(elapsed_time > 0.450):
        print("Test Case 19 Failed by time: " + str(elapsed_time))
        raise ValueError("Test case 19 failed by time")
    else:
        print("Test case 19 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")
    
    data = {'game': {'id': '5a2a571d-b201-46d5-8252-0cb072762a70', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 330, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_ytkYgGc9y7YFBHV4fmHfjmjM', 'name': 'Nessegrev-beta', 'latency': '281', 'health': 86, 'body': [{'x': 3, 'y': 5}, {'x': 2, 'y': 5}, {'x': 2, 'y': 4}, {'x': 1, 'y': 4}, {'x': 1, 'y': 5}, {'x': 0, 'y': 5}, {'x': 0, 'y': 6}, {'x': 1, 'y': 6}, {'x': 1, 'y': 7}, {'x': 2, 'y': 7}, {'x': 2, 'y': 8}, {'x': 1, 'y': 8}, {'x': 0, 'y': 8}, {'x': 0, 'y': 9}, {'x': 0, 'y': 10}, {'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 2, 'y': 9}, {'x': 3, 'y': 9}, {'x': 3, 'y': 10}, {'x': 4, 'y': 10}, {'x': 4, 'y': 9}, {'x': 4, 'y': 8}, {'x': 5, 'y': 8}, {'x': 6, 'y': 8}, {'x': 6, 'y': 9}, {'x': 6, 'y': 10}, {'x': 7, 'y': 10}, {'x': 8, 'y': 10}, {'x': 8, 'y': 9}, {'x': 8, 'y': 8}, {'x': 7, 'y': 8}, {'x': 7, 'y': 7}, {'x': 8, 'y': 7}, {'x': 9, 'y': 7}, {'x': 9, 'y': 6}, {'x': 10, 'y': 6}, {'x': 10, 'y': 5}], 'head': {'x': 3, 'y': 5}, 'length': 38, 'shout': ''}, {'id': 'gs_Qq6JCkj7R3V9K6XvmJWpQ6GK', 'name': 'Shielded_Woodland', 'latency': '360', 'health': 64, 'body': [{'x': 2, 'y': 0}, {'x': 2, 'y': 1}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 3}, {'x': 3, 'y': 3}, {'x': 3, 'y': 2}, {'x': 3, 'y': 1}, {'x': 4, 'y': 1}, {'x': 5, 'y': 1}, {'x': 6, 'y': 1}, {'x': 7, 'y': 1}, {'x': 8, 'y': 1}, {'x': 8, 'y': 2}, {'x': 8, 'y': 3}, {'x': 7, 'y': 3}, {'x': 7, 'y': 2}, {'x': 6, 'y': 2}, {'x': 6, 'y': 3}, {'x': 5, 'y': 3}, {'x': 5, 'y': 4}], 'head': {'x': 2, 'y': 0}, 'length': 22, 'shout': ''}], 'food': [{'x': 0, 'y': 2}, {'x': 2, 'y': 2}, {'x': 9, 'y': 10}, {'x': 4, 'y': 2}, {'x': 10, 'y': 10}, {'x': 4, 'y': 3}], 'hazards': []}, 'you': {'id': 'gs_Qq6JCkj7R3V9K6XvmJWpQ6GK', 'name': 'Shielded_Woodland', 'latency': '360', 'health': 64, 'body': [{'x': 2, 'y': 0}, {'x': 2, 'y': 1}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 3}, {'x': 3, 'y': 3}, {'x': 3, 'y': 2}, {'x': 3, 'y': 1}, {'x': 4, 'y': 1}, {'x': 5, 'y': 1}, {'x': 6, 'y': 1}, {'x': 7, 'y': 1}, {'x': 8, 'y': 1}, {'x': 8, 'y': 2}, {'x': 8, 'y': 3}, {'x': 7, 'y': 3}, {'x': 7, 'y': 2}, {'x': 6, 'y': 2}, {'x': 6, 'y': 3}, {'x': 5, 'y': 3}, {'x': 5, 'y': 4}], 'head': {'x': 2, 'y': 0}, 'length': 22, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (not move == 'right'):
        print("Test Case 20 Failed surviving: " + str(elapsed_time))
        raise ValueError("Test case 20 failed by move")
    elif(elapsed_time > 0.450):
        print("Test Case 20 Failed by time: " + str(elapsed_time))
        raise ValueError("Test case 20 failed by time")
    else:
        print("Test case 20 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")
    
    data = {'game': {'id': '70bdfb03-8017-4540-9644-12e73e567ad5', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 17, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_pywWrMkYPvFThBXwkdRtFrPP', 'name': 'Shielded_Woodland', 'latency': '469', 'health': 93, 'body': [{'x': 4, 'y': 7}, {'x': 3, 'y': 7}, {'x': 3, 'y': 6}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}], 'head': {'x': 4, 'y': 7}, 'length': 5, 'shout': ''}, {'id': 'gs_wpDVp7VKhyFDvY6Mqk8rYP6c', 'name': 'Nessegrev-beta', 'latency': '281', 'health': 85, 'body': [{'x': 0, 'y': 5}, {'x': 1, 'y': 5}, {'x': 1, 'y': 4}, {'x': 1, 'y': 3}], 'head': {'x': 0, 'y': 5}, 'length': 4, 'shout': ''}, {'id': 'gs_DFD7cJMf33FrDrkXHtQm3yYS', 'name': 'Git Adder (2)', 'latency': '147', 'health': 87, 'body': [{'x': 6, 'y': 1}, {'x': 7, 'y': 1}, {'x': 7, 'y': 2}, {'x': 7, 'y': 3}], 'head': {'x': 6, 'y': 1}, 'length': 4, 'shout': ''}, {'id': 'gs_jvc8bJrHX7TvDrJfbyYjtFTF', 'name': 'Head Hunter', 'latency': '81', 'health': 96, 'body': [{'x': 5, 'y': 6}, {'x': 5, 'y': 5}, {'x': 6, 'y': 5}, {'x': 6, 'y': 6}, {'x': 7, 'y': 6}], 'head': {'x': 5, 'y': 6}, 'length': 5, 'shout': ''}], 'food': [{'x': 1, 'y': 8}, {'x': 9, 'y': 9}, {'x': 10, 'y': 6}], 'hazards': []}, 'you': {'id': 'gs_pywWrMkYPvFThBXwkdRtFrPP', 'name': 'Shielded_Woodland', 'latency': '469', 'health': 93, 'body': [{'x': 4, 'y': 7}, {'x': 3, 'y': 7}, {'x': 3, 'y': 6}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}], 'head': {'x': 4, 'y': 7}, 'length': 5, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'right'):
        print("Test Case 21 Failed surviving: " + str(elapsed_time))
        raise ValueError("Test case 21 failed by move")
    elif(elapsed_time > 0.450):
        print("Test Case 21 Failed by time: " + str(elapsed_time))
        raise ValueError("Test case 21 failed by time")
    else:
        print("Test case 21 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")

    data = {'game': {'id': '592256e2-abaa-4a7e-bcb9-5a044bb7da9a', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 115, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_qMXMMjpxjpCRvDYt6RX7rr7T', 'name': 'Git Adder (2)', 'latency': '83', 'health': 62, 'body': [{'x': 6, 'y': 5}, {'x': 6, 'y': 4}, {'x': 5, 'y': 4}, {'x': 5, 'y': 5}, {'x': 4, 'y': 5}, {'x': 3, 'y': 5}, {'x': 3, 'y': 6}, {'x': 3, 'y': 7}, {'x': 4, 'y': 7}], 'head': {'x': 6, 'y': 5}, 'length': 9, 'shout': ''}, {'id': 'gs_jTvRGT3vKvQ8cWYMx7YhTCrJ', 'name': 'Head Hunter', 'latency': '74', 'health': 52, 'body': [{'x': 7, 'y': 0}, {'x': 8, 'y': 0}, {'x': 8, 'y': 1}, {'x': 9, 'y': 1}, {'x': 9, 'y': 2}, {'x': 9, 'y': 3}, {'x': 9, 'y': 4}, {'x': 9, 'y': 5}], 'head': {'x': 7, 'y': 0}, 'length': 8, 'shout': ''}, {'id': 'gs_4btqSM6qWfHdwbTP9c4Gpyw4', 'name': 'Shielded_Woodland', 'latency': '262', 'health': 85, 'body': [{'x': 3, 'y': 4}, {'x': 3, 'y': 3}, {'x': 4, 'y': 3}, {'x': 4, 'y': 2}, {'x': 4, 'y': 1}], 'head': {'x': 3, 'y': 4}, 'length': 5, 'shout': ''}], 'food': [{'x': 10, 'y': 1}, {'x': 0, 'y': 9}, {'x': 9, 'y': 0}, {'x': 1, 'y': 1}, {'x': 3, 'y': 0}, {'x': 1, 'y': 3}], 'hazards': []}, 'you': {'id': 'gs_4btqSM6qWfHdwbTP9c4Gpyw4', 'name': 'Shielded_Woodland', 'latency': '262', 'health': 85, 'body': [{'x': 3, 'y': 4}, {'x': 3, 'y': 3}, {'x': 4, 'y': 3}, {'x': 4, 'y': 2}, {'x': 4, 'y': 1}], 'head': {'x': 3, 'y': 4}, 'length': 5, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'right'):
        print("Test Case 22 Failed surviving: " + str(elapsed_time))
        raise ValueError("Test case 22 failed by move")
    elif(elapsed_time > 0.450):
        print("Test Case 22 Failed by time: " + str(elapsed_time))
        raise ValueError("Test case 22 failed by time")
    else:
        print("Test case 22 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")

    #going down garuntees death if opponent plays right
    # need to check and see if space I have is smaller than body, and if I can not reach a tail
    data = {'game': {'id': '1e215d9c-4111-4f2a-8616-8460bd3a4138', 'ruleset': {'name': 'standard', 'version': 'v1.0.13'}, 'timeout': 500}, 'turn': 442, 'board': {'height': 11, 'width': 11, 'snakes': [{'id': 'gs_4YFXqhRJphK3Y7cvT7Rh8HTH', 'name': 'Shielded_Woodland', 'latency': '409', 'health': 88, 'body': [{'x': 9, 'y': 7}, {'x': 8, 'y': 7}, {'x': 8, 'y': 6}, {'x': 8, 'y': 5}, {'x': 8, 'y': 4}, {'x': 8, 'y': 3}, {'x': 8, 'y': 2}, {'x': 8, 'y': 1}, {'x': 8, 'y': 0}, {'x': 7, 'y': 0}, {'x': 6, 'y': 0}, {'x': 5, 'y': 0}, {'x': 5, 'y': 1}, {'x': 6, 'y': 1}, {'x': 7, 'y': 1}, {'x': 7, 'y': 2}, {'x': 7, 'y': 3}, {'x': 7, 'y': 4}, {'x': 7, 'y': 5}, {'x': 7, 'y': 6}, {'x': 7, 'y': 7}, {'x': 7, 'y': 8}, {'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 5, 'y': 7}, {'x': 5, 'y': 6}], 'head': {'x': 9, 'y': 7}, 'length': 26, 'shout': ''}, {'id': 'gs_Y8XcJPR4CX9bYvrccHhMYdbT', 'name': 'Git Adder (2)', 'latency': '79', 'health': 86, 'body': [{'x': 5, 'y': 5}, {'x': 5, 'y': 4}, {'x': 4, 'y': 4}, {'x': 4, 'y': 5}, {'x': 4, 'y': 6}, {'x': 3, 'y': 6}, {'x': 3, 'y': 5}, {'x': 3, 'y': 4}, {'x': 3, 'y': 3}, {'x': 3, 'y': 2}, {'x': 4, 'y': 2}, {'x': 4, 'y': 1}, {'x': 3, 'y': 1}, {'x': 2, 'y': 1}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 0, 'y': 2}, {'x': 0, 'y': 3}, {'x': 0, 'y': 4}, {'x': 0, 'y': 5}, {'x': 0, 'y': 6}, {'x': 0, 'y': 7}, {'x': 0, 'y': 8}, {'x': 0, 'y': 9}, {'x': 0, 'y': 10}, {'x': 1, 'y': 10}, {'x': 2, 'y': 10}, {'x': 3, 'y': 10}, {'x': 3, 'y': 9}, {'x': 3, 'y': 8}, {'x': 3, 'y': 7}, {'x': 4, 'y': 7}, {'x': 4, 'y': 8}, {'x': 4, 'y': 9}, {'x': 5, 'y': 9}, {'x': 6, 'y': 9}, {'x': 6, 'y': 10}, {'x': 7, 'y': 10}, {'x': 7, 'y': 9}], 'head': {'x': 5, 'y': 5}, 'length': 39, 'shout': ''}], 'food': [{'x': 9, 'y': 10}, {'x': 6, 'y': 7}], 'hazards': []}, 'you': {'id': 'gs_4YFXqhRJphK3Y7cvT7Rh8HTH', 'name': 'Shielded_Woodland', 'latency': '409', 'health': 88, 'body': [{'x': 9, 'y': 7}, {'x': 8, 'y': 7}, {'x': 8, 'y': 6}, {'x': 8, 'y': 5}, {'x': 8, 'y': 4}, {'x': 8, 'y': 3}, {'x': 8, 'y': 2}, {'x': 8, 'y': 1}, {'x': 8, 'y': 0}, {'x': 7, 'y': 0}, {'x': 6, 'y': 0}, {'x': 5, 'y': 0}, {'x': 5, 'y': 1}, {'x': 6, 'y': 1}, {'x': 7, 'y': 1}, {'x': 7, 'y': 2}, {'x': 7, 'y': 3}, {'x': 7, 'y': 4}, {'x': 7, 'y': 5}, {'x': 7, 'y': 6}, {'x': 7, 'y': 7}, {'x': 7, 'y': 8}, {'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 5, 'y': 7}, {'x': 5, 'y': 6}], 'head': {'x': 9, 'y': 7}, 'length': 26, 'shout': ''}}
    move = get_move(data)
    end = time.time()
    elapsed_time = end - start

    if (move == 'down'):
        print("Test Case 23 Failed surviving: " + str(elapsed_time))
        raise ValueError("Test case 23 failed by move")
    elif(elapsed_time > 0.450):
        print("Test Case 23 Failed by time: " + str(elapsed_time))
        raise ValueError("Test case 23 failed by time")
    else:
        print("Test case 23 passed with time: " + str(elapsed_time))
        tests_passed += 1
    start = time.time()
    print("---------------------------------")
    
    print("Tests passed: " + str(tests_passed))