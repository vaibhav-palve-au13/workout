def maximum_product_of_three(lst):
  # Fill this in.
    ans=0
    for i in range(len(lst)-3):
        for j in range(len(lst)-2):
            for k in range(len(lst)-1):
                ans=lst[i]*lst[j]*lst[k+1]
    return ans


print(maximum_product_of_three([-4, -4, 2, 8]))
# 128