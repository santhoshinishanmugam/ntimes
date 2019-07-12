def l(str1,str2):
  if(str1 in str2):
    return str1
  else:
    return l(str[0:len(str1)-1],str2)
s=int(input())
m=[]
for_in range(0,s):
  m.append(input())
m.sort()
print(l(m[0],m[s-1]))
    
    
