s = input() 
a = len(s)
n = 0
for i in s:
  i = int(i)
  n += pow(i,1)
 if n == int(s):
  print("yes")
 else:
  print("no")
