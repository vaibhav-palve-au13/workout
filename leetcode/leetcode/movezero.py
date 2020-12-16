class Solution:
  def moveZeros(self, nums):
    i,j=0,0
    while i <len(nums):
        if nums[i]!=0:
            nums[j]=nums[i]
            j+=1
        i+=1
    for k in range(j,len(nums)):
        nums[k]=0
    return nums
nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]