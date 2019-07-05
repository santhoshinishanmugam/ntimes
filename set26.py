sa = int(input())
t = list(map(int,input().split()))
t.sort()
for i in range(sa):
  print(t[i],end=" ")
