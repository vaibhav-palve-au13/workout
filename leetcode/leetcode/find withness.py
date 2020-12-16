def withness(arr):
    count=0
    max=0
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>max:
            max=arr[i]
            print(arr[i])
            count+=1
    return count
if __name__ == "__main__":
    arr=[8,5,3,2,1]
    print(withness(arr))

