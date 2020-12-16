class stack:
    def __init__(self):
        self.stack=[]
        self.stack2=[]
    def push(self,x):
        self.stack.append(x)
        print(self.stack)
        return
    def pop(self):
        a=self.stack.pop()
        self.stack2.append(a)
        print(self.stack2)
    def comparise(self):
        a=self.stack2.pop()
        
        
        self.push(a)
        self.pop()

if __name__ == "__main__":
    s=stack()
    s.push(3)
    s.push(5)
    s.pop()
    s.push(86)
    s.push(84)
    s.push(83)
    s.push(82)
    s.push(8)
    s.pop()
    s.comparise()


