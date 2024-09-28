#Solution for - Delete duplicate-value nodes from a sorted linked list



# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
#The Code uses two pointer system one for the inner loop and other for outer loop which iterates through
# the Linked List
def removeDuplicates(llist):
    temp=llist # A pointer to compare the data
    while(temp!=None):
        temp1=temp # Second pointer which traverses through the LL
        while(temp1.next!=None):
            if temp1.next.data==temp.data: # Checks for duplicates ,  if found then skips the. node
                temp1.next=temp1.next.next
            else:
                temp1=temp1.next # Updating temp1
        temp=temp.next # Updating temp
    return llist
