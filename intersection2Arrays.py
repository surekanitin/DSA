from collections import Counter

def inter(nums1,nums2):
    # nums3=[]
    # for i in range(len(nums1)):
    #     for j in range(len(nums2)):
    #         if nums1[i] == nums2[j]:
    #             nums3.append(nums1[i])
    #             nums2[j]=-1
    #             break
    # return nums3        
    nums3=[]
    res=Counter(nums1) & Counter(nums2)
    for i in res.elements():
        nums3.append(i)
    return nums3

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
    nums3=inter(nums1,nums2)
    print("Unique Element",nums3)
if __name__ == '__main__':
    main()