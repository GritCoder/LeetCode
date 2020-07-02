class BinTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
class Solution:
    def buildTree(self, preOrder, inOrder):
        self.dic, self.pre = {}, preOrder
        for i in range(len(inOrder)): # 建立哈希映射(字典)
            self.dic[inOrder[i]] = i
        self.recur(0, 0, len(inOrder)-1)
    # 理解三个参数的含义，先序中根结点索引，中序的左右子树边界
    def recur(self, pre_root, in_lchild, in_rchild): # 注意参数都是对应的索引值
        if in_lchild > in_rchild:
            return
        root = BinTreeNode(self.pre[pre_root]) # 建立当前子树的根结点
        i = self.dic[self.pre[pre_root]] # 获取先序在中序中的索引
        root.left = self.recur(pre_root+1, in_lchild, i-1)
        # (i - in_lchild)为左子树长度
        root.right = self.recur(i - in_lchild + pre_root + 1, i+1, in_rchild)
        return root
