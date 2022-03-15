#https://leetcode.com/problems/unique-number-of-occurrences/submissions/
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)     
        x = cnt.values()
        y = set(x)
        return len(x) == len(y)
#         dup={}
#         for i in arr:
#           dup[i]=arr.count(i)
#         #print(dup)
#         res=[]
#         for key, value in dup.items():
            
#             res.append(value)
#         #print(res)    
#         i=0
#         res.sort()
#         while i<len(res)-1:
#             if res[i]==res[i+1]:
#                 return False
#             i+=1
#         return True
            
