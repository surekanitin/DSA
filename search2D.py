#https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        mat=[]
        for i in range(m):
            for j in range(n):
                ele=matrix[i][j]
                mat.append(ele)
                
        start=0
        end=len(mat)-1
        mid=start+(end-start)//2
        while(start<=end):
            if target==mat[mid]:
                return True
            if target>mat[mid]:
                start=mid+1
            else:
                end=mid-1
            mid=start+(end-start)//2 
        return False   
#       m=len(matrix)
#         n=len(matrix[0])
#         for i in range(m):
#             for j in range(n):
#                 if target==matrix[i][j]:
#                     return True
                
#         return False   