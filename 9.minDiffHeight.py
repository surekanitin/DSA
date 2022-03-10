#https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1#

#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        mn=min(arr)
        mx=max(arr)
        res=mx-mn
        for i in range(n):
            if arr[i]>=k:
                mxNew=max(arr[i-1]+k,arr[n-1]-k)
                mnNew=min(arr[0]+k,arr[i]-k)
                res=min(res,mxNew-mnNew)
        return  res    
            
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends