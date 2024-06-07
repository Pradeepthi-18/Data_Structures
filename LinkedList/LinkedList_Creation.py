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

# Read input
n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

# Construct and print linked list
head = construct_linked_list(arr)
print_linked_list(head)
