"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: Node) -> int:
        return max(map(self.maxDepth, root.children), default = 0) + 1 if root else 0
