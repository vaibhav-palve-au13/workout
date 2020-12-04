def sol(nums,temp):
  if len(nums)==len(temp):
    print(temp)
    return
  for i in nums:
    if i not in temp:
      temp.append(i)
      sol(nums,temp)
      temp.pop()
nums=[1,2,3]
sol(nums,[])

def permutation(nums,res):
    if len(nums)==0:
        print(res)
        return
    for i in range(len(nums)):
        permutation(nums[:i]+nums[i+1:],res+nums[i])

if __name__ == "__main__":
    permutation("123","")



# def permute(self, nums):
#     res=[]
#     def helper(nums,temp):
#         if len(nums)==0:
#             res.append(temp)
#             print(temp)
#             return
#         for i in range(len(nums)):
#             helper(nums[:i]+nums[i+1:],temp+nums[i])
    
#     nums="".join(str(i) for i in [1,2,3])
#     helper(nums,"")
#     print(res)
#     return res
    