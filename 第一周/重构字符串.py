'''
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
若可行，输出任意可行的结果。若不可行，返回空字符串。
输入: S = "aab"
输出: "aba"
输入: S = "aaab"
输出: ""
'''

'''
首先找出所有字符出现的次数，根据字符出现的次数来排序整个字符串。
如果一个字符出现的次数超过了 (N + 1) / 2，那么就不存在这样一种排列。否则，按顺序间隔输出字符就可以得到满足要求的排列。
'''
# def solution(input):
#     length = len(input)
#     A = []
#     for c, x in sorted((input.count(x), x) for x in set(input)):
#         if c > (length + 1) / 2:
#             return ""
#         A.extend(c * x)
#         ans = [None] * length
#         # [start:end:step]切片   [::-1]就是反转字符串
#         ans[::2], ans[1::2] = A[length/2:], A[:length/2]
#         return "".join(ans)
'''
贪心思路
'''
def solution(input):
    pass


# if __name__ == "__main__":
#     input = input()
#     res = solution(input)
#     print(res)

