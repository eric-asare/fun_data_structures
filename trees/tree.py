"""
A tree
 - each node has just one parent. A graph could have multiple
 - tree is not cyclic
 - a tree is undirected
All trees are graphs

General Trees have children , can be more than two

Common Trees in Interview: Binary Trees (two children), BST and Trie
"""
# Representation of Binary Trees
# 1. Using a classes
class TreeNode:
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None
    def insert_left(self,node):
        self.left = node
    def insert_right(self, node):
        self.right = node

    def __str__(self) -> str:
        print(self.val)
        if self.left:
            print('<-')
            self.left.__str__()
        if self.right:
            print('->')
            self.right.__str__()
            

"""
Build from ground app

        2
    5       7
        8       9
                    3
"""

three = TreeNode(3)
nine = TreeNode(9)
eight = TreeNode(8)
seven = TreeNode(7)
five = TreeNode(5)
two = TreeNode(2)


nine.insert_right(three)

seven.insert_right(nine)
seven.insert_left(eight)

two.insert_left(five)
two.insert_right(seven)

# two.__str__()

"""
Testing Bubble Up

1. return sum of left and right children as you come up ## Expected 12
2. return sum of left and right children you've seen so far ## Expected :32
3. return sum of left and right children including you - sum of whole tree # Expected: 34
4. depth
5. levels
"""

# 1. is similar to returning the left and right of root - iterative
def shallow(root):
    if not root:
        return 0
    if root.left and not root.right:
        return root.left.val
    elif root.right and not root.left:
        return root.right.val
    else:
        return root.left.val + root.right.val
    
# sum of all nodes bottom up exculing current
def non_cumulative(root):
    if not root:
        return 0
    
    left = non_cumulative(root.left)
    right = non_cumulative(root.right)

    print(left + right)
    return root.val + left + right

# sum of all nodes bottom up
def non_cumulative_sum(root):
    if not root:
        return 0
    left = non_cumulative_sum(root.left)
    right = non_cumulative_sum(root.right)
    return  root.val + left + right

# depth - levels - longest path to any leaf
def depth(root):
    if not root:
        return 0
    left = depth(root.left)
    right = depth(root.right)
    return  1 + max(left, right)

print(non_cumulative(two))
# print(shallow(two))

# 2. Using an array

# Traversal of Trees
# Pre, In, Post - order traversals

