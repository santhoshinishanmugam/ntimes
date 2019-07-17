s = input()
a = set(map(int,input().split()))
t = set(map(int,input().split()))
if t.issubset(a):
  print("YES")
else:
  print("NO")
  
