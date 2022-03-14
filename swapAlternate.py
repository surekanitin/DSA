def swap(arr,n):
    i=0
    while i < n-1:
        temp=arr[i+1]
        arr[i+1]=arr[i]
        arr[i]=temp
        i+=2



def main():
    n=int(input())
    arr=list(map(int,input().split()))
    print("Before alternate swaping ",arr)
    swap(arr,n)
    print("After alternate swaping ",arr)
if __name__ == '__main__':
    main()