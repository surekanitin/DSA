def findArraySum(a, n, b, m):
    # Write your code here.
    i=n-1
    j=m-1
    carry=0
    c=[]
    while i>=0 and j>=0:
        sum=a[i]+b[j]+carry
        carry=sum//10
        sum=sum%10
        c.append(sum)
        i-=1
        j-=1
    while i>=0:
        sum=a[i]+carry
        carry=sum//10
        sum=sum%10
        c.append(sum)
        i-=1
    while j>=0:
        sum=b[j]+carry
        carry=sum//10
        sum=sum%10
        c.append(sum)
        j-=1
    while carry!=0:
        sum=carry
        carry=sum//10
        sum=sum%10
        c.append(sum)
        
    return c[::-1]