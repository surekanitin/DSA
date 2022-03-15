import math

def firstOccurrence(arr,n,k):
    start=0
    end=n-1
    mid= (start+end)//2
    ans=-1
    while start <= end:
        if arr[mid]==k:
            ans=mid
            end=mid-1
        elif k>arr[mid]:
            start=mid+1
        else:
            end=mid-1
        mid= (start+end)//2
    return ans   

def lastOccurrence(arr,n,k):
    start=0
    end=n-1
    mid= (start+end)//2
    ans=-1
    while start <= end:
        if arr[mid]==k:
            ans=mid
            start=mid+1
        elif k>arr[mid]:
            start=mid+1
        else:
            end=mid-1
        mid= (start+end)//2

    return ans 

def firstAndLastPosition(arr, n, k):
    # Write your code here
    res=[]
    res.append(firstOccurrence(arr,n,k))
    res.append(lastOccurrence(arr,n,k))
    return res

def main():
    n,k=map(int,input().split())
    arr=list(map(int,input().split())) 
    res=firstAndLastPosition(arr, n, k)
    print(res)

if __name__ == '__main__':
    main()

	