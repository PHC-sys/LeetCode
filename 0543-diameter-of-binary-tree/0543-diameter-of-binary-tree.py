# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxx =0;
        
        def levels(root):
            if not root: return 0;
            left, right = levels(root.left), levels(root.right)
            self.maxx = max(self.maxx, left+right)
            return 1 + max(left, right)
                # return 0;
        levels(root)
        return self.maxx