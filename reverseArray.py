def reverseArray(arr, m):
    # Write your code here.m
    i=m+1
    j=len(arr)-1
    while(i<=j):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr
