""""Program to Create a Binary Search Tree from an array"""


class Node:

    def __init__(self, t):
        self.key = t
        self.parent = None
        self.right = None
        self.left = None

    def disconnect(self):
        self.parent = None
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.key)



class BST:
    def __init__(self):
        self.root = None

    def insert(self, t):
        new = Node(t)
        if self.root is None:
            self.root = new
        else:
            hook = self.root
            while True:
                if new.key >= hook.key:
                    if hook.right is None:
                        hook.right = new
                        new.parent = hook
                        break
                    else:
                        hook = hook.right
                else:
                    if hook.left is None:
                        hook.left = new
                        new.parent = hook
                        break
                    else:
                        hook = hook.left

    def find_min(self):
        if self.root is None:
            return -1
        else:
            k = self.root
            while True:
                if k.left is None:
                    return k.key
                else:
                    k = k.left

    def find(self, t):
        if self.root is None:
            return False
        else:
            k = self.root
            while True:
                if t == k.key:
                    return True
                else:
                    if t > k.key:
                        if k.right is not None:
                            k = k.right
                        else:
                            return False
                    else:
                        if k.left is not None:
                            k = k.left
                        else:
                            return False

    def delete_min(self):
        if self.root is None:
            return False
        else:
            node = self.root

            while node.left is not None:
                node = node.left

            if node.parent is not None:
                if node.right is not None:
                    node.parent.left = node.right
                    node.right.parent = node.parent
                else:
                    node.parent.left = None
            else:
                if node.right is not None:
                    node.right.parent = None
                    self.root = node.right

            node.disconnect()

    def __str__(self):
        if self.root is None:
            return "No elements"
        else:
            array = [self.root]
            op = ""

            while len(array):
                op += f'Key: {array[0].key}, Parent:{array[0].parent}, Left Child:{array[0].left}, Right Child {array[0].right} \n'
                if array[0].left is not None:
                    array.append(array[0].left)
                if array[0].right is not None:
                    array.append(array[0].right)
                array.pop(0)

            return op


arr = [3, 7, 2, 4, 6]
tree = BST()

for i in arr:
    tree.insert(i)

for i in range(10):
    print(tree)
    tree.delete_min()