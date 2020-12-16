
# binary search using recursion

def binarysearch(a,target,l,r):
    if l<= r:
        mid=(l+r)//2
        if a[mid]==target:
            return mid
        elif a[mid]<target:
            return binarysearch(a,target,mid+1,r)
        else:
            return binarysearch(a,target,l,mid-1)
    else:
        return None

if __name__ == "__main__":
    a=[-3,2,3,4,5,6,7,8,9,10]
    l=0
    target=9  
    r=len(a)-1
    b=binarysearch(a,target,l,r)
    print(b)
# binary search using two pointer
def binarysearc(a,target,l,r):
    while l<=r:
        mid=(l+r)//2
        if a[mid]==target:
            return mid
        elif a[mid]<target:
            l=mid
        else:
            r=mid
        

if __name__ == "__main__":
    a=[-3,2,3,4,5,6,7,8,9,10]
    l=0
    target=5
    r=len(a)-1
    b=binarysearch(a,target,l,r)
    print(b)