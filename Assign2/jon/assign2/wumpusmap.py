'''
Created on Feb 17, 2014

@author: Jon
'''

class WumpusMap(object):
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
        self._map_contents = [[[] for col in range(width)] for row in range(height)]
    
    def __str__(self):
        s = ''
        for row in self._map_contents:
            for col in row:
                s += '['
                for item in col:
                    s = s + item + ', '
                s += '] '
            s += '\n'
        return s
    
    def add_content(self, x, y,content):
        '''
        Add content in content list of square(x, y).
        '''
        self._map_contents[y-1][x-1].append(content)
        
    def get_content(self, x, y):
        '''
        Get content in square(x, y) 
        :return: the content list in square(x, y) 
        '''
        return self._map_contents[y-1][x-1]
    
            
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
        result = []
        content = self.get_content(x, y)
        if 'W' in content or 'P' in content:
            result.append('Over')
        elif 'G' in content:
            content.remove('G')
            result.append('Gold')
        elif 'GO' in content:
            result.append('Goal')
        return result
    
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
                    if 'W' in self.get_content(_x, y):
                        self.get_content(_x, y).remove('W')
                        for nx, ny in self.neighbor(_x, y):
                            self.get_content(nx, ny).remove('S')
                        return 'Hit'
            elif x < tx:
                for _x in range(x+1, self._width):
                    if 'W' in self.get_content(_x, y):
                        self.get_content(_x, y).remove('W')
                        for nx, ny in self.neighbor(_x, y):
                            self.get_content(nx, ny).remove('S')
                        return 'Hit'
        if y != ty:
            if y > ty:
                for _y in range(0, y):
                    if 'W' in self.get_content(x, _y):
                        self.get_content(x, _y).remove('W')
                        for nx, ny in self.neighbor(x, _y):
                            self.get_content(nx, ny).remove('S')
                        return 'Hit'
            elif y < ty:
                for _y in range(y+1, self._height):
                    if 'W' in self.get_content(x, _y):
                        self.get_content(x, _y).remove('W')
                        for nx, ny in self.neighbor(x, _y):
                            self.get_content(nx, ny).remove('S')
                        return 'Hit'
        return 'Miss'
        
        