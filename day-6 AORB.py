def maximum_min(x,y):
  P_A=500-X*2
  P_B=1000-(X+Y)*4
  max_pointAB=P_A+P_B
  P_B=1000-Y*4
  P_A=500-(X+Y)*2
  max_pointBA=P_A+P_B
  return max(max_pointAB,max_pointBA)
T=int(input())
if T in range(1,1001):
  for i in range(T):
    X,Y=map(int,input().split())
    if X in range(1,101) and Y in range(1,101):
      print(maximum_min(X,Y))