class BinaryIndexTree(object):
    def __init__(self, n):
        self.BITree = [0] * (n+1)

    def getSum(self, i):
        ans = 0
        i += 1
        while i > 0:
            ans += self.BITree[i]
            i -= i & (-i) # 本质是 lowBit() 操作 了解一下
        return ans

    def printTree(self, nums, n):
        for i in range(n):
            print(nums[i], end=' ')

    def updateBITree(self, n, i, val):
        i += 1
        while i <= n:
            self.BITree[i] += val
            i += i & (-i) # 本质是 lowBit() 操作 了解一下

    def constructBITree(self, nums, n):
        for i in range(n):
            self.updateBITree(n, i, nums[i])
'''
# 更简洁的一种写法
class BIT(object):
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n+1)
    @staticmethod
    def lowbit(x):
        return x & (-x)
    def query(self, x):
        ret = 0
        while x > 0:
            ret += self.tree[x]
            x -= BIT.lowbit(x)
        return ret
    def update(self, x):
        while x <= self.n:
            self.tree[x] += 1
            x += BIT.lowbit(x)
'''
# 能否将树状数组扩展到以logN的时间复杂度计算区间和呢？
# 答案是肯定的，rangSum(l,r) = getSum(r) - getSum(l - 1)
# 求区间和的问题 线段树/树状数组 是最高效的解法 了解一下
# 树状数组存储的是若干个元素的和 这点要清楚 具体几个元素 是由 lowBit() 算出来的 即 i & (-i) 了解一下
if __name__ == "__main__":
    nums = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(nums)
    tree = BinaryIndexTree(n)
    tree.constructBITree(nums, n)
    tree.printTree(nums, n)
    print(tree.getSum(4))
