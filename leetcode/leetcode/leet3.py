# import heapq
# sorted_stack=[]
# arr=[1,2,3,4,5,6,7,8]
# heapq.heapify(arr)
# while arr:
#     curr=heapq.heappop(arr)
#     sorted_stack.append(curr)
# print(sorted_stack)
# print(sorted_stack[::-1])
# heapq
# print(arr)
# heapq.heapify(arr)
# print(arr)
# arr=[-1*i for i in arr]
# print(arr)

# x=input()
# stack1=[]
# while x!="exit":
#     stack1.append(els)
    
#     ele=input()

# stack=[1,5,4,6,7,8,9]
# sorted_stack=[]
# while stack :
#     top =stack.pop()
#     # if sorted_stack:
#     #     while sorted_stack:
#     #         if sorted_stack[-1]<top :
#     #             break
#     #         stack.append(sorted_stack.pop(-1))
#     sorted_stack.append(top)
# print(sorted_stack)


s=["({})"]
stack=[]
l=len(s)
if l%2:
    print("false")
anyof=set(["(","[","{"])
for i in s:
    if i not in stack:
        stack.append(i)

    else:
        if i=="(":
            if stack or stack.pop(-1)=="(":
                continue
            else:
                print("false")
        elif i=="[":
            if stack or stack.pop(-1)=="[":
                continue
            else:
                print("false")
        elif i=="{":
            if stack or stack.pop(-1)=="{":
                continue
            else:
                print("false")
if not stack:
    print("true")