# def solution(n):
#     count = 0
#     flag = 1
#     while n:
#         if n & flag:
#             count += 1
#         n = n >> 1
#     return count
# # def solution(n):
# #     count = 0
# #     while n:
# #         count += 1
# #         n = n & (n - 1)
# #     return count
# # 直接一句话
# # return bin(n).count('1')
# print(solution(9))

