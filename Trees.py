class Box:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printInOrderTraversal(root):
    if root is None:
        return
    printInOrderTraversal(root.left)
    print(root.data, end=" ")
    printInOrderTraversal(root.right)

def printPreOrderTraversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    printPreOrderTraversal(root.left)
    printPreOrderTraversal(root.right)

def printPostOrderTraversal(root):
    if root is None:
        return
    printPostOrderTraversal(root.left)
    printPostOrderTraversal(root.right)
    print(root.data, end=" ")

def levelOrderTraversal(root):
    if root is None:
        return
    result = []
    Q = [root]

    while Q:
        n = len(Q)
        subResult = []
        for i in range(n):
            currNode = Q.pop(0)
            subResult.append(currNode.data)
            if currNode.left is not None:
                Q.append(currNode.left)
            if currNode.right is not None:
                Q.append(currNode.right)
        result.append(subResult)
    
    for level in result:
        print(level, end=" ")

def zigzagLevelOrder(root):
    if root is None:
        return []
    
    result = []
    queue = [root]
    level = 0
    
    while queue:
        sublist = []
        n = len(queue)
        
        for i in range(n):
            currnode = queue.pop(0)
            sublist.append(currnode.data)
            
            if currnode.left:
                queue.append(currnode.left)
            if currnode.right:
                queue.append(currnode.right)
                
        if level % 2 == 1:
            sublist.reverse()
            
        result.append(sublist)
        level += 1
    
    return result

def isLeafNode(root):
    return root.left is None and root.right is None

def collectLeftView(root, result):
    if root is None:
        return
    while root is not None and not isLeafNode(root):
        result.append(root.data)
        if root.left is not None:
            root = root.left
        else:
            root = root.right

def collectLeafNodes(root, result):
    if root is None:
        return
    if isLeafNode(root):
        result.append(root.data)
        return
    collectLeafNodes(root.left, result)
    collectLeafNodes(root.right, result)

def collectRightViewInReverseFashion(root, result):
    if root is None:
        return
    temp = []
    while root is not None and not isLeafNode(root):
        temp.append(root.data)
        if root.right is not None:
            root = root.right
        else:
            root = root.left
    temp.reverse()
    for ele in temp:
        result.append(ele)

def topViewHelper(root, store, hd, level):
    if root is None:
        return

    if hd not in store or store[hd][0] > level:
        store[hd] = [level, root.data]

    topViewHelper(root.left, store, hd - 1, level + 1)
    topViewHelper(root.right, store, hd + 1, level + 1)

def topView(root):
    result = []
    if root is None:
        return result

    store = {}
    topViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    return result

def bottomViewHelper(root, store, hd, level):
    if root is None:
        return

    if hd not in store or store[hd][0] < level:
        store[hd] = [level, root.data]

    bottomViewHelper(root.left, store, hd - 1, level + 1)
    bottomViewHelper(root.right, store, hd + 1, level + 1)

def bottomView(root):
    result = []
    if root is None:
        return result

    store = {}
    bottomViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    return result

def findBoundaryTraversal(root):
    if root is None:
        return []
    result = []
    result.append(root.data)

    collectLeftView(root.left, result)
    collectLeafNodes(root, result)
    collectRightViewInReverseFashion(root.right, result)
    return result

def LeftView(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        n = len(queue)
        for i in range(n):
            curr = queue.pop(0)
            if i == 0:
                result.append(curr.data)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
    return result

def rightSideView(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        n = len(queue)
        for i in range(n):
            curr = queue.pop(0)
            if i == n - 1:
                result.append(curr.data)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
    return result

# objects creation
obj1 = Box(10)
obj2 = Box(20)
obj3 = Box(30)
obj4 = Box(40)
obj5 = Box(50)
obj6 = Box(60)
obj7 = Box(70)
obj8 = Box(90)
obj9 = Box(100)
obj10 = Box(-40)

# establishing links among those nodes
obj1.left = obj2    #   10
obj1.right = obj3   #  /  \
obj2.left = obj4 #    20   30
obj2.right = obj5#   / \   / \
obj3.right = obj6#  40 50 70 60
obj3.left = obj7 #  \  / \
obj4.right = obj8 # 90 100 -40
obj5.left = obj9
obj5.right = obj10

# Function calls
print("InOrder Traversal:")
printInOrderTraversal(obj1)
print()

print("PreOrder Traversal:")
printPreOrderTraversal(obj1)
print()

print("PostOrder Traversal:")
printPostOrderTraversal(obj1)
print()

print("Level Order Traversal:")
levelOrderTraversal(obj1)
print()

print("Zigzag Level Order Traversal:")
print(zigzagLevelOrder(obj1))
print()

print("Top View:")
print(topView(obj1))
print()

print("Bottom View:")
print(bottomView(obj1))
print()

print("Boundary Traversal:")
print(findBoundaryTraversal(obj1))
print()

print("Left View:")
print(LeftView(obj1))
print()

print("Right Side View:")
print(rightSideView(obj1))
print()
