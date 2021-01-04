"""
Given an array nums of n integers where n > 1, return an array output such
that output[i] is equal to the product of all the elements of nums except nums[i].
Example:
Input: [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the
array (including the whole array) fits in a 32 bit integer.
Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity? (The output array does not count as
extra space for the purpose of space complexity analysis.)
"""
# basic approch:- time complexity o(n)^2 space complaxity o(n)
arr = [1, 2, 3, 4]
list = []
for i in range(len(arr)):
    sum = 1
    for j in range(i+1, len(arr)):
        sum *= arr[j]
    for k in range(i-1, -1, -1):
        sum *= arr[k]
    list.append(sum)
print(list)
# op:- list = [24, 12, 8, 6]
# time complexity o(n) 
array = [1,2,3,4]
result = [1]*len(array)
for i in range(1,len(array)):
    result[i]=array[i-1]*result[i-1]
right_prod = 1
for j in range(len(array)-1,-1,-1):
    result[j]*=right_prod
    right_prod*=array[j]
print(result)

