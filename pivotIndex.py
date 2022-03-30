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


def main():
    n= int(input())
    arr=list(map(int,input().split())) 
    res=getPivot(arr, n)
    print(res)

if __name__ == '__main__':
    main()