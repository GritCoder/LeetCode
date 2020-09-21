class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None
def buildTree(in_, post):
    # 方法 helper 的参数是中序序列中当前子树的左右边界
    def helper(in_left, in_right):
        if in_left > in_right:
            return None
        # 后序中最后一个元素为根结点
        val = post.pop()
        root = TreeNode(val)
        # 求根结点在中序中的索引，当然自己也可以建立一个哈希映射，写个for循环
        index = in_.index(val)
        # 从右子树开始建，因为根结点是post.pop()，一定要对应一致
        root.right = helper(index+1, in_right)
        root.left = helper(in_left, index-1)
        return root
    return helper(0, len(in_) - 1)