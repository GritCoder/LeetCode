'''
给你一个整数数组 arr 和两个整数 k 和 threshold 。
请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。

输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。
'''
# 个人解法
def solution(arr, k, threshold):
    count = 0
    for i in range(len(arr)-(k-1)):
        sum = 0
        for j in range(i,i+k):
            sum += int(arr[j])
        avg = sum / k
        if avg >= threshold:
            count += 1

    return count

# 更优解法 核心思想是用到了空间换时间，加了一个ans辅助数组
'''
首先遍历数组，将累计和存储到一个新的数组中（注意该数组的长度应该比原数组多1）
构建长度为k的滑动窗口，窗口的左右端口差值为中间k个数字的和，取平均后与threshold做判断即可
注意子数组顺序与原数组一致
'''
def best_solution(arr, k, threshold):
    res = [0] # 这个0写的太妙了，没有不行
    ans = 0
    for i in range(len(arr)):
        res.append(res[-1] + arr[i])
    for i in range(len(res) - k): # 与自己解法不一样，不用k-1，因为数组长度比原来多1
        b = res[i + k] # 滑动窗口思想
        a = res[i]
        if (b - a) >= threshold:
            ans += 1
    return ans
if __name__ == "__main__":
    arr, k, threshold = input().split()
    arr = arr[1:][:-1].split(',')
    # print(arr)
    solution(arr, int(k), int(threshold))


