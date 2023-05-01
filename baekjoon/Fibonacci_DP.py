#Baekjoon 2474
import sys

N = sys.stdin.readline()
lst = []

for i in range(int(N)+1):
    lst.append(0)

for i in range(int(N)+1):
    if i == 0:
        lst[i] = 0
    elif i == 1:
        lst[i] = 1
    else:
        lst[i] = lst[i-1] + lst[i-2]

print(lst[int(N)])