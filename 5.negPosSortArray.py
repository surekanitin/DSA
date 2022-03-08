
#https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/

n=int(input())
arr=list(map(int,input().split()))
c1=0
c2=0
print("Before Sorting: ", arr)   
arr1=[]
arr2=[]
for i in range(n):
    if arr[i]<0:
        c1+=1
        arr1.append(arr[i])
    else:
        c2+=1
        arr2.append(arr[i])
        
i=0        
for i in range(n):
    if i<c1:
        arr[i]=arr1[i]
    if i>=c1:
        arr[i]=arr2[n-i-1]
print("After sorting: ", arr)        
        
  

    
        
        
        
        
        
        