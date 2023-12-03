# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        result = []
        def parcours(node):
            if node is None:
                result.append(None)
            else:
                result.append(node.val)
                parcours(node.left)
                parcours(node.right)

        parcours(self)
        return result.__repr__()


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        new_root = TreeNode(0)

        def parcours(node, current_node):
            if node is None:
                return current_node
            new_current_node = parcours(node.left, current_node)
            new_current_node.right = TreeNode(node.val)
            return parcours(node.right, new_current_node.right)
        parcours(root, new_root)
        return new_root.right

