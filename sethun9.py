from itertools import permutations
s = input()
a = list(map(int,input().split()))
t = 0
h = 10000
for i in permutations(a,2):
  if sum(i) == 0:
    t = i
    break
  elif 0-sum(i) < h:
    h = 0-sum(i)
    t = i
print(t[1], t[0])    
    

