class binTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 根据先序建立BST树 利用二叉搜索树的性质  左 < 根 < 右 递归建树
# 另外一种思路，先序从小到大排序后，即为BST树的中序，然后利用先中序列建树
# 本质也是利用了BST树的性质
def createTree(preOrder):
    def helper(lower=float('-inf'), upper=float('inf')):
        # global 表示将变量声明为全局变量
        # nonlocal 表示将变量声明为外层变量（外层函数的局部变量，而且不能是全局变量）
        nonlocal idx
        if idx == n: # 说明树已经构建完毕
            return None
        val = preOrder[idx]
        if val < lower or val > upper:
            return None
        idx += 1
        root = binTree(val)
        root.left = helper(lower, val)
        root.right = helper(val, upper)
        return root
    idx = 0
    n = len(preOrder)
    return helper()
T = createTree([8,5,1,7,10,12])
# 验证
# def preOrder(T):
#     if not T:
#         return None
#     print(T.val)
#     preOrder(T.left)
#     preOrder(T.right)
# preOrder(T)
# 只根据先序建树,其实框架跟上面的差不多,几乎一样

# 深度优先搜索遍历二叉树(其实本质上树的dfs就是先序遍历)
# def dfs(T, result):
#     if T == None:
#         return
#     result.append(T.val)
#     dfs(T.left, result)
#     dfs(T.right, result)
#     return result
# print(dfs(T, []))

# bfs 广度优先遍历二叉树(本质上就是层序遍历)
from queue import *
def bfs(T, result):
    if not T:
        return None
    q = Queue()
    q.put(T)
    while not q.empty():
        T = q.get()
        # print(T.val)
        result.append(T.val)
        if T.left:
            q.put(T.left)
        if T.right:
            q.put(T.right)
    return result
# 若让你返回其节点值自底向上的层次遍历
# 反转一下结果即可 reverse(result)
print(bfs(T, []))


