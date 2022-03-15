def binarySearch(arr,n,k):
    start=0
    end=n-1
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

def main():
    n,k=map(int,input().split())
    arr=list(map(int,input().split())) 
    res=binarySearch(arr, n, k)
    print(res)

if __name__ == '__main__':
    main()