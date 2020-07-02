# 二叉树两节点距离是指从一个节点到达另一个节点需要的最少边数
class BinTree:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
# 最小公共祖先
def findLCA(root, n1, n2):
    if not root: return
    # n1 or n2 有一个是根结点
    if root.val == n1 or root.val == n2:
        return root
    # 去左子树找LCA
    left_lca = findLCA(root.left, n1, n2)
    # 去右子树找LCA
    right_lca = findLCA(root.right, n1, n2)
    # 如果两个树上都能找到，则LCA必为根结点(因为根结点是唯一的交集)
    if left_lca and right_lca:
        return root
    # 否则哪个树上存在就返回哪个树
    return left_lca if left_lca else right_lca
# 求某一节点在二叉树中的层数 root为0层 换言之为求某一节点到根结点的距离
def findLevel(root, node, level):
    if not root: return -1 # -1表示没找到
    if root.val == node:
        return level
    left_level = findLevel(root.left, node, level+1)
    right_level = findLevel(root.right, node, level+1)
    return left_level if left_level != -1 else right_level
def nodeDistance(root, n1, n2):
    lca = findLevel(root, n1, n2)
    dis_lca = findLevel(root, lca, 0)
    dis_n1 = findLevel(root, n1, 0)
    dis_n2 = findLevel(root, n2, 0)
    return dis_n1 + dis_n2 - 2 * dis_lca


