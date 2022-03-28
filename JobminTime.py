def isPossible(job,k,mid):
    assignee=1
    totaljobs=0
    for i in range(len(job)):
        if totaljobs+job[i]<=mid:
            totaljobs=job[i]
        else:
            assignee+=1
            if assignee>k or job[i]>mid:
                return False
            totaljobs=job[i]
    return True

def minTime(k,T,job):
    ans=-1
    start=0
    end=sum(job)
    mid=start+(end-start)//2
    while start<=end:
        if isPossible(job,k,mid):
            ans=mid
            end=mid-1
        else:
            start=mid+1
        mid=start+(end-start)//2

    return ans*T

def main():
    k,T=map(int,input().split())
    job=list(map(int,input().split()))
    result=minTime(k,T,job)
    print(result)


if __name__=='__main__':
    main()

