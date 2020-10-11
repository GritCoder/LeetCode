# 已经AC的代码，没问题
def intervalIntersection(A, B):
    i, j = 0, 0
    ans = []
    # 区间问题，画图分析，考虑各种情况，很简单
    while i < len(A) and j < len(B):
        a1, a2 = A[i][0], A[i][1]
        b1, b2 = B[j][0], B[j][1]
        # 核心代码
        # if b2 < a1 or a2 < b1:
        # [a1,a2] 和 [b1,b2] 无交集
        # 那么存在交集，取反即可
        if b1 <= a2 and b2 >= a1:
            # 计算交集，加入ans
            ans.append([max(a1, b1), min(a2, b2)])
        # 谁终点小，谁后移
        if b2 < a2:
            j += 1
        else:
            i += 1
    return ans
print(intervalIntersection([], []))