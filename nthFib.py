def fib(n):
    a=0
    b=1
    res=[a,b]
    while(n!=0):
        ele=a+b
        res.append(ele)
        a=b
        b=ele
        n-=1
    return res    

def main():
    n=int(input())
    res=fib(n)
    print(res)
    print(res[n-1])
if __name__ == '__main__':
    main()   