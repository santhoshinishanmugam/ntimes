def san(t,m):
  if(len(t)==len(m)):
    return("yes")
  else:
    return("no")
  t,m=map(str,input().split())
  print(san(t,m))


