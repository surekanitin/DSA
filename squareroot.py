def sqrtInteger(n):
    start=0
    end=n
    mid=start+(end-start)//2
    while(start<=end):
        if mid*mid==n:
            return mid
        elif mid*mid>n:
            end=mid-1
        else:
            start=mid+1
        mid=start+(end-start)//2
    return mid    


def accurateRoot(n,precision,tempResult):
    factor=1
    ans=tempResult
    for i in range(precision):
        factor=factor/10
        j=ans
        while(j*j<n):
            ans=j
            j=j+factor
            print(j)
    return ans        


def main():      
    n, precision = map(int,input().split())
    tempResult = sqrtInteger(n)
    result=accurateRoot(n,precision,tempResult)
    print(result)  


if __name__ == '__main__':
    main()
    
            