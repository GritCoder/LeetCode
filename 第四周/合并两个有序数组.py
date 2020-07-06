def solution(arr1, m, arr2, n):
    i = j = 0
    # 把两个数组合并到另一个当中
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        else:
            arr1.insert(i, arr2[j])
            j += 1
    if i >= m:
        # m+j是因为已经存进来j个元素了，索引要跟着变化
        arr1[m+j:] = arr2[j:]
    else:
        arr1= arr1[:m+n]
    #
    # 下面是把两个数组合并到第三个数组当中
    #     if arr1[i] <= arr2[j]:
    #         res.append(arr1[i])
    #         i += 1
    #     else:
    #         res.append(arr2[j])
    #         j += 1
    # print(i, j)
    # res += arr1[i:]
    # res += arr2[j:]
    # return res
    return arr1
print(solution([2,0], 1, [1], 1))