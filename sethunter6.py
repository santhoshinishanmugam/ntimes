s=int(input())
a=list(map(int,input().split()))
flag=0
for i in a:
  if(a.count(i)>1):
    print(i)
    flag=1
    break
if(flag==0):
  print("unique")
