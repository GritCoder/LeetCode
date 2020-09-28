# 双指针，移除指定元素，返回新数组长度
def solution1(nums, val):
    i = 0
    n = len(nums)
    for j in range(n):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
# print(solution1([0,1,2,2,3,0,4,2], 2))
# 有序数组去重双指针解法
def solution2(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            # 往前更新一个元素的空间
            i += 1
            # 赋值
            nums[i] = nums[j]
    return i + 1
print(solution2([0,1,2,2,0,4,2]))

# 无序数组去重，什么又不改变相对位置的，参考之前的题解    