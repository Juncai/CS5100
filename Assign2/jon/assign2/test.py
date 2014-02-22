'''
Created on Feb 14, 2014

@author: Jon
'''
from prover9 import Prover9



class test1(object):
    def __init__(self,a=0):
        self.a = a
    
    def setA(self,a):
        self.a = a


if __name__ == '__main__':
#     filename = 'F:\\Program Files (x86)\\Prover9-Mace4\\bin-win32\\prover9.exe'
#     prover = Prover9()
#     prover.config_prover9(filename, True)
#     assumptions = []
#     assumptions.append('mother(Liz,Charley).')
#     assumptions.append('father(Charley,Billy).')
#     assumptions.append('-mother(x,y) | parent(x,y).')
#     assumptions.append('-father(x,y) | parent(x,y).')
#     assumptions.append('-parent(x,y) | ancestor(x,y).')
#     assumptions.append('-parent(x,y) | -ancestor(y,z) | ancestor(x,z).')
#     
#     goal = 'ancestor(Liz, Billy).'
#     
#     returncode, stdout = prover._prove(goal, assumptions, False)
#     
#     print(returncode)
#     a =  [[0 for col in range(5)] for row in range(3)]
#     a[1][2] = 2
#     for a in range(1,3):
#         print(a)
#     line = 'M45'
# #     print(line[2:] + 1)
#     print(int(line[1:2], 10))
# #     dict = {(1, 'one'), (2, 'two')}
#     dict = [[]]
#     print(dict[0])
#     dict[0].append('one')
#     print(dict[0][0])
#     for i in range(1, 10):
#         if i == 4:
#             break
#         print(i)
#     a = [(1,2), (2,1)]
#     print(a[0][1])
#     b = test1(1)
#     print(b.a)
#     b.a = 10
#     print(b.a)
#     b.setA(100)
#     print(b.a)
    a = []
    for i in range(1,10):
        a.append(i)
    for i in range(1,10):
        print(a.pop())
    
    