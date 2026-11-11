class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def traverse(node):
            if node is None:
                return

            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

        traverse(root)
        return result