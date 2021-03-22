class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, TreeNode):
        if TreeNode.root is None:
            return 0
        lheight = self.height(TreeNode.root.left)
        rheight = self.height(TreeNode.root.right)

        ldia = self.diameterOfBinaryTree(TreeNode.root.left)
        rdia = self.diameterOfBinaryTree(TreeNode.root.right)

        return max(lheight + rheight, max(ldia, rdia))

    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


solution = Solution()
solution.diameterOfBinaryTree([1, 2, 3, 4, 5])