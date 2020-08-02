# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def traverse(index, preorder, limit):
            if index[0] == len(preorder) or preorder[index[0]] > limit:
                return None
            
            node = TreeNode(preorder[index[0]])
            index[0]+=1
            node.left = traverse(index, preorder, node.val)
            node.right = traverse(index, preorder, limit)
            return node
            
        return traverse([0], preorder, 100000001)