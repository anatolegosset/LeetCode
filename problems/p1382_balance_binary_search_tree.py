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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        tree_array = []

        def parcours1(node: TreeNode):
            if node is None:
                pass
            else:
                parcours1(node.left)
                tree_array.append(node.val)
                parcours1(node.right)

        parcours1(root)

        def parcours2(start, end):
            if start == end:
                return None
            if start + 1 == end:
                return TreeNode(val=tree_array[start])
            else:
                mid = (start + end) // 2
                return TreeNode(val=tree_array[mid], left=parcours2(start, mid), right=parcours2(mid+1, end))
        return parcours2(0, len(tree_array))
