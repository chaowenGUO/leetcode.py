# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterDepth(self, root):
        if not root: return (0,) * 2
        else:
            left, right = map(self.diameterDepth, (root.left, root.right))
            return max(left[0], right[0], left[1] + right[1]), max(left[1], right[1]) + 1
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.diameterDepth(root)[0]
