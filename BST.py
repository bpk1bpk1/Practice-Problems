class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def search(root,key):
    if root.val == key or root == None:
        return root
    if root.val < key:
        return search(root.right,key)
    if(root.val > key):
        return search(root.left,key)


def insert(root,node):
    if root == None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

root = Node(50)
node = Node(30)
insert(root,node)
insert(root,Node(20))
insert(root,Node(40))
insert(root,Node(70))
insert(root,Node(60))
insert(root,Node(80))
(search(root,40))
