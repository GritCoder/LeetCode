# 借助库函数
# def solution(inputs):
#     n = len(inputs)
#     if n == 0:
#         return ''
#     prefix = inputs[0]
#     for i in range(1, n):
#         while not inputs[i].startswith(prefix):
#             # 前缀字符截断一位
#             prefix = prefix[:len(prefix)-1]
#     return prefix
# 不用库函数
def solution(inputs):
    n = len(inputs)
    if n == 0:
        return ''
    prefix = inputs[0]
    for i in range(1, n):
        prefix = lcp(prefix, inputs[i])
        if not prefix:
            return ''
    return prefix

def lcp(prefix, input):
    length, index = min(len(prefix), len(input)), 0
    while index < length and prefix[index] == input[index]:
        index += 1
    return prefix[:index]

print(solution(['flower', 'flow', 'flight']))