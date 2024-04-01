# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        bfs,s = [root],list();
        
        for i in bfs: 
            if i.left: bfs.append(i.left);
            if i.right: bfs.append(i.right);
            s.append(i.val)
        # print(len(s))    
        # def dfs(node, l=[]):
        #     if node.left: dfs(node.left, l)
        #     l.append(node.val)
        #     if node.right: dfs(node.right, l)
        #     return l
        # l = dfs(root)
        s.sort()
        # l.sort()
        #min_diff2 = min([abs(a-b) for a,b in zip(l, l[1:])])
        min_diff = min([abs(a-b) for a,b in zip(s, s[1:])])
        #print(min_diff2,min_diff)                         
        return min_diff
                    