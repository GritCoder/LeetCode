# 三数之和 全排列II 组合之和
# 相对于组合总和，这个题目的变化就是，每个元素只能使用一次，不可重复使用
def solution(nums, target):
    ans = []
    t = target
    # 排序相当于减枝 减小了搜索空间  
    nums = sorted(nums)
    n = len(nums)

    def backtrack(target, tmp, index):
        # if target < 0:
        #     return
        # if target == 0:
        #     ans.append(tmp)
        # 注意，这里不能写成target来判断了，因为target在递归过程中是变化的，要用之前的target判断，即 t 变量(调用递归之前保存的)
        # 当然了，写成上面那种 target 与 0 值比较也是可以的，看你个人喜好写法
        if sum(tmp) > t:
            return
        if sum(tmp) == t:
            ans.append(tmp)
        for i in range(index, n):
            if i > index and nums[i] == nums[i - 1]:
                continue
            backtrack(target - nums[i], tmp + [nums[i]], i + 1)

    backtrack(target, [], 0)
    return ans

# Python判断一个数是否在list中，高效的解法是转成字典，这样是O(1)复杂度，否则默认的是O(N)复杂度
# lis = [1,2,3,4,5]
# dic = dict(zip(lis, lis))
# for item in dic:
#     print(item)
# print(dic)

ans = solution([10, 1, 2, 7, 6, 1, 5], 8)
print(ans)
