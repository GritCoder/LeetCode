'''
给定一个长度为N的整型数组arr,其中有N个互不相等的自然数1~N，请实现arr的排序，但是不要把下标0~N-1位置上的数通过直接赋值的方式替换成1~N。
时间复杂度为O(N),额外空间复杂度为O(1)
'''
def solution(arrs):
    n = len(arrs)
    for i in range(n):
        while arrs[i] != i + 1:
            # 核心思想 arr[i]应放在arr[i]-1位置上 故arr[i]和arr[arr[i]-1]交换值
            arrs[arrs[i] - 1], arrs[i] = arrs[i], arrs[arrs[i] - 1]
            print(arrs)
solution([1,2,4,5,3,6])