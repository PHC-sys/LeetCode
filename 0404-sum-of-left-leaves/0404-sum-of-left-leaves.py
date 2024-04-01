# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        l = [];
        def warpper(root,l=[]):
            if not root:
                return;
            if root.left and not root.left.left and not root.left.right:
                l.append(root.left.val) 
                warpper(root.left,l)
            elif root.left:
                warpper(root.left,l)
            if root.right:
                warpper(root.right,l)
        warpper(root,l);
        return sum(l) 