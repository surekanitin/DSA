#count pairs with given sum

#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        numDict = dict()
        count = 0
        for i in range(n):
            nextNum = k - arr[i]
            if nextNum in numDict:
                count += numDict[nextNum]
            if arr[i] in numDict:
                numDict[arr[i]] += 1
            else: numDict[arr[i]] = 1
        #print(numDict)
        return count
       
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends