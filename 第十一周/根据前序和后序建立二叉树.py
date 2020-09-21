class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None
def solution(pre, post):
    # 注意先后序列建树与前中和后中不太一样，理解并明白
    def helper(pre, post):
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        L = post.index(pre[1]) + 1 # +1 表示左子树结点个数，否则的话表示的是索引
        root.left = helper(pre[1:L+1], post[:L])
        root.right = helper(pre[L+1:], post[L:-1])
        return root
    return helper(pre, post)