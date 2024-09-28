# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

#Since the two Linked list are already sorted we need to just compare the data in both LL and create a new LL
def mergeLists(head1, head2):
    L=SinglyLinkedListNode(0) # A dummy node is initialized to make new Linkedlist
    current=L # A pointer to the Node
    while head1 and head2:
        if head1.data<=head2.data: # If the data in head1 is less than head2 then append it to the new LL
            current.next=head1
            head1=head1.next # Since data in head1 is added we can skip this
        else:
            current.next=head2 # If the data in head2 is less than head1 then append it to the new LL
            head2=head2.next# Since data in head2 is added we can skip this
        current=current.next #Updating current
     """Checking if any data is left in both head1 and head2 , if found then added to end of the LL since the data 
      will be the greatest element"""
    
    if head1: 
        current.next=head1
    if head2:
        current.next = head2
    return L.next

            

    
