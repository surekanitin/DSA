def isPossible(stalls,k,mid):
    cowCount=1
    lastPosition=stalls[0]
    for i in range(len(stalls)):
        if stalls[i]-lastPosition>=mid:
            cowCount+=1
            if cowCount==k:
                return True
            lastPosition=stalls[i]
    return False        


def aggressiveCows(stalls, k):
    
    stalls.sort()
    ans=-1
    start=0
    end=stalls[-1]
    mid=start + (end-start)//2
    while start<=end:
        if isPossible(stalls,k,mid):
            ans=mid
            start=mid+1
        else:
            end=mid-1
        mid =start + (end-start)//2
    return ans