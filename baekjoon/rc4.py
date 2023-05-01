
s = []
k = []
key = [1, 2, 3, 4, 5]

for i in range(256):
    s[i] = i
    k[i] = key[i % 5]

for j in range(256):
    j = (j + s[i] )
