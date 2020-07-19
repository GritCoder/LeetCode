# 移除 K 个数字后使剩余的结果值最小
def removeKnums(num, k):
    stack = []
    remains = len(num) - k # 要保留的元素个数
    for digit in num:
        while k and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    # lstrip 删除前导指定字符 rstrip 删除后导 strip 删除前后的  若没有指定字符 就删除空格 \n \t等东西
    return ''.join(stack[:remains]).lstrip('0') or '0' # 注意一下 返回的结果默认去除前导0 即认为前导0是无效的
print(removeKnums(str('578611234'), 3))
