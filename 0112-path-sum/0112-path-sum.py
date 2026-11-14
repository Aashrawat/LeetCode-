# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        stack = [(root, root.val)]

        while stack:
            node, total = stack.pop()

            if node.left is None and node.right is None:
                if total == targetSum:
                    return True

            if node.left:
                stack.append((node.left, total + node.left.val))

            if node.right:
                stack.append((node.right, total + node.right.val))

        return False