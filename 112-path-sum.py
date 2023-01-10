class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            if targetSum == root.val:
                return True
        return self.hasPathSum(root.left, targetSum - root.val) | self.hasPathSum(root.right, targetSum - root.val)
