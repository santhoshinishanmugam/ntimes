from itertools import combinations
s,k=map(int,input().split())
d=len(str(N))
lst=list(combinations(str(N),n-k))
lst=sorted(lst)
print(*lst[0],sep='')
         
