n,k=map(int,input().split())
nums=list(map(int,input().split()))
nums1=[0]*n
for i in range(n):
    nums[(i+k)%n]=nums[i]
for i in range(n):
    nums[i]=nums1[i]