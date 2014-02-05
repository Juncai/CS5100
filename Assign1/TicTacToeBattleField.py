'''
Created on Jan 28, 2014

A Tic Tac Toe battle field for AIs to rock each other!



Global variables you need for your algorithm

Required Functions:

AlgInit(Frame) return None: Extra initialization operations need to be done at the very beginning.

NextAction(state) return action: state is a 9-element integer list that stands for the game board, 0 for empty, 1 for agent, -1 for player
                                action is an integer indicating the index in the state list. Do not make change to the state list.

PlayerAction(Frame, action) return None: Frame is the GUI object that stores some global variables for the algorithm, action is the opponent's
                                action in terms of the index of the state list. You can make a change to some global variables according to 
                                the opponent's move.

@author: juncai
'''

import  wx
import random
import time

# AI 1

from GreedySearch import NextAction as NextAction1

from GreedySearch import Utility as Utility1

from GreedySearch import PlayerAction as PlayerAction1

from GreedySearch import AlgInit as AlgInit1

# AI 2

from ABSearch import NextAction as NextAction2

from ABSearch import Utility as Utility2

from ABSearch import PlayerAction as PlayerAction2

from ABSearch import AlgInit as AlgInit2



#---------------------------------------------------------------------------

class MyFrame(wx.Frame):
    
    state = []
    # create a list to store the buttons, then we can access it easily
    buttonlist = []
    textlist = []
    game_over = False;
    # for greedy algorithm use
    counter_matrix = []
    
    # record time consuming
    time_accumulator1 = 0
    time_consume11 = 0
    time_consume12 = 0
    time_accumulator2 = 0
    time_consume21 = 0
    time_consume22 = 0

    def __init__(
            self, parent, ID, title, pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE
            ):

        wx.Frame.__init__(self, parent, ID, title, pos, size, style)
        self.InitUI()
        self.InitState()

    def InitUI(self):
        ''' Initialize the game UI, create 9 buttons to represent the game board, 
            Menu bar function: restart the game, 
            
        
        '''
        panel = wx.Panel(self, -1)
        # use sizer to arrange the buttons
        sizer = wx.FlexGridSizer(cols=3, hgap=1, vgap=1)
        #sizer = wx.GridSizer(3, 3)
        # create 9 buttons to represent the game board
        for i in range (1, 10):
#             b = wx.BitmapButton(self, i, pic)
            b = wx.Button(self, i, '', size=(50, 50))
            self.buttonlist.append(b)
            # position attribute to indicate the position of the button
            b.pos = i-1
            sizer.Add(b)
        # set the sizer
        self.SetSizer(sizer)
        
        b = wx.Button(self, wx.ID_ANY, 'Restart Game', (20, 200))
        self.Bind(wx.EVT_BUTTON, self.RestartGame, b)
        
        st = wx.StaticText(self, -1, "", (140, 210))
        self.textlist.append(st)
        
        st = wx.StaticText(self, -1, "AI1 Time Consuming: ", (140, 230))
        self.textlist.append(st)
        
        st = wx.StaticText(self, -1, "AI2 Time Consuming: ", (140, 250))
        self.textlist.append(st)
        
        self.Show()

    def InitState(self):
        ''' initialize the state
        
        '''
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # initialize time consuming
        self.time_accumulator1 = 0
        self.time_consume11 = 0
        self.time_consume12 = 0
        self.time_accumulator2 = 0
        self.time_consume21 = 0
        self.time_consume22 = 0
        AlgInit1(self)
        AlgInit2(self)
        # diagonal counter, diagonal_x_counter[0] stands for diagonal, diagonal_x_counter[0] stands for counter-diagonal 
        # counter_matrix: [0][:][:] are horizontal counters, [1] [:][:] are vertical counters, [2] [:][:] are diagonal counters;
        #                 [:][:][0] are agent counters, [:][:][1] are player counters
        
        # randomly pick the one who goes first
        if random.randint(0, 9) >= 5:
            while not self.game_over:
                AgentTurn(self)
                CheckState(self)
                if not self.game_over:
                    PlayerTurn(self)
                    CheckState(self)
            
        else:
            while not self.game_over:
                PlayerTurn(self)
                CheckState(self)
                if not self.game_over:
                    AgentTurn(self)
                    CheckState(self)
        GameResult(self, Utility1(self.state))
        
    def RestartGame(self, event):        
        # initialize the button label
        for i in range(0, len(self.buttonlist)):
            self.buttonlist[i].SetLabel('')
        self.game_over = False
        self.InitState()
        
                
