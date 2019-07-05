s=str(input(" "))
g=0
for i in range(0,len(s)):
  if(s[i]==" "):
    g=g+1
  elif((i+1)==len(s)):
    g=g+1
print(g)    
