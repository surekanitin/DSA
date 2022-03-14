def unique(arr,n):
    # dup={}
    # for i in range(n):
    #   dup[i]=arr.count(i)
    # ele=-9999
    # for key, value in dup.items():
    #     if value==1:
    #         ele=key
    #         break
    # return ele
    ans=0
    for i in range(n):
        ans= ans^arr[i]#same element ke sath XOR karne se 0 hota hai
    return ans    
def main():
    n=int(input())
    arr=list(map(int,input().split()))
    print("Elements ",arr)
    ele=unique(arr,n)
    print("Unique Element",ele)
if __name__ == '__main__':
    main()