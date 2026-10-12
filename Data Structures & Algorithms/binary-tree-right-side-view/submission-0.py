# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            rsv = None
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rsv = node
                    q.append(node.left)
                    q.append(node.right)
            if rsv: res.append(rsv.val)    
        return res
                