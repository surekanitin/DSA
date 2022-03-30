n,k=map(int,input().split())
arr=list(map(int,input().split()))
sm=0
arr.sort()
sm=arr[k-1]+arr[-k]
print(sm)