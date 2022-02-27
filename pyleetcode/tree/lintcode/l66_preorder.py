# https://www.lintcode.com/problem/66/


from typing import List
from pyleetcode.tree.node import TreeNode


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        # node, left, right
        stack = []
        rez = []
        if (root == None):
            return []
        stack.append(root)

        while (stack):
            cur = stack.pop()
            # do what you want here
            rez.append(cur.val)

            if (cur.right != None):
                stack.append(cur.right)
            if (cur.left != None):
                stack.append(cur.left)
        
        return rez
