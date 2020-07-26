# 给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组（的长度）。
def solution(nums):
    # 暴力法
    # if not nums:
    #     return 0
    # res = 0
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         tmp = nums[i:j+1] # 必须 +1 不然取不到右端点 j
    #         count_0 = tmp.count(0)
    #         count_1 = tmp.count(1)
    #         if count_0 == count_1:
    #             res = max(res, j-i+1)
    # return res

    # 哈希法 思路很巧妙  HashMap 来保存所有的 (index, count) 对于一个 count，我们只记录它第一次出现的位置
    # 后面遇到相同的count，我们都用这个第一次记录的 index 来计算子数组的长度。
    if not nums:
        return 0
    maps = {0:-1}
    res, count = 0, 0
    for i, num in enumerate(nums):
        if num == 0:
            count -= 1
        else:
            count += 1
        if count in maps: # 当count再次为0时 说明现在走过的序列中0和1抵消了(个数相等) 此时即找到了一个符合条件的序列
                          # 当然了 count不一定就为0 其他数字也一样 只要走了一圈又回到本身 说明走的过程0和1个数相等 就是满足条件的序列
            res = max(res, i-maps[count]) # 注意，如果maps初始value不是-1 则这里要改为 i-maps[count]+1 因为这里都是表示的索引
        else:
            maps[count] = i # 记录count第一次出现的位置索引
    return res
# maps = {0:1}
# for item in maps:
#     print(item) # 这样默认输出的是key
print(solution([0,1,1,0,1,0]))