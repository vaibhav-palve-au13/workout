def finddublicate(arr):
  t=arr[0]
  s=arr[t]
  while True:
    t=arr[t]
    s=arr[arr[s]]
    if t==s:
      break
  ptr1=arr[0]
  ptr2=t
  while ptr1!=ptr2:
    ptr1=arr[ptr1]
    ptr2=arr[ptr2]
  return ptr1
arr=[1,2,3,3,5,4]
print(finddublicate(arr))