# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return true
        return self.isSame(root.left, root.right)
    def isSame(self, leftroot, rightroot) -> bool:
        if leftroot == None and rightroot == None:
            return True
        if leftroot == None or rightroot == None or self == None:
            return False
        if leftroot.val != rightroot.val:
            return False
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)
        