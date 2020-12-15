# def sol(arr,x):
#     if x in arr:
#         while x in arr:
#             arr.remove(x)
#     return len(arr)
# if __name__ == "__main__":
#     print(sol([1,2,2,3],2))

def sol1(nums):
    x=2
    stack=[]
    for i in range(len(nums)-1):
        if nums[i]==x:
            stack.append(nums[i])
            nums.pop(i)
            print(stack)
    return len(stack)
if __name__ == "__main__":
    print(sol1([0,1,2,2,3,0,4,2]))