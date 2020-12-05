class Queue:
    def __init__(self):
    # Fill this in.
        self.stack=[]

    def enqueue(self, val):
    # Fill this in.
        self.stack.append(val)

    def dequeue(self):
    # Fill this in.
        return self.stack.pop(0)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue(),end=" ")
print(q.dequeue(),end=" ")
print(q.dequeue())
# 1 2 3