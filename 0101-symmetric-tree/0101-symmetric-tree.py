# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: #루트가 없으면 True 반환
            return True
        return self.check(root.left, root.right) #루트의 좌우 값 비교
        
    def check(self, left, right):
        if left is None and right is None: #좌우 둘다 없으면 True
            return True
        if left is None or right is None:  #좌우 중 하나 없으면 False
            return False
        if left.val != right.val:  #좌우 값이 다르면 False
            return False
        a = self.check(left.left, right.right) #좌의 좌 값, 우의 우 값 비교
        b = self.check(left.right, right.left) #좌의 우값, 우의 좌 값 비교
        return a and b
            