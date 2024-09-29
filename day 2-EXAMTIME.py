T=int(input())
for i in range(T):
    D_DSA,D_TOC,D_DM=map(int,input().split())
    D_sum=D_DSA+D_TOC+D_DM
    S_DSA,S_TOC,S_DM=map(int,input().split())
    S_sum=S_DSA+S_TOC+S_DM
    if D_sum>S_sum:
        print('DRAGON')
    elif D_sum<S_sum:
        print('SLOTH')
    elif D_sum==S_sum:
        if D_DSA>S_DSA:
            print('DRAGON')
        elif D_DSA<S_DSA:
            print('SLOTH')
        elif D_DSA==S_DSA:
            if D_TOC>S_TOC:
                print('DRAGON')
            elif D_TOC<S_TOC:
                print('SLOTH')
            else:
                print('TIE')
        else:
          print('TIE')    
    else:
        print('TIE')