strr1,strr2=input().split()
length=len(strr1) if len(strr1)<len(strr2) else len(strr2)
diff=abs(len(strr1)-len(strr2))
counts=diff
for i in range(length):
  if(len(strr2)==1 and strr2[i] in strr1):
    break
  if(strr1[i]!=strr2[i]):
    counts+=1
print(counts)    

