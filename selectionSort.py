def selectionSort(arr,n):
    # Write your code here
    # Do not return anything. Update the given array in-place
    for i in range(n-1):
        mn=i
        j=i+1
        while(j<n):
            if arr[j]<arr[mn]:
                mn=j
            j+=1
        temp=arr[i]
        arr[i]=arr[mn]
        arr[mn]=temp
    return arr
                