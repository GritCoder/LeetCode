'''
辅导课堂在推进质量建设，需要分析每堂直播课的用户报障数量。
当连续多个课程的报障数量之和大于一个数s的时候，系统会发出报警。小猿想知道最长连续的没有触发报警的课程数量。
'''
# 典型的滑动窗口 注意这个题跟最大连续子数组那个题不太一样
def solution(nums, th):
    # n,s = list(map(int,input().strip().split())) # 个数跟阈值
    # nums = list(map(int, input().strip().split())) # 数组
    left, right = 0, 1
    sum_ = nums[0]
    ans, n = 0, len(nums)
    while left <= right and right < n:
        if sum_ <= th:
            ans = max(ans, right - left)
        else:
            sum_ -= nums[left]
            left += 1
        sum_ += nums[right]
        right += 1
    return ans
print(solution([5,1,1,1,2,3], 5))