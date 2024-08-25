# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderHelper(self,node,res):
        if node is not None:
            res.append(node.val)
            self.preorderHelper(node.left,res)
            self.preorderHelper(node.right,res)


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.preorderHelper(root,res)
        return res