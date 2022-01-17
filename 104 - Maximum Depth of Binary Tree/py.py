# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            maxLeft = self.maxDepth(root.left)
            maxRight = self.maxDepth(root.right)
            
            if maxLeft > maxRight:
                return maxLeft  + 1
            else:
                return maxRight + 1