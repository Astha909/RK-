def water_filling(B1,B2,B3):
    if B1==1 and B2==1 and B3==1:
        print('Not now')
    elif B1==1 and B2==1 and B3==0:
        print('Not now')
    elif B1==0 and B2==1 and B3==1:
        print('Not now')    
    elif B1==1 and B2==1 and B3==0:
        print('Not now')
    elif B1==1 and B2==0 and B3==1:
        print('Not now')  
    else:
        print('water filling time')      
T=int(input())
if T in range(1,1001):
    for i in range(T):
        B1,B2,B3= map(int,input().split())
        if B1 in range(2) and B2 in range(2) and B3 in range(2):
             water_filling(B1,B2,B3)