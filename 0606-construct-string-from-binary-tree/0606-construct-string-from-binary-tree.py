# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def warp(t):
            """
            :type t: TreeNode
            :rtype: str
            """ 
            if t:
                #need to consider if left is none and right is not none.
                if t.left==None and t.right != None:
                    return "("+str(t.val)+"()"+warp(t.right)+")"
                return "("+str(t.val)+warp(t.left)+warp(t.right)+")"
            else:
                return ""
        return warp(root)[1:-1]