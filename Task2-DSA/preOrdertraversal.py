"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

"""
In this code we are first printing the root value then using recursive call we reach the left subtree then print it's 
data then going to the right subtree using recursive call.
"""
def preOrder(root):
    if root:
        print(root.info,end=" ")# Visit the root node (current node)
        preOrder(root.left)# Traverse the left subtree
        preOrder(root.right)# Traverse the right subtree
        
        
      
