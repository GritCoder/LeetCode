# 如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
# 递归+剪枝
def solution(root):
    def height(node):
        if not node:
            return 0
        left_h = height(node.left)
        if left_h == -1: return -1 # 剪枝
        right_h = height(node.right)
        if right_h == -1: return -1 # 剪枝
        # 如果是平衡的返回树高度,否则返回-1
        return 1 + max(left_h, right_h) if abs(left_h-right_h) <= 1 else -1
    # != -1 说明是平衡的  否则不是
    return height(root) != -1


# 求二叉树高度也可以用层序遍历(BFS) 最后一层的高度即为树深度
def height(root):
    if not root:
        return 0
    queue = [root] # 根结点入队 这里用列表表示队列了
    res = 0
    # 这种写法总是感觉不太自然,知道就行了,跟纯队列一个意思,具体随心
    while queue:
        tmp = []
        for node in queue: # 这里一次完整的循环迭代代表树的一层
            if node.left: tmp.append(node.left)
            if node.right: tmp.append(node.right)
        queue = tmp
        res += 1
    return res
