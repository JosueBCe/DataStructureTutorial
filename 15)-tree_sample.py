# TODO: Things to remember:
# We are using recursion to perform the insert operation
# We also will use recursion to perform the other operations like removing,
# checking if an element exists in the tree, etc.

class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Tree.Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Tree.Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Tree.Node(data)
            else:
                self._insert_recursive(node.right, data)
    def __iter__(self):
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
            
# Try uncommeting the following 2 lines
#my_tree = Tree()
#my_tree.insert(100)

# Expected output: 100
# try uncommeting the following 2 lines
# for num in my_tree .__iter__(): 
#     print("{}".format(num))