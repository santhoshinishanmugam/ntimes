begin=int(input())
if begin == 0 or begin == -1:
  print(1)
else:
  fact = 1
  for i in range(2, begin+1):
    fact *=i
  print(fact)
