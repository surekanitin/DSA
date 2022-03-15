from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    i=0
    j=n-1
    print("Before sorting",arr)
    step=0
    while(i<j):
        print("step ",step)
        step+=1
        while arr[i]==0 and i<j:
            i+=1
            print(arr)
        while arr[j]==2 and i<j:
            j-=1
            print(arr)
        if arr[i]>arr[j] and i<j:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
            i+=1
            j-=1   
            print(arr) 
    print("After sorting ",arr)

#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
