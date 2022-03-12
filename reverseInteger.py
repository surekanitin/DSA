#https://leetcode.com/problems/reverse-integer/submissions/

import sys
maxSize = pow(2,31)-1
minSize = -pow(2,31)
def reverse(x):
    ans=0
    sign=1
    if x<0:
        sign=-1
        x=x*-1    
    while x!=0:
        digit=x%10
        ans=ans*10+digit
        x= x//10
    if not  minSize<ans<maxSize:
        return 0
    return sign*ans

def main():
    x=int(input())
    print(reverse(x))  

if __name__=="__main__":
    main()
    
        