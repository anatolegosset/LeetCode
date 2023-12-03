# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root):
        def parcours(node):
            if node is None:
                return 0, 0, 0
            sum_left, nb_valid_left, nb_nodes_left = parcours(node.left)
            sum_right, nb_valid_right, nb_nodes_right = parcours(node.right)
            new_sum = sum_left + sum_right + node.val
            new_nb_nodes = nb_nodes_left + nb_nodes_right + 1
            return new_sum, nb_valid_left + nb_valid_right + (node.val == new_sum // new_nb_nodes), new_nb_nodes
        return parcours(root)[1]
