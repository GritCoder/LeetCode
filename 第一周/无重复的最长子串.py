# 滑动窗口的思想
# 时间复杂度：O(N)，其中N是字符串的长度。左指针和右指针分别会遍历整个字符串一次。
# 需要使用一种数据结构来判断 是否有重复的字符，常用的数据结构为哈希集合 Python中的set()
def max_Len_subStr(s:str) -> int:
    occ = set()
    n = len(s)
    ans, j = 0, 0
    for i in range(n):
        if i != 0: # 一开始还没添加，不移除
            occ.remove(s[i-1])  # 添加完了，再移除
        while j < n and s[j] not in occ:
            occ.add(s[j])
            j += 1  # j不用置0，因为当我们选择第k+1个字符作为起始位置时，
                    # 首先从 k+1 到j的字符显然是不重复的
        ans = max(ans, j-i)
    return ans
print(max_Len_subStr("bbbbbb"))