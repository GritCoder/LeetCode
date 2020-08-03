# 滑动窗口的思想
# 时间复杂度：O(N)，其中N是字符串的长度。左指针和右指针分别会遍历整个字符串一次。
# 需要使用一种数据结构来判断 是否有重复的字符，常用的数据结构为哈希集合 Python中的set()
# def max_Len_subStr(s:str) -> int:
#     occ = set()
#     n = len(s)
#     ans, j = 0, 0
#     for i in range(n):
#         if i != 0: # 一开始还没添加，不移除
#             occ.remove(s[i-1])  # 添加完了，再移除
#         while j < n and s[j] not in occ:
#             occ.add(s[j])
#             j += 1  # j不用置0，因为当我们选择第k+1个字符作为起始位置时，
#                     # 首先从 k+1 到j的字符显然是不重复的
#         ans = max(ans, j-i)
#     return ans
# 这个写法更简洁一些 注意子串是连续的
def max_Len_subStr(s: str) -> int:
    k, res, c_dict = -1, 0, {} # 分别初始化索引 结果 字典
    for i, c in enumerate(s):
        if c in c_dict and c_dict[c] > k:  # 字符c在字典中 这么理解吧 通俗一点 比如一个序列是这样的 ..a...a.. 那么K指向的是第一个a c_dict[c]指向的是第二个a 这是核心 理解
            k = c_dict[c] # 更新 k 分析可知 k 始终指向上次出现元素的索引值
            c_dict[c] = i # 更新重复元素的索引 c_dict[c] 指向的是当前的索引
        else: # 若不在字典中 说明是新元素 可以计算当前长度了
            c_dict[c] = i # 字典结构是 字符为key 索引为值
            res = max(res, i - k) # 当前最大长度 # 这里k初始化-1作用就看出来了 确保第一个值正确更新
    return res
print(max_Len_subStr("abcabcd"))