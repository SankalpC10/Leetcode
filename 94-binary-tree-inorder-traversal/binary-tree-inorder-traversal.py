# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrderHelper(self,node,res):
        if node is not None:
            self.inOrderHelper(node.left,res)
            res.append(node.val)
            self.inOrderHelper(node.right,res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inOrderHelper(root,res)
        return res
