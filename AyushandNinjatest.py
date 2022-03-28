def isPossible(time,n,m,barrier):
    dayCount=1
    chapterSum=0
    for i in range(m):
        if (chapterSum +time[i]<=barrier):
            chapterSum+=time[i]
        else:
            dayCount+=1
            if (dayCount>n or time[i]>barrier):
                return False
            else:
                chapterSum=time[i]
    return True
      

def ayushGivesNinjatest(n, m, time):
    # Write your code here.
    start = 0
    end = sum(time)
    mid = start + (end-start)//2
    ans=-1
    while start<=end:
        if isPossible(time,n,m,mid):
            ans=mid
            end=mid-1
        else:
            start=mid+1
        mid=start + (end-start)//2
    return ans
