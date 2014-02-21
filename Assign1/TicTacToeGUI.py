'''
Created on Jan 28, 2014

@author: juncai
'''

import  wx
import random
import time
# from ABSearch import NextAction, Utility, PlayerAction, AlgInit
from GreedySearch import NextAction, Utility, PlayerAction, AlgInit
#---------------------------------------------------------------------------

class MyFrame(wx.Frame):
    
    state = []
    # create a list to store the buttons, then we can access it easily!!!!!!
    buttonlist = []
    textlist = []
    game_over = False;
    # for greedy algorithm use
    counter_matrix = []
    
    # record time consuming
    time_accumulator = 0
    time_consume1 = 0
    time_consume2 = 0

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
            self.Bind(wx.EVT_BUTTON, self.OnClick, b)
            sizer.Add(b)
        # set the sizer
        self.SetSizer(sizer)
        
        b = wx.Button(self, wx.ID_ANY, 'Restart Game', (20, 200))
        self.Bind(wx.EVT_BUTTON, self.RestartGame, b)
        
        st = wx.StaticText(self, -1, "", (140, 210))
        self.textlist.append(st)
        
        st = wx.StaticText(self, -1, "Time Consuming: ", (140, 250))
        self.textlist.append(st)
        
        self.Show()

    def InitState(self):
        ''' initialize the state
        
        '''
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # initiate time consuming
        self.time_accumulator = 0
        self.time_consume1 = 0
        self.time_consume2 = 0
        AlgInit(self)
        # diagonal counter, diagonal_x_counter[0] stands for diagonal, diagonal_x_counter[0] stands for counter-diagonal 
        # counter_matrix: [0][:][:] are horizontal counters, [1] [:][:] are vertical counters, [2] [:][:] are diagonal counters;
        #                 [:][:][0] are agent counters, [:][:][1] are player counters
        
        # randomly pick the one who goes first
        if random.randint(0, 9) >= 5:
            AgentTurn(self)
            PlayerTurn(self, None)
        else:
            PlayerTurn(self, None)
        
    def RestartGame(self, event):        
        # initialize the button label
        for i in range(0, len(self.buttonlist)):
            self.buttonlist[i].SetLabel('')
        self.InitState()
        self.game_over = False
        
        # add restart function!!!!!!!!!!#############################################################
    def OnClick(self, event):
        b = event.GetEventObject()
        if b.GetLabel() == '' and not self.game_over:
            PlayerTurn(self, b)
            # check if the game is over, 2 as continuing
            current_result = Utility(self.state)
            if current_result == 2:
                # agent's move
                AgentTurn(self)
                # check if the game is over
                current_result = Utility(self.state)
                if current_result == 2: 
                    PlayerTurn(self, None)
                else:
                    GameResult(self, current_result)
            else:
                GameResult(self, current_result)
                

def AgentTurn(self):
    '''
        Movement made by agent
    '''
    # set turn to agent
    self.textlist[0].SetLabel("Agent's Turn")
    start = time.clock()
    action = NextAction(self.state, self.counter_matrix)
    self.time_consume1 = time.clock() - start
    self.time_accumulator += self.time_consume1
    # display the time consuming
    self.textlist[1].SetLabel("Time Consuming: %.6f" % (self.time_consume1 + self.time_consume2))    
    # update the state
    if action != -1:
        self.state[action] = 1
        # update the button which is taken by the agent!
        self.buttonlist[action].SetLabel('O')
        
def PlayerTurn(self, button):
    '''
        Movement made by player
        @param self: The GUI frame
        @param button: The button player click. Set None if the player movement is needed
    '''
    if button != None:
        button.SetLabel('X')
        self.state[button.pos] = -1
        start = time.clock()
        PlayerAction(self, button.pos)
        self.time_consume2 = time.clock() - start
        self.time_accumulator += self.time_consume2
    else:
        # set turn back to player
        self.textlist[0].SetLabel("Player's Turn")
    
def GameResult(self, result):
    '''
        Mark the game as over and display the result in a dialog
    '''
    # mark the game as over
    self.game_over = True
    # set message information
    if result == 1:
        message = "Sorry, you lose!"
        label = 'LOSE'
    elif result == 0:
        message = "It's a draw!"
        label = 'DRAW'
    elif result == -1:
        message = "Congratulations, you win!"
        label = 'WIN'
         
    self.textlist[1].SetLabel("Total Time Consuming: %.6f" % self.time_accumulator)
    dlg = wx.MessageDialog(self, message, label, wx.OK | wx.ICON_INFORMATION)
    dlg.ShowModal()
    dlg.Destroy()


if __name__ == '__main__':
    app = wx.App(False)
    MyFrame(None, -1, "Tic Tac Toe", size=(350, 300),
                  style = wx.DEFAULT_FRAME_STYLE)
    app.MainLoop()
    