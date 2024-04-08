# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = [root]
        q = [root]
        while any(q):
            tmp = []
            for node in q:
                if node.right:
                    res.insert(res.index(node) + 1, node.right)
                    tmp.append(node.right)
                if node.left:
                    res.insert(res.index(node) + 1, node.left)
                    tmp.insert(-1, node.left)
            q = tmp
        return [j.val for j in res if j]