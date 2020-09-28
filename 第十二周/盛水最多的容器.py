# 双指针解法，类似于接雨水那个题
def solution(height):
    left, right = 0, len(height) - 1
    ans = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        ans = max(ans, area)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return ans
print(solution([1,8,6,2,5,4,8,3,7]))
