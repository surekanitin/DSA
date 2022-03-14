def duplicate(arr,n):
    # dup={}
    # for i in range(n):
    #   dup[i]=arr.count(i)
    # ele=-9999
    # for key, value in dup.items():
    #     if value>1:
    #         ele=key
    # return ele
    ans=0
    for i in range(n):
        ans= ans^arr[i]#same element ke sath XOR karne se 0 hota hai
    for i in range(n):
        ans= ans^i   
    return ans 
def main():
    n=int(input())
    arr=list(map(int,input().split()))
    print("Elements ",arr)
    ele=duplicate(arr,n)
    print("Duplicate Element",ele)
if __name__ == '__main__':
    main()