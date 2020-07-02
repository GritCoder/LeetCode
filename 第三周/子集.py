# 与全排列 组合相关题目类似
# 递归 时间 O(Nx2^N) 空间 O(Nx2^N)
# def subsets(nums):
#     # n = len(nums)
#     output = [[]]
#     for num in nums:
#         # 开始假设输出子集为空，每一步都向子集添加新的整数，并生成新的子集。
#         output += [curr + [num] for curr in output]
#     return output
# 回溯
def subsets(nums):
    def backtrack(first=0, curr=[]):
        if len(curr) == k: # 递归程序出口 若不加return，会重复很多遍历，尽管结果正确
            output.append(curr[:])
            return output
        for i in range(first, n):
            curr.append(nums[i])
            backtrack(i+1, curr) # 子集跟数有关，因为结果长度可能不一样 所以此处为i
            curr.pop() # 状态回溯
    output = []
    n = len(nums)
    # 幂集是所有长度从 0 到 n 所有子集的组合
    for k in range(n+1): # k 表示的是长度
        backtrack()
    return output
# 字典排序（二进制排序） 子集掩码
# 具有最优的时间复杂度，可以生成按照字典顺序的输出结果
# def subsets(nums):
#     n = len(nums)
#     output = []
#     nth_bit = 1 << n
#     for i in range(2**n):
#         bitmask = bin(i | nth_bit)[3:] # 打印一下就知道为什么从3切片了
#         # print(bitmask)
#         output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
#     return output
print(subsets([1,2,3]))