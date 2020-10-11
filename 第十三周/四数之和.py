# 排序+双指针
# 实际上是可以泛化的，这里是四数之和为0，实际上可以为任何target，注意一下
def solution1(nums):
    if not nums or len(nums) < 4:
        return []
    ans = []
    nums.sort()
    n = len(nums)
    for i in range(n-3):
        # 第一个数去重
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # 第一个数减枝 情况一
        if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > 0:
            break
        # 情况二
        if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < 0:
            continue
        for j in range(i+1, n-2):
            # 第二个数去重
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            # 第二个数减枝 情况一
            if nums[i] + nums[j] + nums[j+1] + nums[j+2] > 0:
                break
            # 情况二
            if nums[i] + nums[j] + nums[n-2] + nums[n-1] < 0:
                continue
            left, right = j + 1, n - 1
            while left < right:
                if nums[i] + nums[j] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[j], nums[left], nums[right]])
                    # 第三四个数去重
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    # 找到一种解后同时更新左右指针
                    left += 1
                    right -= 1
                elif nums[i] + nums[j] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
    return ans

print(solution1([1, 0, -1, 0, -2, 2]))

