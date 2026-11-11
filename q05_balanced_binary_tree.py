"""5. Determine whether a binary tree is height balanced."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def is_balanced(root):
    def height(node):
        if not node:
            return 0
        left, right = height(node.left), height(node.right)
        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) >= 0


print(is_balanced(TreeNode(1)))
