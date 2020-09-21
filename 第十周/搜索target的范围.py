'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
'''
def searchRange(nums, target):
    # arrs = [str(x) for x in nums]
    # print(''.join(arrs))
    find = binSearch(nums, target)
    if find == -1:
        return [-1, -1]
    left = find - 1
    right = find + 1
    # 继续向左查找是否还有元素
    while left >= 0 and nums[left] == target:
        left -= 1
    # 继续向右查找是否还有元素
    while right < len(nums) and nums[right] == target:
        right += 1
    # 为什么返回 left+1 right-1 跑一遍程序就知道了
    return [left+1, right-1]

def binSearch(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2 # 这样写，大数据情况下可以避免溢出 当然你也可以正常写 mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(searchRange([5,7,7,8,8,10], 8))

# 一般来说，二分查找，我们找到目标元素就直接返回了，但是如果有多个重复元素，我们也可以不返回，而是继续查找该元素第一次出现的位置和最后一次出现的位置
# 可以理解为二分查找的升级版吧，了解一下
# 代码改写成Python的很简单，先不改写了，知道就行了，这个case
# 另一种解法，因为是有序的嘛，所以转换为求 target 和 target - 1 的右边界了
def solution(nums, target):
    def helper(target):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        return i
    return [helper(target - 1), helper(target) - 1]
print(solution([5,7,7,8,8,10], 8))

# print(type(([1,2])))
# x = tuple([[1,2]])
# x[0][0] = 3
# print(x[0])