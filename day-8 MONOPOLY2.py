def monopoly(P,Q,R,S):
    sum=0
    if P in range(1,101) and Q in range(1,101) and R in range(1,101) and S in range (1,101):
       if P>Q+R+S:
        print('YES')
       elif Q>P+R+S:
        print('YES')
       elif R>Q+P+S:
        print('YES')
       elif S>Q+R+P:
        print('YES')
       else:
        print('NO')
T=int(input())
if T in range (1,5001):
  for i in range(T):
    P,Q,R,S=map(int,(input().split()))
    res=monopoly(P,Q,R,S)
        