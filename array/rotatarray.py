def rotation(arr,n):
    for i in range(n):
        arr[(len(arr)-1)-i],arr[i]=arr[i],arr[(len(arr)-1)-i]
    return arr

    
if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7,8]
    print(rotation(arr,2))


arr=[1,2,3,4,5,6,7,8]
mid=len(arr)//2
print(mid)
l=arr[2:]+arr[:2]
print(l)


