# arr=[1,3,2,4,1]
# stack=[]  
# min_stack=[]
# for i in range(len(arr)-1,-1,-1):
#     if len(stack)==0:
#         min_stack.append(-1)
#     elif stack[-1]>arr[i] and len(stack)>0:
#         min_stack.append(stack[-1])
#     elif stack[-1]<=arr[i] and len(stack)>0:
#         while len(stack)>0 and stack[-1]<=arr[i]:
#             stack.pop()
#         if len(stack)==0:
#             min_stack.append(-1)
#         else:
#             min_stack.append(stack[-1])
#     stack.append(arr[i])
# print((min_stack),stack)

arr=[3, 1 ,2 ,9 ,2, 2 ]
stack=[]  
min_stack=[]
for i in range(len(arr)-1,-1,-1):
    if len(stack)==0:
        min_stack.append(-1)
    elif stack[-1]>arr[i] and len(stack)>0:
        min_stack.append(stack[-1])
    elif stack[-1]<=arr[i] and len(stack)>0:
        while len(stack)>0 and stack[-1]<=arr[i]:
            stack.pop()
        if len(stack)==0:
            min_stack.append(-1)
        else:
            min_stack.append(stack[-1])
    stack.append(arr[i])
print((min_stack),stack)


