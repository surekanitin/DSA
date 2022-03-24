from sympy import N


def sqrtN(n):

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

def main():      
    n = int(input())
    result = sqrtN(n)
    print(result)  


if __name__ == '__main__':
    main()
    
            