#Queue-Construction (Linked list based implementation)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def enQueue(head, val):
    print(val, "inserted")
    newNode = Node(val)
    if head is None:
        return newNode
  
    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = newNode
    return head

def deQueue(head):
    if head is None:
        print("Queue is empty")
        return None
  
    temp = head.next
    print(head.data, "removed")
    head.next = None
    return temp

def frontValue(head):
    if head is None:
        print("Queue is empty")
        return
    print("Front value is:", head.data)

def printQueue(head):
    if head is None:
        print("Queue is empty")
        return
  
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def printIsQEmpty(head):
    if head is None:
        print("Queue is empty")
    else:
        print("Queue is not empty")

head = None
n = int(input("Enter the number of operations: ").strip())
while n > 0:
    word = list(map(int, input().split()))
    l = word[0]
    if l == 1:
        num = word[1]
        head = enQueue(head, num)
    elif l == 2:
        frontValue(head)
    elif l == 3:
        head = deQueue(head)
    elif l == 4:
        printQueue(head)
    else:
        printIsQEmpty(head)
    n -= 1
