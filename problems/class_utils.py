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