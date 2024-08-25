# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderHelper(self,node,res):
        if node is not None:
            self.preorderHelper(node.left,res)
            res.append(node.val)
            self.preorderHelper(node.right,res)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        pre = []
        self.preorderHelper(root,pre)
        sum = 0
        flag = False
        for i in range(len(pre)):
            if pre[i]==low:
                flag =True
            if flag:
                sum+= pre[i]
                if pre[i]==high:
                    break
        return sum


