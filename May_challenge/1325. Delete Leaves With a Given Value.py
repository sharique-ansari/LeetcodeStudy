# 1325. Delete Leaves With a Given Value
# https://leetcode.com/problems/delete-leaves-with-a-given-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #
        def rec_del(node):
            if not node:
                return None
            if node.right:
                node.right = rec_del(node.right)
            if node.left:
                node.left = rec_del(node.left)
            if not node.left and not node.right and node.val == target:
                return None
            return node

        return rec_del(root)