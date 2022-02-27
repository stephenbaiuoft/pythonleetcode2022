class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        # left, node, right
        rez = []
        stack = []

        cur = root

        while (cur != None or stack):
            while (cur != None):
                stack.append(cur)
                cur = cur.left
            # cur is last in stack now
            cur = stack.pop()
            rez.append(cur.val)

            # now we should go right
            cur = cur.right
        # return stack
        return rez