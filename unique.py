def unique(arr,n):
    dup={}
    for i in range(n):
      dup[i]=arr.count(i)
    ele=-9999
    for key, value in dup.items():
        if value==1:
            ele=key
            break
    return ele
def main():
    n=int(input())
    arr=list(map(int,input().split()))
    print("Elements ",arr)
    ele=unique(arr,n)
    print("Unique Element",ele)
if __name__ == '__main__':
    main()