s1,s2=map(int,input().spplit())
s3=0
for i in range(s1,s2+1):
  if i>1:
    for x in range(2,i):
      if x%2==0:
        break
  else:
    s3+=1
print(s3)    
  
          
