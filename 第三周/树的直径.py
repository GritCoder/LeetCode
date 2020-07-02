# 两节点之间的路径长度是他们之间的节点数目
# 树的直径是两节点间的最大路径长度
# 每个节点的最长路径的计算方法为 左右子树高度之和

def solution(root):
    def height(node):
        res = 0
        if not node:
            return 0
        left_h = height(node.left)
        right_h = height(node.right)
        res = max(res, left_h+right_h) # 即树的直径问题转化为求最大的左右子树高度和
        return res
        # return 1 + max(left_h, right_h) # 这个返回的是树的高度
    res = height(root)
    return res