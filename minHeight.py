def isPossible(woods,N,M,woodHeight):
    reqWood=0
    for i in range(N):
        if reqWood<M:
            if  woods[i]>woodHeight:
                reqWood+=woods[i]-woodHeight
        else:
            return True
    if reqWood>=M:
        return True
    else:
        return False


def main():
    N,M=map(int,input().split())
    woods=list(map(int,input().split()))
    ans=0
    start=0
    end=max(woods)
    mid=start+(end-start)//2
    while start<=end:
        if isPossible(woods,N,M,mid):
            ans=mid
            start=mid+1
        else:
            end=mid-1
        mid=start+(end-start)//2
    print(ans)


if __name__=='__main__':
    main()    