class Solution:
    def buddyStrings(self, a,b):
        if len(a)!=len(b):
            return False
        if a==b:
            if len(a)-len(set(a))>=1:
                return True
            else:
                False
        s=[]
        for i in range(len(a)):
            if a[i]!=b[i]:
                s.append(a[i])
        if len(s)>2:
            return False
        if len(s)!=2:
            return False
        if a[0]==b[1] and a[1]==b[0]:
            return True
        return False
        
             
print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False