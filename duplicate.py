def duplicate(arr,n):
    dup={}
    for i in range(n):
      dup[i]=arr.count(i)
    ele=-9999
    for key, value in dup.items():
        if value>1:
            ele=key
    return ele
def main():
    n=int(input())
    arr=list(map(int,input().split()))
    print("Elements ",arr)
    ele=duplicate(arr,n)
    print("Duplicate Element",ele)
if __name__ == '__main__':
    main()