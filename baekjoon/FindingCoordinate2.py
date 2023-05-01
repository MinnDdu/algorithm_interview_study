import sys


N = int(sys.stdin.readline())
arr = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

for i in range(N-1):
    minimum = arr[i][1]
    for j in range(i+1, N):
        if arr[j][1] < minimum:
            minimum = arr[j][1]
            arr[i], arr[j] = arr[j], arr[i]
        elif arr[j][1] == minimum:
            if arr[j][0] < arr[i][0]:
                minimum = arr[j][1]
                arr[i], arr[j] = arr[j], arr[i]

for i in range(N):
    print(str(arr[i][0]) + " " + str(arr[i][1]))

