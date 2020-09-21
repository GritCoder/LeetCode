# 这个题的变化就是 nums 限定为1-9的自然数，然后加了一个约束条件k，即 tmp 的长度必须为 k，其他也就没啥了，仍然不重复
def solution(n, k):
    ans = []
    def backtrack(n, tmp, index):
        if n == 0 and len(tmp) == k:
            ans.append(tmp)
            return
        if n < 0:
            return
        for i in range(index + 1, 10):
            backtrack(n - i, tmp + [i], i)

    backtrack(n, [], 0)
    return ans
print(solution(18, 2))