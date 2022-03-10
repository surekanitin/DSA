#https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1#
#User function Template for python3
#https://www.interviewbit.com/blog/maximum-subarray-sum/
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        currentSum=0 #current sub array sum
        maxSum=-1e8 ###net arrray sum
        for i in range(N):
            currentSum+=arr[i]#add karo phele wale ke sath
            if currentSum>maxSum:
                maxSum=currentSum #phele wala se bara hai isleye change kardo
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