class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order(node):
    if node is None:
        return []
    res = [node.data]
    if node.left:
        res += pre_order(node.left)
    if node.right:
        res += pre_order(node.right)
    return res

# In-order traversal
def in_order(node):
    res = []
    if node is None:
        return []
    if node.left:
        res += in_order(node.left)
    res.append(node.data)
    if node.right:
        res += in_order(node.right)
    return res

# Post-order traversal
def post_order(node):
    res = []
    if node is None:
        return []
    if node.left:
        res += post_order(node.left)
    if node.right:
        res += post_order(node.right)
    res.append(node.data)
    return res



a = Node("A")
b = Node("B")
c = Node("C")
  
a.left = b
a.right = c

print(pre_order(a))
print(in_order(a))
print(post_order(a))