"""
Binary Search Tree
- values in the left subtree are less than the root value
- values in the right subtree are greater than the root value

- rightmost node is the greatest element in the tree
- leftmost node is the smallest element in the tree

operations: init, insert, remove, search for val, inorder traversal, pre-order traversal, post-order traversal

tricky to write: remove function 
"""

class TreeNode:
    def __init__(self, value, left = None, right = None) -> None:
        self.val = value 
        self.left = left
        self.right = right

class BST:
    def __init__(self, val) -> None:
        self.root = TreeNode(val)

    def insert(self,val) -> None:
        curr = self.root
        parent = curr
        while curr:
            parent = curr
            if curr.val < val:
                curr = curr.right
            else:
                curr = curr.left

        node = TreeNode(val)
        if val > parent.val:
            parent.right = node
        else:
            parent.left = node

    def remove(self, val):
        """
        - if target node does not exist - ignore
        - if target is leaf - set it to None
        - if target has a right subtree, replace it with smallest in rightsubtree and set smallest to None
        - else: replace with biggest in left subtree and set it to none
        """
        parent = None
        curr = self.root
        while curr and curr.val != val:
            parent = curr
            if val > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        # target does not exist
        if curr is None:
            return
        # target is leaf node
        if not curr.right and not curr.left:
            if curr.val > parent.val:
                parent.right = None
            else:
                parent.left = None
            return

        # target has right tree
        target = curr
        if target.right:
            parent = target
            target = target.right
            while target.left:
                parent = target
                target = target.left
            curr.val = target.val
            parent.left = None
        else:
            # find max on left subtree
            target = curr
            parent = target
            target = target.left
            while target.right:
                parent = target
                target = target.right
            curr.val = target.val
            parent.right = None


    def search(self, val) -> bool:
        curr = self.root
        while curr:
            if val == curr.val:
                return True
            elif val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        return False


    def inorder(self, node):
        if not node:
            return 
        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)


    def preorder(self, node):
        if not node:
            return 
        print(node.val)
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if not node:
            return 
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val)

"""
TESTING
"""
bst = BST(6)
bst.insert(4)
bst.insert(11)
bst.insert(8)
bst.insert(3)
bst.insert(1)
bst.insert(5)

print('search for 5 - true:', bst.search(5))
print('search for 9- false:', bst.search(9))

bst.remove(6)

bst.inorder(bst.root)
print("-----")
bst.preorder(bst.root)
print("-----")
bst.postorder(bst.root)