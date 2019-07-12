from itertools import combinations
S,k=map(int,input().split())
d=len(str(S))
lst=list(combinations(str(S),d-k))
lst=sorted(lst)
print(*lst[0],sep='')
         
