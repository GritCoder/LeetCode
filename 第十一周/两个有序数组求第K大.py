# 两个有序数组 求第K大数
'''
这是一道非常经典的题。这题更通用的形式是，给定两个已经排序好的数组，找到两者所有元
素中第 k 大的元素。
O(m + n) 的解法比较直观，直接 merge 两个数组，然后求第 k 大的元素。
不过我们仅仅需要第 k 大的元素，是不需要“排序”这么复杂的操作的。可以用一个计数器，
记录当前已经找到第 m 大的元素了。同时我们使用两个指针 pA 和 pB，分别指向 A 和 B 数组的第
一个元素，使用类似于 merge sort 的原理，如果数组 A 当前元素小，那么 pA++，同时 m++；如果
数组 B 当前元素小，那么 pB++，同时 m++。最终当 m 等于 k 的时候，就得到了我们的答案，O(k)
时间，O(1) 空间。但是，当 k 很接近 m + n 的时候，这个方法还是 O(m + n) 的。
'''
# 思路一，归并排序的merge思路
def solution1(arr1, arr2, k):
    ans = []
    l1 = len(arr1)
    l2 = len(arr2)
    i, j = 0, 0
    while i < l1 and j < l2:
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    # if i >= l1:
    #     ans += arr2[j:]
    # if j >= l2:
    #     ans += arr1[i:]
    ans += arr1[i:]
    ans += arr2[j:]
    print(ans)
    # 因为是从小到大排序的，求第K大数索引要跟着变换一下
    return ans[l1+l2-k]
# 思路二，二分查找
def solution2(arr1, arr2):
    def helper(arr1, arr1_len, arr2, arr2_len, k):
        # 确保 arr1_len 长度小于 arr2_len 长度，这样当有个数组走完的时候，就不用判断是哪个了
        if arr1_len > arr2_len:
            return helper(arr2, arr2_len, arr1, arr1_len, k)
        # 长度小的数组已经没有值了,从 arr2_len 找到第k大的数
        if arr1_len == 0:
            return arr2[k-1]
        # 找到第 1 大的数,比较两个列表的第一个元素,返回最小的那个
        if k == 1:
            return min(arr1[0], arr2[0])
        # 避免出现index越界
        # 注意这个细节，一个是middle，一个是 k - middle ，因为并不见得任何时候 k 都是可以正常划分均匀的
        middle = min(k // 2, arr1_len)
        ex = k - middle
        if arr1[middle-1] < arr2[ex-1]:
            return helper(arr1[middle:], arr1_len-middle, arr2, arr2_len, k-middle)
        if arr1[middle-1] > arr2[ex-1]:
            return helper(arr1, arr1_len, arr2[ex:], arr2_len-ex, k-ex)
        else:
            return arr1[middle-1] # 二者相等的话，返回谁都一样
    # 这个二分，默认的是找的第 k 小，所以要转换一下
    # return helper(arr1, len(arr1), arr2, len(arr2), len(arr1)+len(arr2)-k+1)
    # 下面代码是求中位数的，可以转换成求第K大问题
    m, n = len(arr1), len(arr2)
    # 判断一下奇偶
    if (m + n) % 2 == 0:
        return (helper(arr1, len(arr1), arr2, len(arr2), (m + n) // 2) +
                helper(arr1, len(arr1), arr2, len(arr2), (m + n) // 2 + 1)) / 2
    else:
        return helper(arr1, len(arr1), arr2, len(arr2), (m + n) // 2 + 1)
print(solution2([1, 2, 3, 7], [4, 5, 6]))
# 暴力解法，三行代码
# 合并后排序,找第k大的数
# lst = arr1 + arr2
# lst.sort()
# print(lst[k - 1])
