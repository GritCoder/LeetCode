# 贪心 + 排序
# 动规在这里貌似不太好使
import functools
def mycmp(x, y):
    if x + y > y + x: return 1  # x > y 返回正数
    elif x + y < y + x: return -1 # x < y 返回负数
    else: return 0 # 相等 返回 0

def solution(nums):
    # 转换成字符是怕有大数，出现越界
    # print(str(nums)) # 这样是列表整体变成字符串 并不是单个元素 不满足题意
    strs = [str(item) for item in nums] # 每个元素转字符类型
    strs.sort(key=functools.cmp_to_key(mycmp)) # inplace操作
    return ''.join(strs)
print(solution([3,30,34,5,9]))