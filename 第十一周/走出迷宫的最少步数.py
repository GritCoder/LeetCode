# 时间复杂度O(N^2) 空间复杂度O(1)
# 可以直接在grids上面操作，因为dp具有无后效性
# 也就是说，对于要求的格子来说，它只关心它的右格子与下方格子中的步数，至于这两个格子的步数是如何算出来的
# 它们不关心，这就叫无后效性。
# dp常用的思路是自底向上，即根据出口来求入口(通俗点说是倒着来)，本题即为这样的思路
# 当然了，也有正着来的dp，比如那些最长序列，子串等，就是正着初始化的
# 升级版，应该如何记录最小步数的行走路径呢？这个问题以后有机会可以好好研究一下
def solution(grids):
    rows, cols = len(grids), len(grids[0])
    # 初始化最右边格子，从最后一列倒数第二行开始
    for i in range(rows-2, -1, -1):
        # -1 表示障碍物
        # 如果当前格子的下一个格子不是障碍物.. 则当前格子到出口的步数为下一个格子的步数+1
        if grids[i+1][cols-1] != -1 and grids[i][cols-1] != -1:
            grids[i][cols-1] = 1 + grids[i+1][cols-1]
        # 否则为无穷大
        else:
            grids[i][cols-1] = float('inf')
    # 初始化最底部的格子，从最后一行倒数第二列开始
    for j in range(cols-2, -1, -1):
        if grids[rows-1][j+1] != -1 and grids[rows-1][j] != -1:
            grids[rows-1][j] = 1 + grids[rows-1][j+1]
        else:
            grids[rows-1][j] = float('inf')
    # 从右到左，从下到上填满每个格子的值
    for i in range(rows-2, -1, -1):
        for j in range(cols-2, -1, -1):
            if grids[i][j] == -1:
                grids[i][j] = float('inf')
                continue
            else:
                grids[i][j] = 1 + min(grids[i+1][j], grids[i][j+1])
    print(grids)
    return grids[0][0]
# 这个题其实有点瑕疵，如果最后一行或者最后一列有 -1 的话 初始化的值会不正确 因此要多加一个限制条件 就是 and 后面那个，判断一下自身值
print(solution([
            [0,0,0,0,0,0,0,0],
            [0,0,-1,0,0,0,-1,0],
            [0,0,0,0,-1,0,0,0],
            [-1,0,-1,0,0,-1,0,0],
            [0,0,-1,0,0,0,0,0],
            [0,0,0,-1,-1,0,-1,0],
            [0,-1,0,0,0,-1,0,0],
            [0,0,0,0,0,0,0,0]]
    ))