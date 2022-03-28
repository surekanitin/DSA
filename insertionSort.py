from typing import List

def insertionSort(n: int, arr: List[int]) -> None:
    # Write your code here.
    for i in range(1,n):
        temp=arr[i]
        j=i-1
        while j>=0:
            if arr[j]>temp:
                arr[j+1]=arr[j]
            else:
                break
            j-=1
        arr[j+1]=temp