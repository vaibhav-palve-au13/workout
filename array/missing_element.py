# # def sol(arr):
# #     visited=[0 for _ in range(10)]
# #     for i in range(len(arr)):
# #         if visited[arr[i]]!=1:
# #             visited[arr[i]]=1
# #     for i in range(len(visited)):
# #         if visited[i] !=1:
# #             print(i,end=" ")

# # if __name__ == "__main__":
# #     print(sol([1,2,4,5]))

# def sol(arr):
#     nums=set(arr)
#     n=len(arr)+1
#     for i in range(n):
#         if i not in nums:
#             return i
# if __name__ == "__main__":
#     arr=[0,1,2,3,5]
#     print(sol(arr))
arr=[5,6,3,1,4]
n=len(arr)
total=(n+2)*(n+1)//2
print(sum(arr))
print(total-sum(arr))