# https://leetcode.com/problems/merge-intervals/submissions/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals=sorted(intervals)
        # n=len(intervals)
        # li=[]
        # if n<=1:
        #     return intervals       
        # i=0
        # j=1
        # while(j<=n-1):
        #     sl=[]
        #     if intervals[i][1]>=intervals[j][0]:
        #         sl.append(intervals[i][0])
        #         if intervals[i][1]>=intervals[j][1]:
        #             sl.append(intervals[i][1])
        #         else:    
        #             sl.append(intervals[j][1])
        #         li.append(sl)
        #         i=i+2
        #         j=j+2
        #     else:
        #         li.append(intervals[i])
        #         li.append(intervals[j])
        #         i=i+1
        #         j=j+1
        # return li        
        intervals.sort(key=lambda i:i[0])
        output=[intervals[0]]
        for start,end in intervals[1:]:
            lastEnd=output[-1][1]
            if start<=lastEnd:
                output[-1][1]=max(lastEnd,end)
            else:
                output.append([start,end])
        return output        
                
                