# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:

# Input: root = [1]
# Output: [[1]]

# Example 3:

# Input: root = []
# Output: []

# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        deq = [root]
        res = []

        if not root:
            return []
        
        while(deq):
            level_size = len(deq)
            current_level = []

            for _ in range(level_size):
                node = deq[0]
                deq.pop(0)
                current_level.append(node.val)

                if(node.left):
                    deq.append(node.left)
                if(node.right):
                    deq.append(node.right)
            res.append(current_level)
        return res