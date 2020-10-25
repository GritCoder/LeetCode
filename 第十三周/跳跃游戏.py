# 贪心
def solution(nums):
    n, rightmax = len(nums), 0
    for i in range(n):
        if i <= rightmax:
            rightmax = max(rightmax, i + nums[i])
            if rightmax >= n - 1:
                return True
    return False
print(solution([2,3,1,1,4]))