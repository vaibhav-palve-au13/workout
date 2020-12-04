def insert(arr,x):
    while len(arr)==10:
        return arr
    arr.append(x)
    return insert(arr,x+1)
def remove(x):
    arr.pop(x)
    return arr   
if __name__ == "__main__":
    arr=[1,2,3,5,6]
    print(insert(arr,4))
    print(remove(5))






