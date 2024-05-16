# 2331. Evaluate Boolean Binary Tree
# https://leetcode.com/problems/evaluate-boolean-binary-tree/description/
# 16-0-5-2024
# Category: easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def operation(node):
            if not node.left and not node.right:
                return node.val
            else:
                op = node.val

                if op==2:
                    return operation(node.left) or operation(node.right)
                elif op == 3:
                    return operation(node.left) and operation(node.right)
        return operation(root)