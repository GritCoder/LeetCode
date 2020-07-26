# 暴力法 依次遍历柱形的高度，对于每一个高度分别向两边扩散，求出以当前高度为矩形的最大宽度多少
# def maxOfRectangle(heights):
#     n = len(heights)
#     if n == 0:
#         return 0
#     ans = 0
#     for i in range(n):
#         left = i
#         cur_height = heights[i]
#         while left > 0 and heights[left-1] >= cur_height: # 向左扩散
#             left -= 1
#         right = i
#         while right < n-1 and heights[right+1] >= cur_height: # 向右扩散
#             right += 1
#         max_width = right - left + 1
#         ans = max(ans, max_width * cur_height)
#     return ans
# 单调栈来解
# 对于一个高度，如果能得到向左和向右的边界
# 那么就能对每个高度求一次面积
# 遍历所有高度，即可得出最大面积
# 使用单调栈，在出栈操作时得到前后边界并计算面积
def maxOfRectangle(heights):
    if not heights:
        return 0
    stack = []
    heights = [0] + heights + [0] # 加前导0是保证第一个元素被有效计算 加后导0是保证所有元素都能出栈
    ans = 0
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]: # 注意 此时计算的是当前高度左边的那个柱条的面积
            tmp = stack.pop()
            # 这里宽度-1是因为上面pop了，使宽向左移动了一位，因此减去
            # 如果不减的话 可以使用队列的peek方法
            ans = max(ans, (i-stack[-1]-1) * heights[tmp])
        stack.append(i) # 继续入栈 以备后面计算再次使用
    return ans
print(maxOfRectangle([2,1,5,6,2,3]))