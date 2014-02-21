'''
Created on Feb 17, 2014

@author: Jon
'''
from jon.assign2.wumpusmap import WumpusMap

class CreateWumpusMap(WumpusMap):
    '''
    Map data model for store map data and return content or percepts of
    a given square.
    '''
    _map_contents = None
    _height = None
    _width = None

    def __init__(self, width, height):
        '''
        Constructor
        '''
        self._width = width
        self._height = height
        self._map_contents = [['E' for col in range(width)] for row in range(height)]
        
    def set_content(self, x, y,content):
        '''
        Set content in square(x, y).
        '''
        self._map_contents[y-1][x-1] = content
        
    def get_content(self, x, y):
        '''
        Get content in square(x, y) 
        :return: the content in square(x, y) 
        '''
        return self._map_contents[y-1][x-1]
    
    def get_percept(self, x, y):
        '''
        Get percept in square(x, y)
        :return: A tuple where the first element is whether there is a Stench,
        the second element is whether there is a Breeze
        '''
        stench = False
        breeze = False
        for _x, _y in self.get_neighbor(x, y):
            if self.get_content(_x, _y) == 'W': stench = True
            if self.get_content(_x, _y) == 'P': breeze = True
        
        return (stench, breeze)
        
    def get_neighbor(self, x, y):
        '''
        Get neighbor squares of square (x, y) (include itself)
        :return: A list of tuples contain coordinate of the neighbor squares
        '''
        neighbors = []
        for _x in range(x-1, x+1):
            if _x <= self._width and _x > 0:
                neighbors.append((_x, y))
        for _y in range(y-1, y+1):
            if _y <= self._height and _y > 0:
                neighbors.append((x, _y))
        return neighbors
        
    def move(self, x, y):
        '''
        Move to the square(x, y), return result of this move and make essential 
        update to the map content.
        :return: A string indicates the result of this move
        '''
        content = self.get_content(x, y)
        if content == 'W' or content == 'P':
            return 'Over'
        elif content == 'G':
            self.set_content(x, y, 'A')
            return 'Gold'
        elif content == 'GO':
            self.set_content(x, y, 'A')
            return 'Goal'
        elif content == 'E':
            self.set_content(x, y, 'A')
            return 'None'
            
    def shoot(self, x, y, tx, ty):
        '''
        Shooting an arrow at square(x, y) and aim at square(tx, ty), return the 
        result
        :return: A stirng indicates the result of this shoot
        '''
        if (x != tx and y != ty) or (x == tx and y == ty):
            return 'Invalid'
        if x != tx:
            if x > tx:
                for _x in range(0, x):
                    if self.get_content(_x, y) == 'W':
                        self.set_content(_x, y, 'E')
                        return 'Hit'
            elif x < tx:
                for _x in range(x+1, self._width):
                    if self.get_content(_x, y) == 'W':
                        self.set_content(_x, y, 'E')
                        return 'Hit'
        if y != ty:
            if y > ty:
                for _y in range(0, y):
                    if self.get_content(x, _y) == 'W':
                        self.set_content(x, _y, 'E')
                        return 'Hit'
            elif y < ty:
                for _y in range(y+1, self._height):
                    if self.get_content(x, _y) == 'W':
                        self.set_content(x, _y, 'E')
                        return 'Hit'
        return 'Miss'
        
        