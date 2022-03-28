#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        numberInd = dict()
        n = len(nums)
        for i in range(n):
            secondNum = target - nums[i]
            if secondNum in numberInd.keys():
                return [i, numberInd[secondNum]]
            else:
                numberInd[nums[i]] = i
#         i=0
#         n=len(nums)
#         for i in range(n-1):
#             j=i+1
#             rem=target-nums[i]
#             while(j<n):
#                 if rem==nums[j]:
#                      return i,j
#                 j+=1        
#         return i,j    