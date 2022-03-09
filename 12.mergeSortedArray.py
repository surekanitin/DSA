#https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1#

#User function Template for python3

class Solution:
    def merge(self, arr1, arr2, n, m): 
        # code here
        i = n-1
        j=0
        while (i>=0 and j<m):
            if (arr1[i]>arr2[j]):
                temp=arr1[i]
                arr1[i]=arr2[j]
                arr2[j]=temp
                print(arr1)
                print(arr2)
            
            i-=1
            j+=1
        arr1.sort()
        arr2.sort() 
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":         
    tc=int(input())
    while tc > 0:
        n, m=map(int, (input().strip().split()))
        arr1=list(map(int , input().strip().split()))
        arr2=list(map(int , input().strip().split()))
        ob = Solution()
        ans=ob.merge(arr1, arr2, n, m)
        for x in arr1:
            print(x, end=" ")
        for x in arr2:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends