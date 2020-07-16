# 要树的高度最小，即要生成一颗平衡二叉树， 递归的划分区间即可
# 默认的是构建一颗二叉搜索树(根结点在中间)
class BinTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def solution(nums):
    def recursion(nums):
        if len(nums) == 0:
            return
        mid = len(nums) // 2 # 取整除
        root = BinTree(nums[mid])
        root.left = recursion(nums[:mid])
        root.right = recursion(nums[mid+1:])
        return root
    return recursion(nums)
