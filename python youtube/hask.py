# def hask(key):
#     h=0
#     for i in key:
#         h+=ord(i)
#     return h%100
# print(hask("vp"))


# stock_price=[1,2.0,3,4,5,6,7,8]
# for  i in stock_price:
#     token=i.split(",")
#     day=token[0]
#     price=float(token[1])
#     stock_price.append(day,price)



n = int(input())
s = input()
k = int(input())
if k > 26:
    k = k % 26
s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = s1[k:] + s1[:k]
res = ''
dict1 = {}
for i in range(26):
    dict1[s1[i]] = s2[i]
for i in range(n):
    if ord(s[i]) in range(97, 123) or ord(s[i]) in range(65, 91):
        if ord(s[i]) in range(65, 91):
            temp = ord(s[i]) + 32
            temp = dict1[chr(temp)]
            temp = chr(ord(temp) - 32)
            res += temp
        else:
            res += dict1[s[i]]
    else:
        res += s[i]

print(res)
1
