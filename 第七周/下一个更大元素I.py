# 先找到该元素在nums2中的位置，然后再找它之后比它大的
# def solution(nums1, nums2):
#     n1, n2 = len(nums1), len(nums2)
#     ans = [-1] * n1
#     for i in range(n1):
#         flag = 0
#         bigger = -1
#         for j in range(n2):
#             # 先找出现的位置
#             if nums1[i] == nums2[j]:
#                 flag = 1 # 说明找到了nums1元素在nums2中的位置
#             # 再去比较
#             if flag == 1 and nums1[i] < nums2[j]:
#                 bigger = j
#                 break # get了 这样跳出的只是内层循环
#         if bigger != -1:
#             ans[i] = nums2[bigger] # 更新
#     return ans
# 改进一: 从后往前找不就行了嘛 遇到大的就更新
# def solution(nums1, nums2):
#     n1, n2 = len(nums1), len(nums2)
#     ans = [-1] * n1
#     for i in range(n1):
#         for j in range(n2-1, -1, -1):
#             if nums1[i] == nums2[j]: # 碰见相等直接break就行 这样可以保证找的都是位置后面的
#                 break
#             if nums1[i] < nums2[j]:
#                 ans[i] = nums2[j]
#     return ans
# 改进二: 为nums2维护一个字典，key为当前元素，value为该元素的下一个比其大的值
def solution(nums1, nums2):
    stack = []
    dic = {}
    for item in nums2:
        while stack and item > stack[-1]:
           dic[stack.pop()] = item
        stack.append(item)
    return [dic.get(item, -1) for item in nums1] # get(key, default) 若key不存在 则返回默认值
print(solution([4,1,2], [1,3,4,2]))