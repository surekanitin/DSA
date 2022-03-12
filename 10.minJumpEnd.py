#https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1#

#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        count=0
        i=1
        jump=arr[0]
        if arr[0]==0:
            return -1
        if arr[0]>n-1:
            return 1
        while i<n-1:
            li=arr[i:i+jump]
            print(li)
            mx=max(li)
            print(mx)
            jump=mx
            count+=1
            if mx>=n:
                count+=1
                return count
            # elif i+mx>=n:
            #     count+=2
            #     return count    
        if count==0:
            return -1
        else:
            return count
            
                
    
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