# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderHelper(self,node,res):
        if node is not None:
            self.inorderHelper(node.left, res)
            res.append(node.val)
            self.inorderHelper(node.right,res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorderHelper(root,res)
        return res
