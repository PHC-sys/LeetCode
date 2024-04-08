# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        t0 = root1;
        
        if not root1 and not root2:  # if dont have any child.
            return None;
        elif not root2:  # if only t1. 
            t0.val = root1.val; 
        elif not root1: # if ouly t2.
            t0 = root2;
            t0.val = root2.val;
        else: #both
            t0.val = root1.val + root2.val;
            t0.left = self.mergeTrees(root1.left,root2.left);
            t0.right = self.mergeTrees(root1.right,root2.right);
        
        return t0;