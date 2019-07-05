u=input()
special=0
for i in range(len(u)):
  if(u[i].isalpha()):
    continue
  elif(u(i).isdigit()):
    continue
  else:
    special=special+1
print(special) 
