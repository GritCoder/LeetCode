# 二叉树的结构,类似于C/C++里的struct
from queue import *
class BinTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right

class BinTree:
    def __init__(self, root=None):
        self.root = root
    def initTree(self):
        pass
    def pre_Order(self, tree):
        print(tree.data)
        self.pre_Order(tree.left)
        self.pre_Order(tree.right)
    def in_Order(self, tree): # 递归(栈)比较方便 空间O(n) 时间O(n)
        self.in_Order(tree.left)
        print(tree.data)
        self.in_Order(tree.right)
    def post_Order(self, tree):
        self.post_Order(tree.left)
        self.post_Order(tree.right)
        print(tree.data)
    def layer_Order(self, tree): # 层序用队列比较方便
        q = Queue()
        q.put(tree) # append
        while not q.empty():
            current = q.get() # pop
            print(current.data)
            if current.left:
                q.put(current.left)
            if current.right:
                q.put(current.right)
    def reverse(self, tree): # 递归反转
        if tree:
            tree.left, tree.right = tree.right, tree.left
            self.reverse(tree.left)
            self.reverse(tree.right)

