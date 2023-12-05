""" TODO: Solve the following excercises 
let's go 🌳⛏️🌲⚒️!
"""


class Tree:
    """ A tree is a widely used data structure in computer science that represents a hierarchical structure. 
    It consists of nodes connected by edges, where each node can have zero or more child nodes. 
    """
    class Node:

        """The top node of the tree is called the root, 
        and every other node is a descendant of the root. """

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """ Initialize the tree. """
        self.root = None

    # TODO: EXCERCISE 1
    def insert(self, data):
        """ It performs a node insertion """
        # Base case
        if self.root is None:
            self.root = Tree.Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """ Go through the nodes and insert the new node
        where it belongs. """
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

    # Normal interation
    def _traverse_forward(self, node):
        """ Iterates through the tree """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def __iter__(self):
        yield from self._traverse_forward(self.root)

   # TODO: EXCERCISE 2
    def _traverse_backward(self, node):
        """ Iterates through the tree recursively reversily. """
        # TODO: how to traverse backwards if we traversed forward?
        pass

    def __reversed__(self):
        yield from self._traverse_backward(self.root)

    # TODO: EXCERCISE 3
    def size(self):
        """ Check the size of a tree """
        return self._size_recursive(self.root)

    def _size_recursive(self, node):
        """ Recursivly goes through the nodes and checks the tree size """

        if node is None:
            return 0
        else:
            # TODO: how to check the size of a tree?
            # PRO tip: remember that you need to count to the
            # root and the left and right side of the tree
            pass

    # TODO: EXCERCISE 4
    def contains(self, node):
        """ Checks if value is in the tree """
        # TODO: how to check if a value is in the tree?
        pass

    def _contains_recursive(self, node, value):
        """ Recursively checks if value is in the tree """

        if node is None:
            pass
        # TODO: how to check if a value is in the tree?
        # PRO tip: remember that you need check the value with the node
        # and go through the nodes checking to the right side and the left side


my_tree = Tree()
# EXCERCISE 1
print("===== EXCERCISE 1 =====")
my_tree.insert(100)
my_tree.insert(200)
my_tree.insert(400)
# Expected output: 100, 200, 400
for num in my_tree:
    print(num)

print("===== EXCERCISE 2 =====")
# EXCERCISE 2
# Print the nodes in reverse order:
# Expected output: 400, 200, 100
for num in reversed(my_tree):
    print(num)

print("===== EXCERCISE 3 =====")
# TODO: EXCERCISE 3
num_being_checked = 10
num_being_checked_2 = 200
# Expected output: 3
print(my_tree.size())

print("===== EXCERCISE 4 =====")
# TODO: EXCERCISE 4

print(my_tree.contains(num_being_checked))  # False
print(my_tree.contains(num_being_checked_2))  # True
