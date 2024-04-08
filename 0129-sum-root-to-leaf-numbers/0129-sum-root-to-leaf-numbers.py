# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node, q):
            if not node: return
            traverse(node.left, q + [str(node.val)])
            traverse(node.right, q + [str(node.val)]) 
            if not node.left and not node.right: res[0] += int("".join(q + [str(node.val)]))
        res = [0]
        traverse(root, [])
        return res[0]