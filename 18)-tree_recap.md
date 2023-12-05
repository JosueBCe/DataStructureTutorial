# Tree Concepts Recap  🌳🌲🌴🎄 
A tree is a widely used data structure that represents a hierarchical structure.

## Basic Terminology

- **Node**: Each element in a tree is called a node. It contains data and references to its child nodes.
- **Root**: The topmost node in a tree. It does not have any parent nodes.
- **Child**: A node directly connected to another node when moving away from the root.
- **Parent**: A node directly connected to another node when moving towards the root.
- **Siblings**: Nodes that share the same parent.
- **Leaf**: A node that does not have any child nodes.
- **Edge**: The connection between two nodes in a tree.

## Binary Tree
A binary tree is a special type of tree where each node has at most two child nodes: a left child and a right child.

## Tree Traversal

Tree traversal refers to the process of visiting each node in a tree in a specific order. There are several common traversal methods:
- **Pre-order traversal**: Visits the root node, then the left subtree, and finally the right subtree.
- **In-order traversal**: Visits the left subtree, then the root node, and finally the right subtree. In a binary search tree, an in-order traversal will result in nodes being visited in ascending order.
- **Post-order traversal**: Visits the left subtree, then the right subtree, and finally the root node.
- **Level-order traversal**: Visits the nodes at each level from left to right, starting from the root.

## Binary Search Tree (BST)

A binary search tree is a type of binary tree in which the nodes are ordered based on their values. For any node in the tree, all nodes in its left subtree have values less than the node's value, and all nodes in its right subtree have values greater than the node's value. This property allows for efficient searching, insertion, and removal of nodes.

## Common Operations

- **Insertion**: Adds a new node to the tree while maintaining the ordering property.
- **Deletion**: Removes a node from the tree while preserving the binary search tree property.
- **Search**: Determines whether a given value is present in the tree.
- **Traversal**: Visits all the nodes in the tree in a specific order.
- **Size**: Calculates the number of nodes in the tree.

## Conclusion
Understanding the basic concepts, such as nodes, edges, traversal methods, and binary search trees, enables effective manipulation and analysis of tree structures.