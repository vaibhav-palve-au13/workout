class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def add(self,x):
    if head is None:
        return node(x)
    else:
        new=node(x)
        temp=head
        while temp!=None:
            temp=temp.next
        temp.next=new
        return head
        
    
def insertion(self,target,x):
    temp=head
    new=node(x)
    if temp.data!=target:
        temp=temp.next
    n=temp.next
    temp.next=new
    new.next=n
def delectiion(self,target):
    temp=head
    while temp.next!=target:
        temp=temp.next
    prev=temp    
    prev.next=temp.next.next
def printll(self):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
if __name__ == "__main__":
    head=None
    head=add(head,3)
    head=add(head,5)
    head=add(head,3)

    printll(head)   













# class node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None
# def add(head,x):
#     if head is None:
#         return node(x)
#     else:
#         new_node=node(x)
#         temp=head
#         while temp.next!=None:
#             temp=temp.next
#         temp.next=new_node
#         return head
# def insertion(head,target,x):
#     temp=head
#     while temp.data!=target:
#         temp=temp.next
#     neighbor=temp
#     new_node=node(x)
#     temp.next=new_node
#     new_node.next=neighbor
# def delete(head,target,x):
#     temp=head
#     while temp.next.data != target:
#         temp=temp.next
#     temp.next=temp.next.next
#     return head

# def printll(head):
#     temp=head
#     while temp !=None:
#         print(temp.data)
#         temp=temp.next
# if __name__ == "__main__":
#     head=None
#     head=add(head,11)
#     head=add(head,22)
#     head=add(head,33)
#     head=insertion(head,2,22)
#     printll(head)