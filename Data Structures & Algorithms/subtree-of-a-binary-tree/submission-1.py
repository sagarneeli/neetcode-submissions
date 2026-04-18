# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2 or root1.val != root2.val:
                return False

            left = sameTree(root1.left, root2.left)
            right = sameTree(root1.right, root2.right)

            return left and right

        def dfs(node):
            if not node:
                return False
            
            if sameTree(node, subRoot):
                return True
            
            left = dfs(node.left)
            right = dfs(node.right)

            return left or right
        
        return dfs(root)
        