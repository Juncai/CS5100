'''
Created on Feb 14, 2014

@author: Jon
'''

def allowed_neighbors(current, allowed):
    '''
    Generate neighbor square of current position from a list of allowed square
    @param current: a tuple containing the coordinates of the current position of the agent
    @param allowed: a tuple list of safe squares
    @return: a tuple list of allowed neighbor square of the current position
    '''
    neighbors = []
    currentx = current[0]
    currenty = current[1]
    for i in range(-1,3):
        for j in range(-1,3):
            temp = (currentx + i, currenty + j)
            if allowed.count(temp) > 0:
                neighbors.append(temp)
    neighbors.remove(current)
    return neighbors

def mdistance(square, goal):
    """
    @return: Manhattan distance between given square and the goal
    """
    return abs(goal[0] - square[0]) + abs(goal[1] - square[1])

if __name__ == '__main__':
    current = (1, 1)
    allowed = [(1, 1), (1, 2)]
    neighbors = allowed_neighbors(current, allowed)
    print(neighbors)
    print(current)