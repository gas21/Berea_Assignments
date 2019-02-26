# CSC 440 Design and Analysis of Algorithms
# Assignment Cryptarithm: Exhaustive Search
# Author: Soe Win Han
# Attribution: None
# Python 3.71

"""
Note: May take a long time depending on input and processing speed.
"""

from itertools import chain
from itertools import permutations


def cryptarithm(first, second, sum):
    alpha, solution, temp, digits = [], [], '', '0123456789'
    a, b, c = len(first), len(second), len(sum)
    for i in chain(first, second, sum):
        if i not in alpha:
            alpha.append(i)
    for i in permutations(digits, len(alpha)):
        for j in chain(first, second, sum):
            temp += i[alpha.index(j)]
        nfirst, nsecond, nsum = temp[:a], temp[a:a+b], temp[a+b:]
        if int(nfirst) + int(nsecond) == int(nsum):
            if nfirst[0] != '0' and nsecond[0] != '0' and nsum[0] != '0':
                solution.append(i)
        temp = ''
    print(alpha)
    print(solution)
    for i in solution:
        for j in chain(first, second, sum):
            temp += i[alpha.index(j)]
        nfirst, nsecond, nsum = temp[:a], temp[a:a + b], temp[a + b:]
        print(nfirst + " + " + nsecond + " = " + nsum)


cryptarithm('send', 'more', 'money')