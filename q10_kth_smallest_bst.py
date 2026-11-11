"""10. Return the k-th smallest BST value."""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def kth_smallest(root, k):
    stack = []
    node = root
    while True:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right


print(kth_smallest(TreeNode(2, TreeNode(1), TreeNode(3)), 2))
