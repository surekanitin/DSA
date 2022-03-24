def getPivot(arr,n):
        start=0
        end=n-1
        mid=start +(end-start)//2
        while(start<end):
            if arr[mid]>=arr[0]:
                start= mid+1
            else:
                end =mid
            mid=start +(end-start)//2
        return start
	
def binarySearch(arr,s,e,k):
    start=s
    end=e
    mid= (start+end)//2
    while start <= end:
        
        if arr[mid]==k:
            return mid

        if k>arr[mid]:
            start=mid+1

        else:
            end=mid-1

        mid= (start+end)//2

    return -1
def findPosition(arr, n, k):
    
    pivot=getPivot(arr,n)
    if (k>= arr[pivot] and k<=arr[n-1]):
        return binarySearch(arr,pivot,n-1,k)
    else:
        return binarySearch(arr,0,pivot,k)
		
#     ans = arr.index(k) if k in arr else -1
#     return ans
	
    