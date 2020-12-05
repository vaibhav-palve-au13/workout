def buy_and_sell(arr):
    maxprofit=0
    buy=arr[0]
    for i in range(1,len(arr)):
        maxprofit=max(maxprofit,arr[i]-buy)
        buy=min(buy,arr[i])
    return maxprofit

print(buy_and_sell([152,845,6325,741,1,5645,894]))
# # 5

# def buy_and_sell(arr):
#     maxprofit=0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             profit=arr[j]-arr[i]
#             if profit>maxprofit:
#                 maxprofit=profit
#     return maxprofit

#   #Fill this in.
  
# print(buy_and_sell([9, 11, 8, 5, 7, 10,55454,545,665,554,4,5454,5245,5,6565,65,665,635]))
# # 5