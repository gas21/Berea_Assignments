# Description: 8 Queen Solver. The program generates all 92 solutions for the 8 Queen Problem.
# Author: Soe Win Han
# Attribution: None

from itertools import permutations


solutions = []
boards = [i for i in permutations('01234567', 8)]
for i in boards:
    stack = [(k, int(i[k])) for k in range(8)]
    if all([all((all([(s[0] + l, s[1] + l) not in stack for l in range(1, 8)])) for s in stack),
           all((all([(s[0] - l, s[1] + l) not in stack for l in range(1, 8)])) for s in stack),
            all((all([(s[0] - l, s[1] - l) not in stack for l in range(1, 8)])) for s in stack),
            all((all([(s[0] + l, s[1] + l) not in stack for l in range(1, 8)])) for s in stack)]):
        solutions.append(i)
print(solutions)
print(len(solutions))
