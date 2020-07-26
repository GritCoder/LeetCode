# 核心是要明白 水能达到的最高位置 等于两边最大高度的较小值减去当前高度的值
# 暴力法(朴素法) # 提交超时 明白思想 很多优化都是基于暴力法的
# def solution(height):
#     ans = 0
#     n = len(height)
#     for i in range(n):
#         max_left, max_right = 0, 0
#         for j in range(i, -1, -1): # 向左找最大高度
#             max_left = max(max_left, height[j])
#         for j in range(i, n): # 向右找最大高度
#             max_right = max(max_right, height[j])
#         ans += min(max_right, max_left) - height[i] # 求解
#     return ans
# 栈
# 当遍历墙的高度的时候，如果当前高度小于栈顶的墙高度，说明这里会有积水，我们将墙的高度的下标入栈
# 如果当前高度大于栈顶的墙的高度，说明之前的积水到这里停下，我们可以计算下有多少积水了。计算完，就把当前的墙继续入栈，作为新的积水的墙。
def solution(height):
    ans = 0
    stack = []
    n = len(height)
    for i in range(n): # 遍历的是每一个高度 因此计算的也是当前高度的积水量
        # 若要计算积水量 就要找到左右边界才行
        while stack and height[i] > height[stack[-1]]:
            cur = stack[-1] # 要计算积水量的当前高度
            stack.pop()
            if not stack:
                break
            # 注意理解 i 其实是右边界 三者关系 [left cur i]
            # 因为上面已经弹出了当前高度 所以现在栈顶元素是cur的左边界
            distance = i - stack[-1] - 1 # -1是因为中间才能接水 边界不算
            min_ = min(height[i], height[stack[-1]])
            # 注意这里跟朴素法不一样了 这里转化成求面积了 对比 柱形图的最大矩形 那道题
            ans += distance * (min_ - height[cur]) # 还是那句话 水能达到的最高位置 等于两边最大高度的较小值减去当前高度的值
        stack.append(i)
    return ans
print(solution([0,1,0,2,1,0,1,3,2,1,2,1]))
