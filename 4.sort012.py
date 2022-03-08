#https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

class Solution:
    def sort012(self,arr,n):
        # code here
        e1=arr.count(0)
        e2=arr.count(1)
        e3=arr.count(2)
        for i in range(n):
            if i<e1:
                arr[i]=0
            elif i<e1+e2:
                arr[i]=1
            else:
                arr[i]=2
            
        return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends