'''
Created on Feb 17, 2014

@author: Jon
'''
from jon.assign2.wumpusmap import WumpusMap

INPUT_FILE='userlogin.txt'
PROVER9_PATH='F:\\Program Files (x86)\\Prover9-Mace4\\bin-win32\\prover9.exe'
ASSUMPTION=[]

def agent(filename):
    """
    
    """
    (wumpusmap, agent_location, goal) = buildmap(filename)
#     print(mdistance((4,4), goal))
    save_square = [agent_location, goal]
    
    

def buildmap(filename):
    """ Open and read the input file, return a dict where the key is userID,
        the value is the login times.
    """
        
    fptr = open(filename, 'rU')
     
    for line in fptr:
        mid_index = (len(line) - 1) / 2
        if 'M' in line:
            width = int(line[1:mid_index+1], 10)
            height = int(line[mid_index+1:], 10)
            wumpusmap = WumpusMap(width, height)
            break
    for line in fptr:
        if 'A' in line:
            x = int(line[1:mid_index+1], 10)
            y = int(line[mid_index+1:], 10)
            wumpusmap.add_content(x, y, 'A')
            agent_location = (x, y)
        elif 'B' in line:
            x = int(line[1:mid_index+1], 10)
            y = int(line[mid_index+1:], 10)
            wumpusmap.add_content(x, y, 'B')
        elif 'P' in line:
            x = int(line[1:mid_index+1], 10)
            y = int(line[mid_index+1:], 10)
            wumpusmap.add_content(x, y, 'P')
        elif 'S' in line:
            x = int(line[1:mid_index+1], 10)
            y = int(line[mid_index+1:], 10)
            wumpusmap.add_content(x, y, 'S')
        elif 'W' in line:
            x = int(line[1:mid_index+1], 10)
            y = int(line[mid_index+1:], 10)
            wumpusmap.add_content(x, y, 'W')
        elif 'GO' in line: #special index!
            x = int(line[2:mid_index+2], 10)
            y = int(line[mid_index+2:], 10)
            wumpusmap.add_content(x, y, 'GO')
            goal = (x, y)
        elif 'G' in line:
            x = int(line[1:mid_index+1], 10)
            y = int(line[mid_index+1:], 10)
            wumpusmap.add_content(x, y, 'G')
    fptr.close()
    return (wumpusmap, agent_location, goal)

def mdistance(square, goal):
    """
    Return Manhattan distance between given square and the goal
    """
    return abs(goal[0] - square[0]) + abs(goal[1] - square[1])

def initassumption():
    s = 'all x all y all a all b adjacent((x, y), (a,b)) <->'
    s += '((x=a) | (y=b)) & ((x=a) | (x=a+1) | (x=a+(-1))) & '
    s += '((y=b+1) | (y=b+(-1)) | (y=b)) & '
    s += '((y=b+1) | (y=b+(-1)) | (x=a+1) | (x=a+(-1))).'
    ASSUMPTION.append(s)
    











if __name__ == '__main__':
    agent('D:\Dropbox\CS5100\Assignments\Assign2\code\wumpus_world.txt')