def CheckState(self):
    if Utility1(self.state) != 2:
        self.game_over = True
    


def AgentTurn(self):
    '''
        Movement made by agent
    '''
    # set turn to agent
    self.textlist[0].SetLabel("AI1's Turn")
    start = time.clock()    
    action = NextAction1(self.state, self.counter_matrix)
    self.time_consume11 = time.clock() - start
    self.time_accumulator1 += self.time_consume11
    # display the time consuming
    self.textlist[1].SetLabel("AI1 Time Consuming: "+ str(self.time_consume11 + self.time_consume12))   
    # update the state
    if action >= 0 and action < 9 and self.state[action] == 0:
        self.state[action] = 1
        # update the button which is taken by the agent!
        self.buttonlist[action].SetLabel('O')
    else:
        dlg = wx.MessageDialog(self, 'Illegal action!', 'WARNING', wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    start = time.clock()    
    PlayerAction2(self, action)
    self.time_consume22 = time.clock() - start
    self.time_accumulator2 += self.time_consume22
        
def PlayerTurn(self):
    '''
        Movement made by player
        @param self: The GUI frame
        @param button: The button player click. Set None if the player movement is needed
    '''
    # set turn to agent
    self.textlist[0].SetLabel("AI2's Turn")
    neg_state = []
    # convert the state to adapt the algorithm
    for i in self.state:
        neg_state.append(-i)
    start = time.clock()
    action = NextAction2(neg_state, self.counter_matrix)
    self.time_consume21 = time.clock() - start
    self.time_accumulator2 += self.time_consume21
    # display the time consuming
    self.textlist[2].SetLabel("AI2 Time Consuming: "+ str(self.time_consume21 + self.time_consume22))   
    # update the state
    if action >= 0 and action < 9 and self.state[action] == 0:
        self.state[action] = -1
        # update the button which is taken by the agent!
        self.buttonlist[action].SetLabel('X')
    else:
        dlg = wx.MessageDialog(self, 'Illegal action!', 'WARNING', wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    start = time.clock()
    PlayerAction1(self, action)
    self.time_consume12 = time.clock() - start
    self.time_accumulator1 += self.time_consume12
    
def GameResult(self, result):
    '''
        Mark the game as over and display the result in a dialog
    '''
    # set message information
    if result == 1:
        message = "AI1 wins!"
        label = 'AI1 WIN'
    elif result == 0:
        message = "It's a draw!"
        label = 'DRAW'
    elif result == -1:
        message = "AI2 wins!"
        label = 'AI2 WIN'
    
    self.textlist[0].SetLabel(message)
    self.textlist[1].SetLabel("AI1 Total Time Consuming: "+ str(self.time_accumulator1))   
    self.textlist[2].SetLabel("AI2 Total Time Consuming: "+ str(self.time_accumulator2))   
#     dlg = wx.MessageDialog(self, message, label, wx.OK | wx.ICON_INFORMATION)
#     dlg.ShowModal()
#     dlg.Destroy()


if __name__ == '__main__':
    app = wx.App(False)
    MyFrame(None, -1, "Tic Tac Toe", size=(400, 300),
                  style = wx.DEFAULT_FRAME_STYLE)
    app.MainLoop()
    