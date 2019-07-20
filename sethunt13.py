s = [i for i in input()]
a = s[::-1]
while lens(s) > 1:
  if s.pop(0)!= s.pop():
    print('NO')
    break
  else:
    print('YES')
  
