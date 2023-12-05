# Tree 🌲

A tree is a widely used data structure in computer science that represents a hierarchical structure. It consists of nodes connected by edges, where each node can have zero or more child nodes. The top node of the tree is called the root, and every other node is a descendant of the root.

Trees are used to represent hierarchical relationships, such as file systems, organization charts, and family trees.

Here are some facts and examples:

- Nodes with no child nodes are called leaf nodes.
- Nodes with at least one child node are called internal nodes.
- The height of a tree is determined by the longest path from the root to a leaf node.

Here's an example of how a tree can be represented visually:

```
       A
     / | \
    B  C  D
   / \    |
  E   F   G
```

The height of this tree is **2**.

Tree traversal refers to the process of visiting each node in a tree data structure. There are several methods to traverse a tree, including depth-first traversal (pre-order, in-order, and post-order) and breadth-first traversal.

Here's an example of a recursive algorithm to traverse a tree in pre-order:

```python
def _traverse_forward(node):
    if node is None:
        return

    # Process the current node
    # ...

    # Recursively traverse the left subtree
    _traverse_forward(node.left)

    # Recursively traverse the right subtree
    _traverse_forward(node.right)
```

In this algorithm, the `_traverse_forward` function takes a node as input and performs the following steps:

1. If the node is `None`, which represents an empty subtree, the function returns.
2. The function processes the current node.
3. The function recursively traverses the left subtree by calling `_traverse_forward` on the left child node.
4. The function recursively traverses the right subtree by calling `_traverse_forward` on the right child node.

By using recursion, the algorithm can traverse the tree in a pre-order fashion, visiting the nodes in the desired order.


### Operations 
Let's work with a class that implements a Node
```python
    class Node:
            """
            Each node of the BST will have data and links to the 
            left and right sub-tree. 
            """

            def __init__(self, data):
                """ 
                Initialize the node to the data provided.  Initially
                the links are unknown so they are set to None.
                """
        
                self.data = data
                self.left = None
                self.right = None
```

#### Insert(value) 
    ```python
    def insert(root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = insert(root.left, data)
            else:
                root.right = insert(root.right, data)
        return root
    ```

#### Remove (value)
    ```python
    def find_min_value_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = remove(root.left, data)
        elif data > root.data:
            root.right = remove(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = find_min_value_node(root.right)
            root.data = temp.data
            root.right = remove(root.right, temp.data)
        return root
    ```

#### Contains (value)
  ```python
    def contains(root, data):
        if root is None:
            return False
        if data == root.data:
            return True
        elif data < root.data:
            return contains(root.left, data)
        else:
            return contains(root.right, data)
```

#### Traverse_forward
```python


        def __init__(self):
            """
            Initialize an empty Tree.
            """
            self.root = None

        def _traverse_forward(self, node):
            if node is not None:
                yield from self._traverse_forward(node.left)
                yield node.data
                yield from self._traverse_forward(node.right)
```

#### Height(node)
```python
    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  

    def _get_height(self, node):
        if node is None:
            return 0 
        else: 
            return 1 + max(self._get_height(node.left), self._get_height(node.right))
```

#### Size
```python
    def get_size(root):
        if root is None:
        return 0
    else:
        left_size = get_size(root.left)
        right_size = get_size(root.right)
        return left_size + right_size + 1
```
    
#### Empty
```python

def is_empty(root):
    return root is None
```
