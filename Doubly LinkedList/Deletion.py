class Box:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
      
def findTail(head):
    if head == None:
        return None
    tail = head
    while tail.next != None:
        tail = tail.next
    return tail

def insertAtEnd(head, ele):
    newNode = Box(ele)
    if head == None:
        return newNode
    tail = findTail(head)
    tail.next = newNode
    newNode.prev = tail
    return head

def printLeftToRight(head):
    curr = head
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next
    print()

def printRightToLeft(head):
    tail = findTail(head)
    while tail != None:
        print(tail.data, end = " ")
        tail = tail.prev
    print()

def deleteHeadNode(head):
    if head == None or head.next == None:
        return None
    head = head.next
    head.prev = None
    return head

def deleteTailNode(head):
    if head == None or head.next == None:
        return None
    prev = None
    curr = head
    while curr.next != None:
        prev = curr
        curr = curr.next
    prev.next = None
    return head

def deleteAtSpecificPosition(head, position):
    currInd = 1
    curr = head
    prev = None
    while currInd != position:
        currInd += 1
        prev = curr
        curr = curr.next
    if prev == None:
        head = head.next
        head.prev = None
        return head
    prev.next = curr.next
    if curr.next:
        curr.next.prev = prev
    return head


n = int(input())
l = list(map(int, input().split()))
position = int(input())

head = None
for ele in l:
    head = insertAtEnd(head, ele)

print("Initial list from left to right:")
printLeftToRight(head)
print("Initial list from right to left:")
printRightToLeft(head)

head = deleteHeadNode(head)
print("List after deleting head node from left to right:")
printLeftToRight(head)
print("List after deleting head node from right to left:")
printRightToLeft(head)

head = deleteTailNode(head)
print("List after deleting tail node from left to right:")
printLeftToRight(head)
print("List after deleting tail node from right to left:")
printRightToLeft(head)

head = deleteAtSpecificPosition(head, position)
print(f"List after deleting node at position {position} from left to right:")
printLeftToRight(head)
print(f"List after deleting node at position {position} from right to left:")
printRightToLeft(head)