from collections import Counter

def inter(arr,brr,n,m):
    ans=[]
    i=0
    j=0
    while(i<n and j<m):
        if arr[i]==brr[j]:
            ans.append(arr[i])
            i+=1
            j+=1
        elif arr[i]<brr[j]:
            i+=1
        else:
            j+=1
    return ans        
    # nums3=[]
    # for i in range(len(nums1)):
    #     for j in range(len(nums2)):
    #         if nums1[i] == nums2[j]:
    #             nums3.append(nums1[i])
    #             nums2[j]=-1
    #             break
    # return nums3        
    # nums3=[]
    # res=Counter(nums1) & Counter(nums2)
    # for i in res.elements():
    #     nums3.append(i)
    # return nums3

    #res = []
    # for num in nums2:
    #     if counts1[num] > 0:
    #         res += num,
    #         counts1[num] -= 1
    # return res


def main():
    n,m=map(int,input().split())
    nums1=list(map(int,input().split()))
    nums2=list(map(int,input().split()))
    print("Elements of Array 1",nums1)
    print("Elements of Array 2",nums2)
    nums3=inter(nums1,nums2,n,m)
    print("Unique Element",nums3)
if __name__ == '__main__':
    main()