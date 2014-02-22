'''
Created on Feb 16, 2014

@author: Jon


pseudocode of A* search
    A*-GRAPH-SEARCH(current,goals,allowed)
    input: current, current position of the agent
            goals, a list of goal squares
            allowed, a list of save squares to go to
            
'''
from prover9 import Prover9

def a_star_batch(current,goals,allowed):
    '''
    @param current: current position of the agent
    @param goals: a list of goal squares
    @param allowed: a list of save squares to go to
    @return: the nearest goal square and a plan to get to the goal square with shortest path
    '''
    nearest_goal = (float("inf"),None)
    for goal in goals:
        distance,plan = a_star(current,goal,allowed)
        if distance < nearest_goal[0]:
            nearest_goal = goal
            shortest_path = (distance,plan)
    return (nearest_goal, shortest_path)

def a_star(current,goal,allowed):
    '''
    @param current: current position of the agent
    @param goal: goal square of the path
    @param allowed: a list of save squares to go to
    @return: a plan to get to the goal square
    '''
    nodes = {}
    for square in allowed:
        nodes[square] = node(mdistance(square,goal));
    nodes[current].g = 0
    open = []
    plan = []
    f = nodes[current].g + nodes[current].h
    heappush(open,(f, current))
    while len(open) > 0:
        p = heappop(open)
        neighbors = allowed_neighbors(p,allowed)
        for square in neighbors:
            g = nodes[p].g + 1
            h = mdistance(square,goal)
            f_new = g + h
            if square == goal:
                nodes[goal].parent = p
                plan.append(goal)
                node_in_path = nodes[goal]
                while node_in_path.parent != None:
                    plan.append(node_in_path.parent)
                    node_in_path = nodes[node_in_path.parent]
                return (f_new, plan)
            f_old = nodes[square].g + nodes[square].h
            if f_new < f_old:
                nodes[square].g = g
                nodes[square].parent = p
                if open.count((f_old,square)) > 0:
                    open.remove((f_old,square))
                heappush(open,(f_new, square))
    return(-1,plan)


class node(object):
    def __init__(self,h=float("inf"),g=float("inf"),parent=None):
        '''
        
        '''
        self.g = g
        self.h = h
        self.parent = parent


    