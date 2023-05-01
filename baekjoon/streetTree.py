import sys
import math

N = int(sys.stdin.readline())
trees = []
for i in range(N):
    trees.append(int(sys.stdin.readline()))
    
def minimum():
    if len(trees) == 0 or len(trees) == 1:
        return len(trees)

    minimumGap = math.inf

    for i in range(1, len(trees)):
        if trees[i] - trees[i - 1] < minimumGap:
            minimumGap = trees[i] - trees[i-1]

    expectation = []
    goToAnswer = True
    for i in range(minimumGap, 0, -1):
        for j in range(trees[0], trees[-1] + 1, i):
            expectation.append(j)
        for k in trees:
            if k not in expectation:
                expectation = []
                goToAnswer = False
                break
            else:
                goToAnswer = True
        if goToAnswer:
            return len(expectation) - len(trees)

print(minimum())