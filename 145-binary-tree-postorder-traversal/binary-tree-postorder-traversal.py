# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderHelper(self,node,res):
        if node is not None:
            self.postorderHelper(node.left,res)
            self.postorderHelper(node.right,res)
            res.append(node.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postorderHelper(root,res)
        return res
