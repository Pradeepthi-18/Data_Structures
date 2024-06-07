class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(curr):
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print() 

def construct_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

def insertNodeAtTail(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    
    current = head
    while current.next is not None:
        current = current.next
    
    current.next = new_node
    return head                                                                                                                                       

def insertNodeAtHead(llist, data):
    temp = Node(data)
    if llist is None:
        return temp 
    temp.next = llist 
    return temp                                                                                                                            

def insertNodeAtPosition(llist, data, position):
    temp = Node(data)
    if position == 0:
        temp.next = llist
        return temp

    currentIndex = 0 
    currentNode = llist
    while currentIndex != position - 1 and currentNode is not None:
        currentIndex += 1 
        currentNode = currentNode.next 
    
    if currentNode is None:
        raise IndexError("Position out of bounds")
    
    temp.next = currentNode.next 
    currentNode.next = temp 
    return llist

# Read input
n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

# Construct and print linked list
head = construct_linked_list(arr)
print("Original linked list:")
print_linked_list(head)

# Insert at tail
tail_data = int(input("Enter the element to insert at the tail: "))
head = insertNodeAtTail(head, tail_data)
print("After inserting at tail:")
print_linked_list(head)

# Insert at head
head_data = int(input("Enter the element to insert at the head: "))
head = insertNodeAtHead(head, head_data)
print("After inserting at head:")
print_linked_list(head)

# Insert at a specific position
position = int(input("Enter the position to insert the new element: "))
position_data = int(input("Enter the element to insert at the position: "))
head = insertNodeAtPosition(head, position_data, position)
print("After inserting at position", position, ":")
print_linked_list(head)
