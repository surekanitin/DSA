def bubbleSort(arr,n):
    # Write your code here
    # Do not return anything. Update the given array in-place
    s=False
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                s=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if s==False:
            break            
                