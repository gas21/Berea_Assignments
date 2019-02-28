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
    alpha, temp, digits = [], '', '0123456789'
    a, b, c = len(first), len(second), len(sum)
    for i in chain(first, second, sum):
        if i not in alpha:
            alpha.append(i)
    for i in permutations(digits, len(alpha)):
        for j in chain(first, second, sum):
            temp += i[alpha.index(j)]
        if int(temp[:a]) + int(temp[a:a+b]) == int(temp[a+b:]):
            if temp[:a][0] != '0' and temp[a:a+b][0] != '0' and temp[a+b:][0] != '0':
                print(str(alpha) + "\n" + str(i) + "\n" + temp[:a] + " + " + temp[a:a + b] + " = " + temp[a + b:])
        temp = ''


cryptarithm('send', 'more', 'money')
