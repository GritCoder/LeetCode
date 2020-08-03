def reversePairs(nums):
    cnt = 0
    def merge(left, right): # 合并
        result = [] # 保存排序好的结果
        i = 0; j = 0
        nonlocal cnt
        while(i < len(left) and j < len(right)):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1 # 下标后移
            else:
                cnt += len(left) - i
                result.append(right[j])
                j += 1 # 下标后移
        result += left[i:]
        result += right[j:]
        return result
    def mergeSort(arr): # 分治
        if len(arr) <= 1:
            return arr
        mid = int(len(arr) / 2)
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        return merge(left, right)
    mergeSort(nums)
    return cnt
print(reversePairs([7,5,6,4]))
# arr = [1,2,11,4,6]
# res = mergeSort(arr)