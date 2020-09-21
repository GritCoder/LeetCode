# 递归
def solution1(nums, S):
    cnt = [0]
    n = len(nums)
    def track(nums, index, sum_, S):
        if index == n:
            if sum_ == S:
                cnt[0] += 1
        else:
            track(nums, index+1, sum_+nums[index], S)
            track(nums, index+1, sum_-nums[index], S)
    track(nums, 0, 0, S)
    return cnt[0]

# 动态规划 这个思路妙就妙在转换成了0-1背包问题
'''
把所有符号为正的数总和设为一个背包的容量，容量为x；把所有符号为负的数总和设为一个背包的容量，容量为y。
在给定的数组中，有多少种选择方法让背包装满。令sum为数组的总和，则x+y = sum。而两个背包的差为S,则x-y=S。从而求得x=(S+sum)/2。
基于上述分析，题目转换为背包问题：给定一个数组和一个容量为x的背包，求有多少种方式让背包装满。
'''
def solution2(nums, S):
    sum_ = sum(nums)
    # 目标和不可能大于数组和
    if S > sum_:
        return 0
    # 因为都是整数，(sum_ + S) 不能为奇数，不然就出现小数了，也不能划分
    if (sum_ + S) % 2 != 0:
        return 0
    x = (sum_ + S) // 2
    dp = [0] * (x+1)
    dp[0] = 1
    for num in nums:
        # for i in range(num, x+1):
        # 完全背包问题内循环是正序
        '''
        0-1背包内循环逆序，主要是因为
        一维的Dp是二维Dp在空间上进行复用的结果。dp[i]=f(dp[i-num])，等式的右边其实是二维DP上一行的数据，应该是只读的，
        在被读取前不应该被修改。如果正序的话，靠后的元素在读取前右边的dp有可能被修改了，倒序可以避免读取前被修改的问题。
        当然如果你把dp先复制一份出来，那顺序就无所谓了，都是正确的。
        '''
        for i in range(x, num-1, -1):
            dp[i] += dp[i-num]
    return dp[x]

print(solution2([1,1,1,1,1], 3))
