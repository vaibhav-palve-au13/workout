# '''a=input("enter a name  :\n")
# print("good mornig,"+a)'''
# name = input(" enter a name :")
# date=input (" enter a date")
# company=input("enter a name ")
# contury="india"
# letter = ''' dear  # ,
# you are selected 
# for a team leader for @ company and you csn go * conturie 
# date 1'''
# letter=letter.replace("#",name)
# letter=letter.replace("@",company)
# letter=letter.replace("*",contury)
# letter= letter.replace("1",date)
# print(letter)


# st=" this is a string with double  spaces "
# doublespace=a.find("  ")
# a=st.replce("  "," ")
# print(doublespace)
# print(a)
# string="this is contain  space"
# string=string.replace("  "," ")
# print(string)
# print(string.count("t"))
# print(string.capitalize())

# list=[1,5,1,2,3,4,7]
# dict={}
# for i in range(len(list)):
#     dict[list[i]]=i
    
#     if i in dict:
#         print(dict[i],i)
# a=[1,2,3,4,5,6]
# for i in range(len(a)-1):
#     print(a[i],"index no .",i)
def sol(s):
    cp=0
    op=0
    for i in range(len(s)):
        if s[i]=="(":
            cp+=1
        else :
            op+=1
        if op>cp:
            return False
    return cp==op
def solve (s,n):
    if len(s)==2*n:
        if sol(s):
            print(s) 
        return 
    else:
        solve(s +"(",n)
        solve(s +")",n)
        

print(solve("",3))
