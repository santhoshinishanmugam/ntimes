n,t=map(input().split())
s=int(n)
g=int(t)
for i in range(s+1,g+1):
  if(i>1 and i<g):
    for n in range (2,i):
      if((i%n)==0):
        break
      else:
        print(i,end=" ")
       
          
         
             
