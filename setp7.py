h=input()
f=h[::2]
g=h[1::2]
s=''
for i,j in zip(f,g):
  s += (j + i)
print(s) 
  
