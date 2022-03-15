#https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # count=Counter(nums)
        # ans=[]
        # for key in count.keys():
        #     if count[key]==2:
        #         ans.append(key)
        # ans.sort()        
        # return ans    
        output=[]
        for num in nums:
            if nums[abs(num) - 1] < 0:
                output.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return output