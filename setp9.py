c,v=map(int,input().split())
p=[]
for j in range(c+1,v+1):
  if j>1:
    for i in range(2,j):
      if(j%v==0):
        break
      else:
        p.append(i)
  print(len(p)+1)      
