# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result, level = [], [root]
        while root and level:
            result += level[-1].val,
            level = [child for node in level for child in (node.left, node.right) if child]
        return result
