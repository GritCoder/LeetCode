# 深搜
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 这个题最妙的地方就是这一句，path += str(root.val)，先拼接成字符串，再转成int，类似于 cur = cur * 10 + root->val
def solution1(root):
    paths = []
    def dfs(root, path=''):
        # 如果根结点不存在，return
        if not root:
            return
        # 否则，记录当前节点的值，添加到path中
        path += str(root.val)
        # 判断左右孩子
        if not root.left and not root.right:
            paths.append(int(path)) # 说明目前有一条路径遍历完了，将值添加到列表中
        # 递归遍历左右孩子
        dfs(root.left, path)
        dfs(root.right, path)
        # 当前的路径走到最深后，需退回一个节点再向其他分支遍历，类似于再去计算其他分支的值的时候，将目前分支的值置空
        path = path[:-1] # 列表切片，不要最后一个元素
    dfs(root)
    return sum(paths)

# 另一种相对简洁的写法
def solution2(root):
    def dfs(root, cur):
        if not root:
            return 0
        cur = cur * 10 + root.val
        if not root.left and not root.right:
            return cur
        return dfs(root.left, cur) + dfs(root.right, cur)
    return dfs(root, 0)
