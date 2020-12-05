# # Function to print contiguous sublist with the largest sum
# # in given set of integers
# def kadane(A):

# 	# stores maximum sum sublist found so far
# 	maxSoFar = 0
# 	# stores maximum sum of sublist ending at current position
# 	maxEndingHere = 0
# 	# stores end-points of maximum sum sublist found so far
# 	start = end = 0
# 	# stores starting index of a positive sum sequence
# 	beg = 0
# 	# traverse the given list
# 	for i in range(len(A)):
# 		# update maximum sum of sublist "ending" at index i
# 		maxEndingHere = maxEndingHere + A[i]
# 		# if maximum sum is negative, set it to 0
# 		if maxEndingHere < 0:
# 			maxEndingHere = 0		# empty sublist
# 			beg = i + 1
# 		# update result if current sublist sum is found to be greater
# 		if maxSoFar < maxEndingHere:
# 			maxSoFar = maxEndingHere
# 			start = beg
# 			end = i
# 	print("The sum of contiguous sublist with the largest sum is", maxSoFar)
# 	print("The contiguous sublist with the largest sum is", A[start: end + 1])


# if __name__ == '__main__':

# 	A = [34, -50, 42, 14, -5, 86]
# 	kadane(A)
def sol(arr):
    m=0
    max=0
    s=e=0
    b=0
    for i in range(len(arr)):
        max=max+arr[i]
        if max<0:
            max=0
            b=i+1
        if m<max:
            m=max
            s=b
            e=i+1
            print(max)
    return arr[s:e]

if __name__ == "__main__":
    a=[1,5,8,6,-100,3,4,5,10]
    print(sol(a))