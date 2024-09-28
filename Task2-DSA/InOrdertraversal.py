"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

"""
In this code we are using recursive call to print the inorder traversal of a tree.
Using recursive call we reach the leftmost node then the print statement is encountered which prints the data.
Then we recursively reach the rightmost node
"""
def inOrder(root):
    if root: # Checks if root is present 
        inOrder(root.left) # Traverse the left subtree
        print(root.info,end=" ")# Visit the root node
        inOrder(root.right) # Traverse the right subtree
    
