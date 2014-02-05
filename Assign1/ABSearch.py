'''
Created on Jan 27, 2014
AI NAME: schizoider
@author: juncai


draw: 0
agent win: 1
player win: -1

'''
import copy
import time
import random




################################
#     Functions for console output bigin
################################

def ConsoleAgentTurn(state):
    ''' 
        Compute the agent's next action and calculate the time consumption.
    '''
    start = time.clock()
    action = NextAction(state, None)
    time_consume = time.clock() - start
    # display the time consuming
    print("Time Consuming: %.6f" % time_consume + "s")    
    # update the state
    if action != -1:
        state[action] = 1
    return time_consume

def ConsolePlayerTurn(state):
    '''
        Receive the input from player. 
    '''
    action = PlayerInput()
    while action < 0 or action > 8:
        print("Please input valid x and y value!")
        action = PlayerInput()
    state[action] = -1
    

def PlayerInput():
    raw_action = raw_input("Enter input 'x' <space> 'y': ")
    x = int(raw_action.split()[0])
    y = int(raw_action.split()[1])
    return x - 1 + (y -1) * 3 
    

def PrintState(state):
    state_display = []
    for i in state:
        if i == 1:
            state_display.append("O")
        elif i == -1:
            state_display.append("X")
        else:
            state_display.append(" ")
    print("---------------------------------")
    print("|       |   1   |   2   |   3   |")
    print("---------------------------------")
    print("|   1   |   " + state_display[0] + "   |   " + state_display[1] + "   |   " + state_display[2] + "   |")
    print("---------------------------------")
    print("|   2   |   " + state_display[3] + "   |   " + state_display[4] + "   |   " + state_display[5] + "   |")
    print("---------------------------------")
    print("|   3   |   " + state_display[6] + "   |   " + state_display[7] + "   |   " + state_display[8] + "   |")
    print("---------------------------------")

def PrintResult(state, time_accumulator):
    result = Utility(state) 
    if result == 1:
        print "The agent wins!"
    elif result == -1:
        print "Congratulation, you win!"
    elif result == 0:
        print "It's a draw!"
    print("The total time consumption is %.6f" % time_accumulator + "s")



################################
#     Functions for GUI output
################################


def AlgInit(self):
    '''
        Reserved function for more operation when game initializes
    '''
    pass

def PlayerAction(self, action):
    '''
        Reserved function for more operation when player takes an action
    '''
    pass

################################
#     The minimax algorithm with alpha-beta pruning algorithm
################################

def NextAction(state, counter_matrix):
    '''
        A minimax algorithm with Alpha-beta pruning, return the action
    '''
    return MaxValue(state, -2, 2)[1]

def MaxValue(state, a, b):
    utility = Utility(state)
    if utility != 2:
        return [utility, -1]
    v = -2
    for action in Action(state):
        v1 = MinValue(AgentResult(state, action), a, b)[0]
        if v1 > v:
            v = v1
            best_action = action
        if v >= b:
            return [v, best_action]
        a = max(a, v)
    return [v, best_action]

def MinValue(state, a, b):
    utility = Utility(state)
    if utility != 2:
        return [utility, -1]
    v = 2
    for action in Action(state):
        v1 = MaxValue(PlayerResult(state, action), a, b)[0]
        if v1 < v:
            v = v1
            best_action = action
        if v <= a:
            return [v, best_action]
        b = min(b, v)
    return [v, best_action]

def Utility(state):
    '''
        Calculate the utility of the state. Test if the game is over. 
        Return 2 if the game is not over; 1 if the agent wins; -1 if the player wins; 0 if it's a draw
        done!
    '''
    # check rows and columns
    for i in range(0, 3):
        # check rows
        if state[i*3] == state[i*3+1] and state[i*3+1] == state[i*3+2] and state[i*3] != 0:
            return state[i*3]
        # check columns
        if state[i] == state[i+3] and state[i+3] == state[i+6] and state[i] != 0:
            return state[i]
    # check diagonal
    if state[0] == state[4] and state[4] == state[8] and state[0] != 0:
        return state[0]
    if state[2] == state[4] and state[4] == state[6] and state[2] != 0:
        return state[2]
    for i in state:
        if i == 0:
            return 2
    return 0

def Action(state):
    '''
        return the valid action in the current state
        done!
    '''
    actions = []
    for i in range(0, len(state)):
        if state[i] == 0:
            actions.append(i)
    return actions

def AgentResult(state, action):
    '''
        return the state after the current action when agent take action
        done!
    '''
    next_state = copy.copy(state)
    next_state[action] = 1
    return next_state

def PlayerResult(state, action):
    '''
        return the state after the current action when player take action
        done!
    '''
    next_state = copy.copy(state)
    next_state[action] = -1
    return next_state



if __name__ == '__main__':
    state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # initiate time consuming
    time_accumulator = 0
    PrintState(state)
    # randomly pick the one who goes first
    if random.randint(0, 9) >= 5:
        time_accumulator += ConsoleAgentTurn(state)
        PrintState(state)
    # Continue the game until over
    while Utility(state) == 2:
        ConsolePlayerTurn(state)
        PrintState(state)
        if Utility(state) == 2:
            time_accumulator += ConsoleAgentTurn(state)
            PrintState(state)
    PrintResult(state, time_accumulator)
    