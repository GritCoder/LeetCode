array = [5,2,3,4,7]
# 一句话实现快排
# quick_sort = lambda array: array if len(array) <= 1 else quick_sort([
#     item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([
#     item for item in array[1:] if item > array[0]])
# print(quick_sort(array))
# 常规思路实现快排
def partition(array, left, right):
    p = array[left] # -> p = array[right] (1)
    # 先从右边找比枢轴小的 然后再从左边找比枢轴大的
    # 次序不可乱，如果乱了 对应(1)(2)(3)处跟着改变
    while(left < right):
        while(left < right and array[right] >= p):
            right -= 1
        array[left] = array[right]
        # 上下这两段代码不可交换位置 交换了就报错 索引值交换的问题 不细研究了
        # 如果非要交换 则需要改一下代码 看(1)(2)(3)
        # 即 若轴初始化左边的了，则从右边开始循环 最后轴返回也是左边...
        # 若初始化右边的了...则反之。也不用死记了，理解就行了
        while(left < right and array[left] <= p):
            left += 1
        array[right] = array[left]
    # 更新枢轴
    array[left] = p # -> array[right] = p (2)
    # 返回枢轴
    return left # -> right (3)
def quick_sort(array, left, right):
    if left <= right:
        mid = partition(array, left, right)
        quick_sort(array, left, mid-1)
        quick_sort(array, mid+1, right)
    return array
# print(quick_sort(array, 0, 4)) # 传的是索引值，注意一下，都是对索引进行的操作

# 数组中寻找第K小，就是快排的一个改版，具体实现如下
# def kmin(array, left, right, k):
#     if left <= right:
#         mid = partition(array, left, right)
#         if mid == k-1: # 因为处理是按照索引来的，0开始，所以对齐索引要减去1
#             return array[mid]
#         elif mid < k-1: # 说明在右区间
#             return kmin(array, mid + 1, right, k)
#         else:
#             return kmin(array, left, mid-1, k)
# k = 5
# print(kmin(array, 0, len(array)-1, k))


import heapq

#lis = heapq.nsmallest(3, array)
#print(lis[-1])

# heapq.heapify(array) # inplace操作, 没有返回值
# print(array) # -> [2, 4, 3, 5, 7] 相当于堆的初始化(建堆)，此时并不是有序的

# Python堆/优先队列实现第K小

# python里面实现的是最小堆，pop操作返回的是最小值
def heapsort(array):
    h = []
    for item in array:
        heapq.heappush(h, item)
        if len(h) > 3: # 不能大于3就break，因为这样不能保证最后里面的元素是最大(小)的
            heapq.heappop(h)
    print(h)
    return heapq.heappop(h)
print(heapsort(array))