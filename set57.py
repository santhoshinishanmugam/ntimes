count=0
s,a = map(int,input().split())
l=list(map(int,input().split()))
for i in range(len(l)):
  if (l[i]==a):
    count+=1
print(count)    

