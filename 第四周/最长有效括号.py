# 栈 python中的栈跟列表等效
# def solution(strs):
#     stack = []
#     stack.append(-1)
#     maxans = 0
#     for i in range(len(strs)):
#         if strs[i] == '(':
#             stack.append(i)
#         else:
#             stack.pop()
#             if not stack:
#                 stack.append(i)
#             else: # 不为空则是一个有效的括号 求其长度
#                 maxans = max(maxans, i-stack[-1])
#     return maxans
# 双向扫描,思路很简单
def solution(strs):
    left = right = 0
    maxans = 0
    # 这种情况只能求出右括号大于左括号情况下的有效长度
    for item in strs:
        if item == '(':
            left += 1
        else:
            right += 1
        if right == left:
            maxans = max(maxans, 2 * right)
        elif right > left: # 左到右遍历 则 right > left 不能反
            right = left = 0
    left = right = 0
    # 这种情况只能求出左括号大于右括号情况下的有效长度
    for item in strs[::-1]:
        if item == '(':
            left += 1
        else:
            right += 1
        if right == left:
            maxans = max(maxans, 2 * left)
        elif left > right: # 右到左遍历 则 left > right 不能反
            left = right = 0
    # 返回的是两种情况下的最大有效长度
    return maxans
print(solution('()((())'))