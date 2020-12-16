def sum(x):
    print("sum of",end=" ")
    for i in range(1,x+1):
        if (i%3==0) or (i%5==0):
            print(i,end=" ")

if __name__ == "__main__":
    a=int(input("enter the number:"))
    sum(a)