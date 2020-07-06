# 八皇后问题  递归 + 回溯 这样的题有点类似全排列的味道
# 具体更详细的理解 见 https://leetcode-cn.com/problems/eight-queens-lcci/solution/python-zui-sheng-nei-cun-de-xie-fa-by-zhoudaxia/ 下面评论
def solution(n):
    st = [['.'] * n for _ in range(n)]
    res = []
    print(st)
    # 切记递归相关的变量放在嵌套函数外初始化(旷世面试时已踩过坑)
    def dfs(x_d, y_d, cur):
        j = len(cur) # 已经填充的元素个数  其实也是行的值 因为一行肯定只能填一个
        if len(cur) == n: # 若为n 则说明已经排列完了，输出一个解
            m = []
            for item in st: # 这里的出口跟全排列不太一样 是因为输出格式要求 了解一下
                # print(item)
                m.append(''.join(item))
            res.append(m)
        # 从左往右开始填的(列方向)
        for i in range(n):
            # cur存着之前已经填充Q的列的索引
            # x_d 和 y_d 分别存放负对角线和正对角线已经填充的集合
            if i not in cur and i+j not in x_d and i-j not in y_d:
                # i是列，j是行
                st[j][i] = 'Q' # 这个j用的妙，就完全不用判断行了 这里的意思已经控制一行填一个了
                dfs(x_d+[i+j], y_d+[i-j], cur+[i]) # 填下一个位置
                st[j][i] = '.' # 回溯
    dfs([], [], []) # 一开始俩对角线和列都没有被填充 因此都为空
    return res
print(solution(4))