# 堆是一种完全二叉树(因此用数组来存储比较有效，空间利用率高)
# 堆有两种类型: 最大堆(每个结点的值都大于或等于左右孩子结点) 最小堆(每个结点的值都小于或等于左右孩子结点)
def heapIfy(arr, n, i):
    largest = i # 构建最大堆
    l = 2 * i + 1 # 左右孩子结点
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]: # 注意细节，这里是largest索引而非i，因为上面if语句可能执行
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # 交换
        heapIfy(arr, n, largest) # 某个结点交换后，可能会影响堆结构，所以要递归的进行再构建
def heapSort(arr):
    n = len(arr)
    # 构建一个堆(即其他不管，先让堆顶元素保持最大或者最小)
    # i 是某个根结点
    # 因为有一半元素的左右孩子是不在数组中的，因此循环改成 for i in range(int(n/2),-1,-1)
    # 也是可以的(已测试，完全正确)
    for i in range(n, -1, -1): # 没明写，但其实已经包含了一个辅助位了
        heapIfy(arr, n, i)     # 因为是倒着构建堆的(这样可以减少一半的上浮次数)
                               # 所以辅助位是n而不是0了!
    # 每一个元素都跟第一个(若是正向建堆，则跟最后一个交换)交换
    for i in range(n-1, 0, -1): # 都跟第一个交换，所以索引到1就行了，自己跟自己没必要交换
        arr[i], arr[0] = arr[0], arr[i]
        heapIfy(arr, i, 0)
    return arr
arr = [4, 3, 2, 1]
print(heapSort(arr)) #说白了，最大堆就是从小到大排列的
