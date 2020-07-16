# 暴力法 利用直线方程定义来做
def judge(x1, y1, x2, y2, x, y): # 直线方程变形 把除转化为乘 避免小数精度影响
    if (y2-y1) * (x-x2) == (x2-x1) * (y-y2):
        return True
def maxPoints(points):
    # 只有0 1 2个点的情况，直接返回点的个数
    n = len(points)
    if n < 3:
        return n
    # 判断所有点是否都在一条直线上(即所有点的纵坐标或者横坐标都是一样的)
    i = 0
    for i in range(n-1):
        if points[i][0] != points[i+1][0] or points[i][1] != points[i+1][1]:
            break
    if i == n - 2:
        return n
    Max = 0
    # 前面两层循环确定所有的直线  最后一个循环去匹配所有点 求结果
    for i in range(n):
        for j in range(i+1, n):
            if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                continue # 说明是同一点
            res = 0
            for k in range(n):
                if k != i and k != j:
                    if judge(points[i][0], points[i][1], points[j][0], points[j][1],
                             points[k][0], points[k][1]):
                        res += 1
            Max = max(res, Max)
    return Max + 2 # 加上直线上本身两个点
print(maxPoints([[1,1],[1,1],[1,1],[2,2],[2,2],[2,2]]))

# 还有一种方法 转化为 经过某个点的直线，哪条直线上的点最多
# 接下来只需要换一个点，然后用同样的方法考虑完所有的点即可
# 其实有点类似于CV里面的霍夫直线检测的思路