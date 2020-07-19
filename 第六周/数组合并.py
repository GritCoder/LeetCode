# 数组合并 本质上就是归并排序的merge过程
def mergeArray(a, b):
    if not a:
        return b
    if not b:
        return a
    i, j = 0, 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else: # 这里包含了大于等于的情况了 都一样 因此上面不用加等号
            res.append(b[j])
            j += 1
    # 把剩余的元素copy进res中
    print(i, j)
    if i >= len(a):
        res += b[j:]
    else:
        res += a[i:]
    return res

a = [1,2,3]
b = [2,4,7]
print(mergeArray(a, b))