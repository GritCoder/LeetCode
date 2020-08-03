# 归并法
# def reversePairs(nums):
#     cnt = 0
#     def merge(left, right): # 合并
#         result = [] # 保存排序好的结果
#         i = 0; j = 0
#         nonlocal cnt
#         while(i < len(left) and j < len(right)):
#             if left[i] <= right[j]: # 注意 如果这里不加等号 归并排序就不是稳定的了 get了
#                 result.append(left[i])
#                 i += 1 # 下标后移
#             else:
#                 cnt += len(left) - i
#                 result.append(right[j])
#                 j += 1 # 下标后移
#         result += left[i:]
#         result += right[j:]
#         return result
#     def mergeSort(arr): # 分治
#         if len(arr) <= 1:
#             return arr
#         mid = int(len(arr) / 2)
#         left = mergeSort(arr[:mid])
#         right = mergeSort(arr[mid:])
#         return merge(left, right)
#     mergeSort(nums)
#     return cnt
# 暴力法
# def reversePairs(nums):
#     n = len(nums)
#     cnt = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] > nums[j]:
#                 cnt += 1
#     return cnt

# 高级解法 树状数组 详情解析见 https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/
'''
预备知识
「树状数组」是一种可以动态维护序列前缀和的数据结构，它的功能是：
单点更新 update(i, v)： 把序列 i 位置的数加上一个值 v，这题 v = 1
区间查询 query(i)： 查询序列 [1 \cdots i][1⋯i] 区间的区间和，即 i 位置的前缀和
修改和查询的时间代价都是 O(\log n)其中 n 为需要维护前缀和的序列的长度。
'''
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

import bisect
class Solution(object):
    def reversePairs(self, nums):
        n = len(nums)
        # 离散化
        tmp = sorted(nums)
        # 这里离散化后 nums[i] 里面存储的是对应元素的索引了 因此下面的for循环必须带
        for i in range(n):
            nums[i] = bisect.bisect_left(tmp, nums[i]) + 1 # bisect函数的返回值是列表的整数下标 left是指碰到相同的元素则插入到元素的左边
        # print(nums[:])
        # 树状数组统计逆序对
        bit = BIT(n)
        ans = 0
        for i in range(n-1, -1, -1):
            ans += bit.query(nums[i]-1) # 注意 这里是索引了 可以跟第八周树状数组那个脚本结合着看
            bit.update(nums[i])
        return ans
obj = Solution()
print(obj.reversePairs([7,5,6,4]))