s=input()
a=list(map(int,input().split()))
t=[]
for i in range(len(a)):
  if i % 2 == 0:
    if a[i] % 2 !=0:
      t.append(a[i])
for i in t:
  print(i,end=" ")
      
