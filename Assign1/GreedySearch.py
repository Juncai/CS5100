'''
Created on Jan 28, 2014
AI NAME: 3Ter
@author: juncai
'''

import time
import random


################################
#     Functions for console output bigin
################################

def ConsoleAgentTurn(state, counter_matrix):
    ''' 
        Compute the agent's next action and calculate the time consumption.
    '''
    start = time.clock()
    action = NextAction(state, counter_matrix)
    time_consume = time.clock() - start
    # display the time consuming
    print("Time Consuming: %.6f" % time_consume + "s")    
    # update the state
    if action != -1:
        state[action] = 1
    return time_consume

def ConsolePlayerTurn(state, counter_matrix):
    '''
        Receive the input from player. 
    '''
    action = PlayerInput()
    while action < 0 or action > 8:
        print("Please input valid x and y value!")
        action = PlayerInput()
    state[action] = -1
    start = time.clock()
    updatecountermatrix(counter_matrix, action, -1)    
    time_consume = time.clock() - start
    return time_consume

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
        print("The agent wins!")
    elif result == -1:
        print("Congratulation, you win!")
    elif result == 0:
        print("It's a draw!")
    print("The total time consumption is %.6f" % time_accumulator + "s")
        





################################
#     Functions for GUI output
################################



def AlgInit(self):
    '''
        Reserved function for more operation when game initializes
    '''
    self.counter_matrix = [[[0, 0], [0, 0], [0, 0]],
                      [[0, 0], [0, 0], [0, 0]], 
                      [[0, 0], [0, 0]]]


def PlayerAction(self, action):
    '''
        Reserved function for more operation when player takes an action
    '''
    # update the counter matrix using player's action 
    updatecountermatrix(self.counter_matrix, action, -1)



#########################
#   Greedy search algorithm
#########################

def NextAction(state, counter_matrix):
    ''' using counter_matrix and player's action to find the next action
        action is a integer standing for the action of the player
    '''
    # initiate the max_score and best_action
    max_score = -1
    
    for i in range(0, len(state)):
        current_score = 0
        if state[i] == 0:
            # calculate score
            if counter_matrix[0][i/3][0] == 2:
                current_score += 100
            elif counter_matrix[0][i/3][0] == 0:
                current_score += 2
                if counter_matrix[0][i/3][1] == 2:
                    current_score += 10
            if counter_matrix[1][i%3][0] == 2:
                current_score += 100
            elif counter_matrix[1][i%3][0] == 0:
                current_score += 2
                if counter_matrix[1][i%3][1] == 2:
                    current_score += 10

            if i == 0 or i == 4 or i == 8:
                if counter_matrix[2][0][0] == 2:
                    current_score += 100
                elif counter_matrix[2][0][0] == 0:
                    current_score += 2
                    if counter_matrix[2][0][1] == 2:
                        current_score += 10
            if i == 2 or i == 4 or i == 6:
                if counter_matrix[2][1][0] == 2:
                    current_score += 100
                elif counter_matrix[2][1][0] == 0:
                    current_score += 2
                    if counter_matrix[2][1][1] == 2:    # see if player takes 2 grids
                        current_score += 10
            if current_score > max_score:
                max_score = current_score
                best_action = i
    updatecountermatrix(counter_matrix, best_action, 1)
    return best_action

    
def updatecountermatrix(counter_matrix, action, turn):
    ''' using action and role to update the counter_matrix, check if the game is over at the same time
        -1 stands for tie, 0 stands for agent win, 1 stands for player win, 2 stands for not over
        @param action: an integer indicates which grid is taken
        @param turn: 1 or -1, 1 stands for agent, -1 stands for player
        
    '''
    # convert the turn to role (the index in the counter matrix)
    if turn == 1:
        role = 0
    else:
        role = 1
    # if no action can be taken, it's a tie
    if action == -1:
        return -1
    # update the horizontal counter
    counter_matrix[0][action/3][role] += 1
    # update the vertical counter
    counter_matrix[1][action%3][role] += 1
    # update the diagonal counter
    if action == 0 or action == 4 or action == 8:
        counter_matrix[2][0][role] += 1
    # update the counter-diagonal counter
    if action == 2 or action == 4 or action == 6:
        counter_matrix[2][1][role] += 1





def Utility(state):
    '''
        Test if the game is over. If it's over, return the utility. 
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

if __name__ == '__main__':
    state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter_matrix = [[[0, 0], [0, 0], [0, 0]],
                      [[0, 0], [0, 0], [0, 0]], 
                      [[0, 0], [0, 0]]]
    # initiate time consuming
    time_accumulator = 0
    
    PrintState(state)
    # randomly pick the one who goes first
    if random.randint(0, 9) >= 5:
        time_accumulator += ConsoleAgentTurn(state, counter_matrix)
        PrintState(state)
    # Continue the game until over
    while Utility(state) == 2:
        time_accumulator += ConsolePlayerTurn(state, counter_matrix)
        PrintState(state)
        if Utility(state) == 2:
            time_accumulator += ConsoleAgentTurn(state, counter_matrix)
            PrintState(state)
    PrintResult(state, time_accumulator)
