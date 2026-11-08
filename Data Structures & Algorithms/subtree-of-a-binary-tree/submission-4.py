# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same_tree(node, subroot):
            if not node and not subroot:
                return True
            if node and not subroot:
                return False
            if not node and subroot:
                return False
            if node.val != subroot.val:
                return False
            
            left_same = same_tree(node.left, subroot.left)
            right_same = same_tree(node.right, subroot.right)

            return left_same and right_same
        
        def dfs(node):
            if not node:
                return False

            is_same = same_tree(node, subRoot)

            if is_same:
                return True

            left = dfs(node.left)
            right = dfs(node.right)

            return left or right
        
        return dfs(root)



            
