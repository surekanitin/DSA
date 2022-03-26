def isPossible(arr,n,m,mid):
    studentCount=1
    pageSum=0
    for i in range(n):
        print(f"step {i}")
        if pageSum +arr[i]<=mid:
            pageSum+=arr[i]
            print(f"if{pageSum}")  
        else:
            studentCount+=1
            if studentCount>m or arr[i]>mid:
                return False
            pageSum=arr[i]
            print(f"Else{pageSum}")   
    return True   


def allocateBooks(arr, n, m):

    # Write your code here
    # Return the minimum number of pages
    start = 0
    end = sum(arr)
    mid = start + (end-start)//2
    ans=-1
    while start<=end:
        print(f"mid {mid}")
        if isPossible(arr,n,m,mid):
            ans=mid
            end=mid-1
        else:
            start=mid+1
        mid=start + (end-start)//2
    return ans


def main():
        n,m=map(int,input().split())
        arr=list(map(int,input().split())) 
        result=allocateBooks(arr, n, m)
        print(result)


if __name__=='__main__':
    main()
    
