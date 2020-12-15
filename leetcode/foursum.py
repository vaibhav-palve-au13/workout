"""Given an array nums of n integers and an integer target, are there elements a, b, c,
and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array
which gives the sum of target.
Notice that the solution set must not contain duplicate quadruplets.
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:
Input: nums = [], target = 0
Output: []
"""


def four_sum( array, target):
    nums = array
    nums.sort()
    result = []
    for i in range(len(nums)  -  3):
        if i>0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        while j <= len(nums)-3:
            k = j+1
            r = len(nums) - 1
            while k < r:
                temp = nums[i] + nums[j] + nums[k] + nums[r]
                if temp == target :
                    result.append([nums[i],nums[j],nums[k],nums[r]])
                    while nums[k] == nums[k+1]:
                        k+=1
                    while nums[r] == nums[r-1]:
                        r-=1
                elif temp < target:
                    k+=1
                else:
                    r-=1
            j +=1        
    return result

if __name__ == "__main__":
    array = [1, 0, -1, 0, -2, 2]
    target = 0
    four_sum(array, target)
