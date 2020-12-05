# class binary:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def add(self,data):
#         if data==self.data:
#             return 
#         if data<self.data:
#             if self.left:
#                 self.data.left.add(data)
#             else:
#                 self.data=binary(data)
#         else:
#             if  self.right:
#                 self.data.right.add(data)
#             else:
#                 self.data=binary(data)
# def inorder(self):
#     element=[]
#     if self.left:
#         element+=self.left.inorder()
#     element.append(self.data)
#     if self.right:
#         element+=self.right.inorder()
#     return element
# def build(element):
#     root=binary(element[0])
#     for i in range(1,len(element)):
#         root.add(element[i])
#     return root

# if __name__ == "__main__":
#     arr=[7,5,3,8,4,6,1,9]
#     new=build(arr)
#     print(inorder())
