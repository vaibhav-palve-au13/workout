class queue:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        self.stack.append(x)
        print(self.stack)
        return
    def pop(self):
        print(self.stack.pop(0))
        return
if __name__ == "__main__":
    q=queue()
    q.push(3)
    q.push(2)
    q.pop()
    q.push(13)
    q.push(35)
    q.pop()
    q.pop()
    q.push(43)
    