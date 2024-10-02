T=int(input())
if T in range(1,4001):
    for i in range(T):
        N=int(input())
        if N>=1 and N<=10**5:
            A=list(map(int,input().split()))[:N]
            freq={}
            for num in A:
                if num in freq:
                    freq[num]+=1
                else:
                    freq[num]=1
            max_freq=max(freq.values())
            min_operation=N-max_freq
            print(min_operation)
                