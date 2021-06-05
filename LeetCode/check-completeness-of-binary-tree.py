# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        def dfs(node, d):
            nonlocal depth, flag
            
            if not node:
                if d > depth:
                    depth = -1
                elif d < depth:
                    flag -= 1
                    if flag == 0:
                        depth = -1
                    else:
                        depth = d
                    
                return 
            
            left_node, right_node = node.left, node.right
            dfs(left_node, d+1)
            dfs(right_node, d+1)
                
        flag = 3
        depth = sys.maxsize
        dfs(root, 0)
        
        if depth == -1:
            return False
        return True
        