from queue import *
class BinTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
# 设两个队列，s1存放奇数层，s2存放偶数层
# 遍历s1节点的同时按照右子树、左子树的顺序加入s2，
# 遍历s2节点的同时按照左子树、右子树的顺序加入s1
def printTree(tree):  # 层序用队列比较方便
    flag = 1 # 当前层
    q1 = Queue()
    q2 = Queue()
    if not tree: return
    q1.put(tree)
    while not q1.empty() or not q2.empty():
        if flag % 2 != 0:
            while not q1.empty():
                current = q1.get()  # pop
                print(current.data)
                if current.right:
                    q2.put(current.right)
                if current.left:
                    q2.put(current.left)

        if flag % 2 == 0:
            while not q2.empty():
                current = q2.get()
                print(current.data)
                if current.left:
                    q1.put(current.left)
                if current.right:
                    q1.put(current.right)

        flag += 1

