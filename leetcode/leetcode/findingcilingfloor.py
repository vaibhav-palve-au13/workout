class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  # Fill this in.
    if root_node is None:
        return

    if root.value < k:
        if root_node.right.value >k:
            return 
    else:

        if root_node.value > k :
            return 
    lh=findCeilingFloor(root_node.left,k) 
    rh=findCeilingFloor(root_node.right,k)
    return (lh,rh)
        


if __name__ == "__main__":
        
    root = Node(8) 
    root.left = Node(4) 
    root.right = Node(12) 
    
    root.left.left = Node(2) 
    root.left.right = Node(6) 
    
    root.right.left = Node(10) 
    root.right.right = Node(14) 

    print (findCeilingFloor(root, 5))
    # (4, 6)
