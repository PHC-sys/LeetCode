# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        
        def get_depth(node):
            while node: # 노드가 null이 아닌 경우
                if not node.left and not node.right: # 단말 노드인 경우
                    return 1
                
                # 자식 노드들의 최고 깊이에 1을 더한 값을 리턴함
                return max(get_depth(node.left), get_depth(node.right)) + 1
            
            return 0 # 노드가 null인 경우에는 0 반환
        
        return get_depth(root)
        