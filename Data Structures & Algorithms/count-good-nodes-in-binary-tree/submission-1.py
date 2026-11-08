# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs with 2 params
        # keep track of largest value seen on the path to the node being tested
        # if node.val < max_seen: continue
        # count += 1, update max_seen

        count = 0

        def dfs(node, max_seen):
            nonlocal count
            if not node:
                return

            if node.val >= max_seen:
                max_seen = max(max_seen, node.val)
                count += 1

            dfs(node.left, max_seen)
            dfs(node.right, max_seen)
        
        dfs(root, float('-inf'))
        
        return count
        