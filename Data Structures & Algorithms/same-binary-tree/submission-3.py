# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        q1 = deque()
        q2 = deque()

        q1.append(p)
        q2.append(q)

        while q1 or q2:
            if len(q1) != len(q2):
                return False
            
            for _ in range(len(q1)):
                n1 = q1.popleft()
                n2 = q2.popleft()

                if not n1 and n2:
                    return False
                if not n2 and n1: 
                    return False
                if not n1 and not n2:
                    continue
                if n1.val != n2.val:
                    return False
                
                q1.append(n1.left)
                q1.append(n1.right)
                q2.append(n2.left)
                q2.append(n2.right)

        return True
                
                


