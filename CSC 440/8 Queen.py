# Description: 8 Queen Solver. The program generates all 92 solutions for the 8 Queen Problem.
# Author: Soe Win Han
# Attribution: None
#####################################################################
import time
from itertools import permutations
a = time.process_time()
solutions = []
for i in permutations(range(8), 8):
    stack = {(k, i[k]) for k in range(8)}
    if all([True if k not in stack else False for k in [m for s in stack for l in range(1, 8) for m in [
            (s[0]+l, s[1]+l), (s[0]-l, s[1]+l), (s[0]-l, s[1]-l), (s[0]+l, s[1]+l)]]]):
        solutions.append(i)
print(str(solutions) + "\n" + str((len(solutions))))
print(time.process_time() - a)


