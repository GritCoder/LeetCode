# 思路比较简单,就是考虑的边界条件比较多 若溢出 末尾'0' 开头'-'等,不具体列举了
# def solution(num):
#       # 情况并没有完全考虑全面
# #     num = str(num)
# #     if num.startswith('-') and num.endswith('0'):
# #         num = num[1:][:-1]
# #     elif num.startswith('-'):
# #         num = num[1:]
# #     elif num.endswith('0'):
# #         num = num[:-1]
# #     return num[::-1]
# #
# # print(solution(-1230))

def reverse(self, x):
    if '-' in str(x):
        y = str(x).replace("-", "")
        y = int('-' + y[::-1])
        if (-2) ** 31 < y < 2 ** 31 - 1:
            y = y
        else:
            y = 0
    else:
        y = int(str(x)[::-1])
        if (-2) ** 31 < y < 2 ** 31 - 1:
            y = y
        else:
            y = 0
    # print(int('0123')) -> 123 自动去掉前面的0了,因此可以不用考虑这种情况
    return y