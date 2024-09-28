"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

"""
In this code we first traversing through the left subtree using recursive call then through the right subtree finally printing the data at these nodes.
"""
def postOrder(root):
    if root:
        postOrder(root.left)# Traverse the left subtree
        postOrder(root.right)# Traverse the right subtree
        print(root.info,end=" ")# Visit the root node
        
