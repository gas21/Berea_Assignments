# Description: 8 Queen Solver. The program generates all 92 solutions for the 8 Queen Problem.
# Author: Soe Win Han + Source
# Attribution: http://code.activestate.com/recipes/576647-eight-queens-six-lines/
#####################################################################
from itertools import permutations
import time

a = time.process_time()
board = range(8)
solutions = []
for j in permutations(board):
    if (8 == len(set(j[i]+i for i in board))
          == len(set(j[i]-i for i in board))):
        solutions.append(j)
print(solutions)
print(time.process_time() - a)
