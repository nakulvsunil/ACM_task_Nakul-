class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the front
    def insertFront(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    # Insertion at the end
    def insertEnd(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
        newNode.prev = last

    # Insertion at a given position
    def insertPos(self, position, newData):
    if position == 0:
        newNode = Node(newData)
        newNode.next = self.head
        if self.head:
            self.head.prev = newNode
        self.head = newNode
        return

    newNode = Node(newData)
    current = self.head
    count = 0

    while current is not None and count < position - 1:
        current = current.next
        count += 1

    if current is None:
        print("Position is beyond the length of the list")
        return

    newNode.next = current.next
    if current.next is not None:
        current.next.prev = newNode
    current.next = newNode
    newNode.prev = current

    # Deletion at the front
    def deleteFront(self):
        if self.head is None:  # If the list is empty
            print("The list is empty.")
            return
        if self.head.next is None:  # If there's only one element
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # Deletion at the end
    def deleteEnd(self):
        if self.head is None:  # If the list is empty
            print("The list is empty.")
            return
        if self.head.next is None:  # If there's only one element
            self.head = None
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = None

    # Deletion at a given position
    def deleteAtPos(self, pos):
        if self.head is None:  
            print("The list is empty.")
            return
        temp = self.head
        if pos == 0:  # If the position is the head 
            self.deleteFront()
            return
        for _ in range(pos):
            if temp is None:  # If position is greater than the number of nodes
                print("Position out of bounds.")
                return
            temp = temp.next
        if temp.next: 
            temp.next.prev = temp.prev
        if temp.prev:  
            temp.prev.next = temp.next

    # Display 
    def displayFront(self):
        current = self.head
        last = None
        print("Traversal in forward direction:")
        while current:
            print(current.data, end=" ")
            last = current  # Store the last node for reverse traversal
            current = current.next
        print("\nTraversal in reverse direction:")
        while last:
            print(last.data, end=" ")
            last = last.prev
        print()

#Insertion
dll = DoublyLinkedList()
dll.insertFront(10)  
dll.insertFront(5)
dll.insertEnd(20)    
dll.insertEnd(30)

#Display
dll.display()


dll.deleteFront() 
dll.deleteEnd()   
dll.insertEnd(25)  
dll.insertEnd(35)
dll.deleteAtPos(1)  
dll.display()
