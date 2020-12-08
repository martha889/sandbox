class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        element = Node(data)

        if self.root is None:
            self.root = element

        else:
            node = self.root

            while True:
                if node.left is None and element.data < node.data:
                    node.left = element
                    node.left.parent = node
                    break
                elif node.right is None and element.data >= node.data:
                    node.right = element
                    node.right.parent = node
                    break
                else:
                    if element.data >= node.data:
                        node = node.right
                    else:
                        node = node.left

    def search(self, key):
        node = self.root
        found = False

        while True:
            if node.data == key:
                found = True
                break
            else:
                if key > node.data:
                    if node.right is not None:
                        node = node.right
                    else:
                        break
                else:
                    if node.left is not None:
                        node = node.left
                    else:
                        break

        return found

    def print_inorder(self):
        def recursion(node):
            if node is not None:
                recursion(node.left)
                print(node.data, end=" ")
                recursion(node.right)

        recursion(self.root)

    def print_preorder(self):
        def recursion(node):
            if node is not None:
                print(node.data, end=" ")
                recursion(node.left)
                recursion(node.right)

        recursion(self.root)

    def print_postorder(self):
        def recursion(node):
            if node is not None:
                recursion(node.left)
                recursion(node.right)
                print(node.data, end=" ")

        recursion(self.root)


array = [8, 10, 14, 13, 3, 1, 6, 4, 7]

binary_search_tree = BST()

for i in array:
    binary_search_tree.insert(i)

binary_search_tree.print_postorder()



