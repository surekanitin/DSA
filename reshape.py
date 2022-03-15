#https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
		# Check weather the matrix can be made by using the given r,c values.
        if m*n != r*c:
            return mat
		# Storing in 1-d Array.
        arr = [0 for i in range(m*n)]
        count=0
        for i in range(m):
            for j in range(n):
                arr[count] = mat[i][j]
                count+=1
		# Initilize a new Matrix with given Dimensions
        new_matrix = [[0 for i in range(c)] for j in range(r)]
        count =0
        for i in range(r):
            for j in range(c):
                new_matrix[i][j]=arr[count]
                count+=1
        return new_matrix