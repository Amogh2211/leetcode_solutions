########### INPUT ###############

import fileinput
import sys
q = []

for line in fileinput.input(files ='input.txt'):
    q.append(line.split(','))
test_list = list(map(int, q[0]))

sys.stdout= open('output.txt', 'w')

#################################

#           Solution

#################################

def contains_duplicate(nums):
    a = set()
    for i in nums:
        if i in a:
            return True
        a.add(i)
    return False

print(contains_duplicate(test_list))

