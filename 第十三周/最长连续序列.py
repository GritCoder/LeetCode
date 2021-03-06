# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 哈希法
'''
对于匹配的过程，暴力的方法是 O(n) 遍历数组去看是否存在这个数，
但其实更高效的方法是用一个哈希表存储数组中的数，这样查看一个数是否存在即能优化至 O(1) 的时间复杂度。

但仔细分析这个过程，我们会发现其中执行了很多不必要的枚举，如果已知有一个 x, x+1, x+2, ⋯,x+y 的连续序列，
而我们却重新从 x+1，x+2 或者是 x+y 处开始尝试匹配，那么得到的结果肯定不会优于枚举 x 为起点的答案，
因此我们在外层循环的时候碰到这种情况跳过即可。

那么怎么判断是否跳过呢？由于我们要枚举的数 x 一定是在数组中不存在前驱数 x−1 的，不然按照上面的分析我们会从 x−1 开始尝试匹配，
因此我们每次在哈希表中检查是否存在 x−1 即能判断是否需要跳过了。

'''
def solution(nums):
    long = 0
    nums = set(nums)
    for num in nums:
        if num - 1 not in nums:
            cur_num = num
            cur_long = 1
            while cur_num + 1 in nums:
                cur_num += 1
                cur_long += 1
            long = max(long, cur_long)
    return long
print(solution([100,4,200,1,3,2]))
