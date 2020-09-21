# 位置 i 能达到的水柱高度和其左边的最高柱子、右边的最高柱子有关，我们分别称这两个柱子高度为l_max和r_max；
# 位置 i 最大的水柱高度就是min(l_max, r_max)。
# 更进一步，对于位置 i，能够装的水为：
# water[i] = min(
#                # 左边最高的柱子
#                max(height[0..i]),
#                # 右边最高的柱子
#                max(height[i..end])
#             ) - height[i]

# 暴力法
def solution1(heights):
    n = len(heights)
    ans = 0
    # i 表示当前柱子，因为最左边和最右边的柱子不可能装水的，因此遍历的时候可以不用考虑，知道就行了
    for i in range(1, n-1):
        l_max, r_max = 0, 0
        # 找右边柱子
        for j in range(i, n):
            r_max = max(r_max, heights[j])
        # 找左边柱子
        for j in range(i, -1, -1):
            l_max = max(l_max, heights[j])
        # 如果自己柱子是最高的话就是
        # l_max = r_max = heights[i]
        ans += min(l_max, r_max) - heights[i]
    return ans
# 暴力解法优化，每次都计算l_max和r_max，我们可以先一次性计算了保存，以空间换时间，变成O(N)时间复杂度
def solution2(heights):
    n = len(heights)
    ans = 0
    # l_max[i]表示位置 i 左边最高的柱子高度，r_max[i]表示位置 i 右边最高的柱子高度。
    l_max, r_max = [0] * n, [0] * n
    l_max[0], r_max[n-1] = heights[0], heights[n-1]
    # 正向计算左边，因为0是初始值
    for i in range(1, n):
        l_max[i] = max(heights[i], l_max[i-1])
    # 反向计算右边，因为n-1是初始值
    for i in range(n-2, -1, -1):
        r_max[i] = max(heights[i], r_max[i+1])
    # 计算答案
    # i 表示当前柱子，因为最左边和最右边的柱子不可能装水的，因此遍历的时候可以不用考虑，知道就行了
    for i in range(1, n-1):
        ans += min(l_max[i], r_max[i]) - heights[i]
    return ans

# O(1) 空间复杂度的解法
# 很容易理解，l_max是height[0..left]中最高柱子的高度，r_max是height[right..end]的最高柱子的高度。
'''
此时的l_max是left指针左边的最高柱子，但是r_max并不一定是left指针右边最高的柱子，这真的可以得到正确答案吗？
其实这个问题要这么思考，我们只在乎min(l_max, r_max)。对于上图的情况，我们已经知道l_max < r_max了，
至于这个r_max是不是右边最大的，不重要，重要的是height[i]能够装的水只和l_max有关。
'''
def solution3(heights):
    n, ans = len(heights), 0
    left, right = 0, n-1
    l_max, r_max = heights[0], heights[n-1]
    while left <= right:
        l_max = max(l_max, heights[left])
        r_max = max(r_max, heights[right])
        if l_max < r_max:
            ans += l_max - heights[left]
            left += 1
        else:
            ans += r_max - heights[right]
            right -= 1
    return ans

print(solution3([0,1,0,2,1,0,1,3,2,1,2,1]))
