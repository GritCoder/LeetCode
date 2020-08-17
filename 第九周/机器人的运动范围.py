# 广搜
def solution(m, n, k):
    def digitSum(x):
        ans = 0
        while x:
            ans += x % 10
            x //= 10
        return ans
    from collections import deque
    q = deque([(0, 0)])
    s = set() # 存放已经访问的点
    while q:
        x, y = q.popleft()
        if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitSum(x) + digitSum(y) <= k:
            s.add((x, y))
            for nx, ny in [(x+1, y), (x, y+1)]:
                q.append((nx, ny))
    return len(s)
# 深搜(递归)
'''
已知x的数位和为s_x 那么求x+1的数位和，有如下公式
s_x + 1 if (x + 1) % 10 else s_x - 8
即x+1如果对10取余不为0 则x+1数位和为s_x + 1 否则为 s_x - 8
'''
# 当然了 如果不知道也可以不用数位和公式 每次递归的时候调用一下digitSum函数来算一下也行
def solution1(m, n, k):
    # 递归参数： 当前元素在矩阵中的行列索引 i 和 j ，两者的数位和 si, sj 。
    def dfs(i, j, si, sj):
        if i >= m or j >= n or si + sj > k or (i, j) in s:
            return 0
        s.add((i, j))
        return 1 + dfs(i+1, j, si+1 if (i+1) % 10 else si - 8, sj) + \
               dfs(i, j+1, si, sj+1 if (j+1) % 10 else sj - 8)
    s = set()
    return dfs(0, 0, 0, 0)


