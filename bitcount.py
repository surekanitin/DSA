
def bit(n):
    count=0
    while(n!=0):
        digit=n&1
        if digit==1:
            count+=1
        n=n>>1    
    return count    


def main():
    a,b=map(int,input().split())
    res=bit(a) + bit(b)
    print(res)

    
if __name__ == '__main__':
    main()   