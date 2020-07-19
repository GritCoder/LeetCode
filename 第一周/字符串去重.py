'''
题目要求：保持字典序最小并且字符序列的相对位置不变输出
贪心 - 用栈
每遇到一个字符，如果这个字符不存在于栈中，就需要将该字符压入栈中。
但在压入之前，需要先将之后还会出现，并且字典序比当前字符小(即栈顶元素比目前字符大)的栈顶字符移除，然后再将当前字符压入。
'''
# 注:  跟 不同字符的最小子序列(1081题) 一样的思路 一样的代码
import collections
def solution(input): # 可以按照这个思路来理解 跟第六周 移掉K位数字那个题思路类似 方便理解
    stack = []
    remain_counter = collections.Counter(input) # 这个函数统计的是每个字符出现的次数
    print(remain_counter)
    for c in input:
        if c not in stack: # 若 c 不在栈里面 肯定要添加 不过就是添加前要判断一下栈还是否需要pop出元素
            while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                stack.pop()
            stack.append(c)
        remain_counter[c] -= 1
    return ''.join(stack)

# 使用 hashmap 代替了数组的遍历查找，属于典型的空间换时间方式(优化)
# def solution(input:str):
#     stack = []  # 在python中，个人理解为栈可以用列表来代替 可以完全用列表的方法
#     seen = set() # 一个空集合 无序的 # 已测试，换成列表也可以，就是添加元素的方法换一下
#     last_occurrence = {c:i for i, c in enumerate(input)} # 用来判断字符最后出现的位置，这种写法实在是高！
#     print(last_occurrence)
#     # seen this is to maintain only one of each character 状态变量
#     for i, c in enumerate(input):
#         if c not in seen:
#             while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
#                 seen.remove(stack.pop()) # discard为集合删除元素的操作， 与remove不同，若元素不存在集合中 remove会报错 discard不会
#                                         # 实际测试时也没报错，知道就行了
#             seen.add(c)
#             stack.append(c)
#     print(seen)
#     return ''.join(stack)
if __name__ == "__main__":
    res = solution("cbacdcbc")
    print(res)