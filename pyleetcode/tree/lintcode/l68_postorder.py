class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        # left, right, node
        s1helper = []
        s2 = []
        rez = []
        cur = root

        if (cur == None):
            return []
        
        s1helper.append(cur)
        # use s1helper to get the list order
        while (s1helper):
            cur = s1helper.pop()
            s2.append(cur)
            
            # This is s1helper order, left, right
            # So when it reaches s2, then it'd be right, left, node(remember node goes in s2)
            if (cur.left != None):
                s1helper.append(cur.left)
            if (cur.right != None):
                s1helper.append(cur.right)
        
        while (s2):
            # now the order from s2
            cur = s2.pop()
            rez.append(cur.val)
        
        return rez