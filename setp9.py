inp1,inp2=map(int,input().split())
count=0
for n in range(inp1,inp2+1):
  if(n > 1):
    for x in range(2,n):
      if((n%x)==0):
        break
      else:
        count=count+1
print(count)        
