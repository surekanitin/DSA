#https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1#

#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        res=0
        l=r=0
        while r < n-1:
            far=0
            for i in range(1,r+1):
                far=max(far,i+arr[i])
            l=r+1    
            r=far
            res+=1
        return res    
            
                
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)
# } Driver Code Ends