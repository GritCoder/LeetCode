# 典型的矩阵搜索问题，可用深搜+减枝解决
def exist(board, word):
    m, n = len(board), len(board[0])
    visit = [[0] * n for _ in range(m)]
    def dfs(i, j, k):
        # 减枝条件
        if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k] or visit[i][j]:
            return False
        if k == len(word) - 1:
            return True
        visit[i][j] = 1
        # 只要有一个方向到达，就可以返回
        ans = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1)
        # 回溯过去，这个必须得加，因为是一个一个搜索的，若不加，就等于所有点都相同的flag了，很明显答案会错误
        visit[i][j] = 0
        return ans
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False
print(exist([["C","A","A"],["A","A","A"],["B","C","D"]],
"AAB"))
