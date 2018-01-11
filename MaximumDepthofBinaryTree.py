# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth=0
        stack1=[]
        stack2=[root]
        if root==None:
            return 0
        while stack2!=[]:
            depth+=1
            stack1,stack2=stack2,[]
            for node in stack1:
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
        return depth
