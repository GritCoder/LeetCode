'''
核心思路是以左括号为基准，通过维护对右括号的需求数need，来计算最小的插入次数
因为只有遇到右括号)的时候才会need--，need == -1意味着右括号太多了，所以需要插入左括号。
最后返回 left + need 是因为 left 记录的左括号的插入次数，need记录了右括号的需求
'''
def solution(s):
    left = 0
    need = 0
    for c in s:
        if c == '(':
            # 对右括号的需求 + 1
            need += 1
        if c == ')':
            # 对右括号的需求 - 1
            need -= 1
            if need == -1:
                need = 0
                # 需插入一个左括号
                left += 1
    return left + need
print(solution('())('))
