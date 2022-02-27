from ctypes import sizeof
from typing import Optional

from black import main


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # Second time i did it, 100%
    def inorderSuccessorV2 (self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # InOrder is Left, Node, Right 
        # binary search tree, so left is always smaller than parent, while right is always larger
        
        # define inorderSuccessor returns successorNode of for a given node, if exists 
        # it return null otherwise 
        
        # Base case 
        if (root is None or p is None):
            return None
        
        # If p is in root's right subtree, including the root
        # we know the successor will utimately be root.right (it won't include root)
        if (p.val >= root.val):
            rightSuccessor = self.inorderSuccessor(root.right, p)
            # If not found, then this is the last node
            if (rightSuccessor is None):
                return None
            
            # Found it, we may return here
            return rightSuccessor 
            
        else: # p.val < root.val 
            leftSuccessor = self.inorderSuccessor(root.left, p)
            # Not found, so root is the one after 
            if (leftSuccessor is None):
                return root 
            
            return leftSuccessor 


    def inorderSuccessorInOrder(
        self, root: TreeNode, p: TreeNode
    ) -> Optional[TreeNode]:
        # Python both stack and queue are []
        # exception -> pop() vs pop[0] is queue
        # we'd always use [].append(some_value) to append to the end of the list
        stack = []
        found = False
        # [] is false, so not stack -> not empty
        cur = root
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if found:
                return cur
            if p == cur:
                found = True
            cur = cur.right
        return None

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        """
        inOrder traversal, Left, Node, Right
        if p.val >= root.val (root, and its right of the subtree, but successor, the  root node can be ignored due to inOrder
        if p.val < root.val (left of subtree and root may be successor)
        """
        if root == None or p == None:
            return root

        elif p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        else:  # p.val > root.val
            left = self.inorderSuccessor(root.left, p)
            if left is None:  # root is successor, as its left contains no successor
                return root
            else:
                return left  # found a some left that's not none


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

s = Solution()
print(s.inorderSuccessorInOrder(root, root.left).val)
