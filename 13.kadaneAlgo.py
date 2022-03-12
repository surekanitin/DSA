#https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1#

#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        currentSum=0
        maxSum=-1e8
        for i in range(N):
            currentSum+=arr[i]
            if currentSum>maxSum:
                maxSum=currentSum
            if currentSum<0:
                currentSum=0
        return maxSum        
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends