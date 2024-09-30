#day-3 code 1
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if X in range(2,13) and Y in range(1,X):
        sum=0
        sum=X*4+Y
        print(sum)