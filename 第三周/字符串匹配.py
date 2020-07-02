# 子串逐一比较(暴力法) - O((N-L)*L) 滑动窗口
# def solution(haystack, needle):
#     if not needle:
#         return 0
#     len_haystack, len_needle = len(haystack), len(needle)
#     for start in range(len_haystack-len_needle+1):
#         if haystack[start:start+len_needle] == needle:
#             return start
#     return -1
# 优化 不用所有子串都比较 只比较首字符相等的子串 借助偏移表(空间换时间)
# 具体思路解析看 https://leetcode-cn.com/problems/implement-strstr/solution/python3-sundayjie-fa-9996-by-tes/
# 最坏情况：O(nm) 平均情况：O(n)
def shift(needle):
    dic = {}
    m = len(needle)
    # 这里必须倒着遍历，这样可以确保子串中重复字符的索引是最小的
    # 因为如果主串字符在子串中，返回的是最小索引，这样二者才能保持一致
    # 偏移表的作用是存储每一个在模式串中出现的字符
    # 在模式串中出现的‘最右’[这也是倒着遍历的原因]位置到尾部的距离+1
    for i in range(m-1, -1, -1):
        if not dic.get(needle[i]):
            dic[needle[i]] = m - i
    dic["end"] = m + 1 # +1是因为如果pattern长度后一位字符不在偏移表内
    return dic
def solution(haystack, needle):
    if not needle:
        return 0
    dic = shift(needle)
    idx = 0
    # idx + len(needle) 实际上就是滑动窗口了 动态的变化
    m, n = len(needle), len(haystack)
    while idx + m <= n:
        # 当前待匹配字符串
        cur_str = haystack[idx:idx+m]
        if cur_str == needle:
            return idx
        else:
            # while里面有'='，这里如果不加这个边界判断，若子串与主串一样，则会溢出错
            if idx + m >= n:
                return -1
            # cur_c是主串中pattern长度后的那个字符
            cur_c = haystack[idx+m]
            if dic.get(cur_c):
                idx += dic[cur_c]
            else:
                idx += dic["end"]
    return -1 if idx + m >= n else idx
print(solution("mississippi", "issi"))
