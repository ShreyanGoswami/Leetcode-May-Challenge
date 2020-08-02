# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = []
        
        def inorder(node, arr):
            if node is None:
                return
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)
        
        inorder(root, arr)
        return arr[k-1]