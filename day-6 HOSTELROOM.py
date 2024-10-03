T=int(input())
if T in range(1,4001):
    for i in range(T):
        N,X=map(int,(input().split()))
        if N in range(1,101) and X in range(0,101):
            A=list(map(int,input().split()))[:N]
            res=[]
            current_person=X
            max_person=X
            for i in range(N):
                current_person+=A[i]
                if current_person>max_person:
                    max_person=current_person
            res.append(max_person)
            for result in res:
              print(result)