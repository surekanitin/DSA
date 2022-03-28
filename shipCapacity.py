#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/submissions/
#same as book allocation problem

def isPossible(weights,days,mid):
    dayCount=1
    weight=0
    for i in range(len(weights)):
        if weight+weights[i]<=mid:
            weight+=weights[i]
        else:
            dayCount+=1
            if dayCount>days or weights[i]>mid:
                return False
            weight=weights[i]
    return True
    
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start=0
        ans=-1
        end=sum(weights)
        mid=start+(end-start)//2
        while(start<=end):
            if isPossible(weights,days,mid):
                ans=mid
                end=mid-1
            else:
                start=mid+1
            mid=start+(end-start)//2
        return ans