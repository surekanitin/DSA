#https://leetcode.com/problems/magnetic-force-between-two-balls/submissions/
#same as agressivecow

def isPossible(position,m,mid):
    magnetCount=1
    lastPosition=position[0]
    for i in range(len(position)):
        if position[i]-lastPosition>=mid:
            magnetCount+=1
            if magnetCount==m:
                return True
            lastPosition=position[i]
    return False
        

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        ans=-1
        start=0
        end=max(position)
        mid=start+(end-start)//2
        while start<=end:
            if isPossible(position,m,mid):
                ans=mid
                start=mid+1
            else:
                end=mid-1
            mid=start+(end-start)//2
        return ans