"""
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use
the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""
class TwoSum :
    def __init__(self, array, target):
        self.array = array
        self.tar = target

    def twosum(self):
        mapping = dict()
        for i in range(len(self.array)):
            if self.tar - array[i] in mapping:
                return [mapping[self.tar - array[i]],i]
            else:
                mapping[array[i]] = i
        return [-1, -1]

if __name__ == "__main__":
    array  = [2, 7, 11, 15]
    target = 9
    s = TwoSum(array, target)
    print(s.twosum())
