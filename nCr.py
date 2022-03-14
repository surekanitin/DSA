# n c r

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def nCr(n,r):
    num=factorial(n)
    dem= factorial(r)* factorial(n-r)
    return num//dem
def nPr(n,r):
    num=factorial(n)
    dem=factorial(r)
    return num//dem
def main():
    n,r=map(int,input().split())
    ans=nCr(n,r)
    ans1=nPr(n,r)
    print(f"Combination of {n} and {r} is {ans1}")
    print(f"Combination of {n} and {r} is {ans}")
if __name__ == '__main__':
     main()   