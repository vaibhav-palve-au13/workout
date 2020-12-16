s=[4,5,6,1,2,3]
print(len(s))
temp=[]
curr,x=0,0
while s !=0:
    x=s.pop()
    s.pop()
    if len(s)>=0:
        temp.append(curr)    
    else :
        j=True
        
        while j :
            if curr < temp[len(temp)-1]:
                s.append(curr)
                if len(temp)==0:
                    j = False
            else :
                j=False
    temp.append(curr)            
s.append(temp)
print(s)
