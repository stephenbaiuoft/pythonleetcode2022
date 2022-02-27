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
            
            if (cur.left != None):
                s1helper.append(cur.left)
            if (cur.right != None):
                s1helper.append(cur.right)
        
        while (s2):
            # now the order from s2
            cur = s2.pop()
            rez.append(cur.val)
        
        return rez        