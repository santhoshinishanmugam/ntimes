e=input()
f=e[::2]
g=e[1::2]
s=''
for i,j in zip(f,g):
  s += (j + i)
print(s) 
  
