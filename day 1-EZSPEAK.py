#programe to check whether the letter is easy to pronounce or not 
T=int(input())
vowel={'a','e','i','o','u'}
for i in range(0,T):
    N=int(input())
    S=input()
    count=0
    is_easy=True
    for j in S:
        if j in vowel:
            count=0
        else:
            count+=1
            if count==4:
                is_easy=False
                break
    if is_easy:
        print('YES')
    else:
        print('NO')