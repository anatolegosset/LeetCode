from problems.class_utils import TreeNode


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def parcours(node):
            if node is None:
                return 0, float('-inf'), float('inf'), float('-inf'), True
            left_sum, left_max_sum, left_min, left_max, is_left_bst = parcours(node.left)
            right_sum, right_max_sum, right_min, right_max, is_right_bst = parcours(node.right)
            if is_left_bst and is_right_bst and left_max < node.val < right_min:
                return left_sum + right_sum + node.val, max(0, left_max_sum, right_max_sum, left_sum + right_sum + node.val), min(left_min, node.val), max(right_max, node.val), True
            else:
                return 0, max(left_max_sum, right_max_sum), min(left_min, node.val, right_min), max(left_max, node.val, right_max), False

        return parcours(root)[1]
