# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        # helper参数为子树在中序中的边界(左右索引)
        def helper(in_left, in_right): # 注意参数都是对应的索引值
            if in_left > in_right:
                return None
            # 先序中第一个元素值为根
            val = preorder.pop(0)
            root = TreeNode(val)
            # 求根索引
            index = inorder.index(val)
            # 递归建树
            root.left = helper(in_left, index-1)
            root.right = helper(index+1, in_right)
            return root
        return helper(0, len(inorder)-1)