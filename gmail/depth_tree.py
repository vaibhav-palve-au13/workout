class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
    # string representation
        return self.val

def deepest(node):
  # Fill this in.
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    l=deepest(node.left)
    r=deepest(node.right)
    return 1+max(l,r) 


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)