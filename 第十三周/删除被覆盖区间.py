# 区间问题，优先排序一下看看
def solution1(intervals):
    # 区间按起点升序，若起点相同，则按终点降序
    intervals.sort(key=lambda x:(x[0], -x[1]))
    cnt = 0
    pre_end = 0
    for st, end in intervals:
        if end > pre_end:
            cnt += 1
            pre_end = end
    return cnt

# 暴力法
def solution2(intervals):
    n = len(intervals)
    cnt = n
    # 对于每一个区间，枚举剩余的空间，判断是否被覆盖
    for i in range(n):
        for j in range(n):
            if i != j and intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                cnt -= 1
                # 仔细揣摩一下，找到就完事了，再往下接着找也没有意义了
                break
    return cnt
print(solution2([[1,4],[3,6],[2,8]]))