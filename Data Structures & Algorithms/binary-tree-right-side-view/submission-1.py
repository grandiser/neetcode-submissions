# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # always see the root
        # go level by level (bfs)
        # level = []
        # append to that
        # take level[-1]

        # answer = []
        # queue(root)
        # while queue:
            # level = []
            # for _ in range(queue)
                # popleft
                # add to level if not null
            # answer.append(level[-1])
        
        answer = []
        queue = deque()
        queue.append(root)

        # 4 null null null
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

            if level:
                answer.append(level[-1])
        
        return answer
        