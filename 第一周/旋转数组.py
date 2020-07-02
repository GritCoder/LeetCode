# 暴力法 O(1)空间复杂度
# def rotate(nums, k):
#     length = len(nums)
#     for i in range(k):
#         last = nums[length-1] # 都是跟最后一个元素交换，因此跟i无关
#         for j in range(length):
#             nums[j], last = last, nums[j]
#     return nums

# 引入辅助空间,计算每一个元素的新位置
def rotate(nums, k):
    length = len(nums)
    tmp = [0] * length
    for i in range(length):
        tmp[(i+k)%length] = nums[i] # 必须用临时数组，否则原数组元素会被修改
    for i in range(length):
        nums[i] = tmp[i]
    return nums


print(rotate([1,2,3,4,5], 1))
