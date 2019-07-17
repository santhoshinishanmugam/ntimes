s = input()
a = map(int,input().split())
t = map(int,input().split())
if t.issubset(a):
  print("YES")
else:
  print("NO")
  
