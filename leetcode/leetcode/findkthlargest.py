def findKthLargest(nums, k):
    c=0
    for i in nums:
        if i >=k:
            c+=1
    return c
print(findKthLargest([3, 5, 2, 4,5,8,6,3,2, 6, 8], 3))
# 5