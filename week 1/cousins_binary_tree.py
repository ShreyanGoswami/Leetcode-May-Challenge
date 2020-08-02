In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        from collections import deque as dq
        
        q = dq()
        q.append(root)
        
        while len(q) > 0:
            n = len(q)
            temp = []
            for i in range(n):
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left is not None:
                    if curr.right is not None:
                        if (x == curr.left.val or y == curr.left.val) and (x == curr.right.val or y == curr.right.val):
                            return False
                        q.append(curr.left)
                        q.append(curr.right)
                    else:
                        q.append(curr.left)
                else:
                    if curr.right is not None:
                        q.append(curr.right)
            if x in temp and y in temp:
                return True
        return False