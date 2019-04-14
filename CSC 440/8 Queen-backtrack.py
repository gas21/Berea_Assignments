# Description: 8 Queen Solver. The program generates all 92 solutions for the 8 Queen Problem.
# Author: Soe Win Han + Source
# Attribution: http://code.activestate.com/recipes/576647-eight-queens-six-lines/
#####################################################################

from itertools import permutations


solutions = []
boards = [i for i in permutations(range(8), 8)]
for i in boards:
    stack = [(k, int(i[k])) for k in range(8)]
    if all([True if k not in stack else False for k in [m for s in stack for l in range(1, 8) for m in [(s[0] + l, s[1] + l),
                (s[0] - l, s[1] + l), (s[0] - l, s[1] - l), (s[0] + l, s[1] + l)]]]):
        solutions.append(i)
print(solutions)
print(len(solutions))