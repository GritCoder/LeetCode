# 跟移除K个数字思路一样 只不过这里变成了两个数组 最后merge一下就行了
def maxNum(nums1, nums2, k):
    def pick_max(nums, k): # 跟移除K个数组类似 只不过这里变成了让结果最大 然后丢弃元素
        stack = []
        drop = len(nums) - k # 取 k 个元素  那当然是丢弃 len(nums) - k 个元素
        for num in nums:
            while drop and stack and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)
        return stack[:k]
    def merge(A, B): # 类似于归并排序的merge
        ans = []
        while A or B:
            bigger = A if A > B else B
            ans.append(bigger[0])
            bigger.pop(0) # 指定索引 弹出第一个元素  必须加0 否则就会弹出最后一个元素 结果就不对了
        return ans
    res = []
    for i in range(k+1): # 暴力遍历每一种情况的组合 然后取其最大者
        if i <= len(nums1) and k - i <= len(nums2):
            res.append(merge(pick_max(nums1, i), pick_max(nums2, k-i)))
    return max(res)
print(maxNum([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
