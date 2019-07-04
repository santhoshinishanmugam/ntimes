m = list(map(int, input().split()))
t = []
for i in range(m[0], m[-1]):
  r = str(i)
  l = len(r)
  c = 0
  for j in r:
    j = int(j)
    c += pow(j, l)
    if c == i:
      r.append(i)
for i in r:
  print(i, end=" ")
