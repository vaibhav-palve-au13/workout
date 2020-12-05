class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_unival_subtrees(root):
    # Fill this in.
    if root is None:
        return 0
    count=count_unival_subtrees(root.left)+count_unival_subtrees(root.right)
    if is_universal(root):
        count+=1
    return count

def is_universal(root):
    if root is None:
        return True
    if root.left and root.val!=root.left.val:
        return False
    if root.right and root.val!=root.right.val:
        return False
    if is_universal(root.left) and is_universal(root.right):
        return True
    return False
    
a = Node(0)
a.left = Node(0)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))