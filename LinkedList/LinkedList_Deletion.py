class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def createLinkedList(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()

def deleteLastNode(head):
    if not head:
        return None
    if not head.next:
        return None  
    
    current = head
    while current.next.next:
        current = current.next
    
    current.next = None
    return head

def deleteHeadNode(head):
    if not head:
        return None
    return head.next

def deleteAtPosition(head, position):
    if position == 1:
        return head.next
    curr = head
    for _ in range(position - 2):
        if curr.next:
            curr = curr.next
        else:
            return head 
    if curr.next:
        curr.next = curr.next.next
    return head

def deleteNodeByValue(head, value):
    if not head:
        return None
    if head.data == value:
        return head.next
    
    curr = head
    while curr.next and curr.next.data != value:
        curr = curr.next
    
    if curr.next:
        curr.next = curr.next.next
    return head

# Read input
n = int(input("Enter the number of elements: "))
values = list(map(int, input("Enter the elements: ").split()))


head = createLinkedList(values)
print("Original linked list:")
printLinkedList(head)

# Delete last node and print linked list
head = deleteLastNode(head)
print("After deleting last node:")
printLinkedList(head)

# Delete head node and print linked list
head = deleteHeadNode(head)
print("After deleting head node:")
printLinkedList(head)

# Delete at a specific position and print linked list
position = int(input("Enter the position to delete the node: "))
head = deleteAtPosition(head, position)
print(f"After deleting node at position {position}:")
printLinkedList(head)

# Delete node by value and print linked list
value = int(input("Enter the value to delete the node: "))
head = deleteNodeByValue(head, value)
print(f"After deleting node with value {value}:")
printLinkedList(head)
