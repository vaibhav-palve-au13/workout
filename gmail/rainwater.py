# def capacity(arr):
#     # Fill this in.
#     ans=0
#     for i in range(1,len(arr)-1):
#         max_left=max(arr[:i])
#         max_right=max(arr[i+1:])
#         water=min(max_left,max_right)-arr[i]
#         if water>0:
#             ans+=water

#     return ans

# print(capacity([0, 11, 0, 2, 10, 0, 1, 3, 2, 1, 2, 1]))
# 6
# class Solution:
##     ## Method 1 -----------------------------
##     
## Brute Force --------------------------
##     def trap(self, height: List[int]) -> int:
##         N = len(height)
#         
##         result = 0
##         for n in range(1, N-1):
##             max_left = max(height[:n])
##             max_right = max(height[n+1:])
#             
##             water = min(max_left, max_right) - height[n]
##             # print(water)
##             if water > 0:
##                 result += water
#                 
##         return result
#     
#     ## Method 3 -----------------------------
#     ## Monotonic Stack --------------------------
#     def trap(self, height: List[int]) -> int:
#         stack, res = [], 0
#         
##         for i, h in enumerate(height):
##             while stack and height[stack[-1]] < h:
##                 bottom = stack.pop()
##                 if stack: 
##                     res += (min(h, height[stack[-1]]) - height[bottom]) * (i - stack[-1] - 1)
##             stack.append(i)      
##         return res
#     
#     
##     ## Method 2 -----------------------------
##     ## DP + prefix max --------------------------
##     def trap(self, height: List[int]) -> int:
##         ## store maxLeft and maxRight of current element
##         N = len(height)
##         maxLeft = [0]*N
##         maxRight = [0]*N
##         for i in range(1, N):
##             maxLeft[i] = max(maxLeft[i-1], height[i-1])
##             maxRight[N-1-i] = max(height[N-i], maxRight[N-i])
##         # print(maxLeft, maxRight)
#         
##         result = 0
##         for i in range(N):
##             water = min(maxLeft[i], maxRight[i]) - height[i]
##             if water > 0:
##                 result += water
#                 
##         return result
# 
# 
##     ## Method 3 -----------------------------
##     ## Two Pointers --------------------------
##     def trap(self, height: List[int]) -> int:
##         l, r = 0, len(height)-1
##         maxLeft, maxRight = 0, 0
##         result = 0
##         while l < r:
##             maxLeft = max(maxLeft, height[l])
##             maxRight = max(maxRight, height[r])
##             if height[l] < height[r]:
##                 result += maxLeft - height[l]
##                 l += 1
##             else:
##                 result += maxRight - height[r]
##                 r -= 1
##             # print(l, r, result)
#         
##         return result

def sol(height):
    l=0
    r=len(height)-1
    left_max,right_max=0,0
    result=0
    while l< r:
        left_max=max(left_max,height[l])
        right_max=max(right_max,height[r])
        if left_max <= right_max:
            result+=(left_max - height[l])
            l+=1
        else :
            result+=(right_max -height[r])
    return result
print(sol([0, 11, 0, 2, 10, 0, 1, 3, 2, 1, 2, 1]))