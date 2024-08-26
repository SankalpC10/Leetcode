"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorderHelper(self,node,res):
        if node is not None:
            for i in node.children:
                self.postorderHelper(i,res)
            res.append(node.val)


    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.postorderHelper(root,res)
        return res