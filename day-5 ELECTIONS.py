T=int(input())
if T in range(500):
    for j in range (T):
        A,B,C=map(int,input().split())
        if A in range(102) and B in range(102) and C in range (102):
            if A+B+C==101:
                if A>50:
                    print("A")
                elif B>50:
                    print("B")
                elif C>50:
                    print("C")
                else:
                    print('NOTA')
            else:
                print('noumber of voter exceed more than 101')
        