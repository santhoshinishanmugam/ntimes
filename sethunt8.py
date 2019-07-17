from itertools import permutations
s = input()
a = list(map(int,input().split()))
y = []
for i in permutations(a,3):
  if i[0] < i[1] < i[2]:
    if i[0] + i[1] == i[3]:
      y.append([str(j) for j in i])
for i in y:
  print(' '.join(i))
      
