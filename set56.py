l=input()
g,h=0,0
for c in l:
  if c.isalpha():
    g +=1
  if c.isdigit():
    g +=1
if g and h:
  print("Yes")
else:
  print("No")
    
