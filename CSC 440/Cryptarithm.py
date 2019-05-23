# CSC 440 Design and Analysis of Algorithms
# Assignment Cryptarithm: Exhaustive Search
# Author: Soe Win Han
# Attribution: None
# Python 3.71

"""
Note: May take a long time depending on input and processing speed.
"""
from itertools import permutations
import time


def cryptarithm(first, second, sum):
    abc, temp, a, b, c = list(first + second + sum), '', len(first), len(second), len(sum)
    abc = list(dict.fromkeys(abc))
    for i in permutations('0123456789', len(abc)):
        for j in (first + second + sum):
            temp += i[abc.index(j)]
        if int(temp[:a]) + int(temp[a:a+b]) == int(temp[a+b:]):
            if temp[:a][0] != '0' and temp[a:a+b][0] != '0' and temp[a+b:][0] != '0':
                print(str(abc) + "\n" + str(i) + "\n" + temp[:a] + " + " + temp[a:a + b] + " = " + temp[a + b:])
        temp = ''


a = time.process_time()
cryptarithm('send', 'more', 'money')
print(time.process_time()-a)
