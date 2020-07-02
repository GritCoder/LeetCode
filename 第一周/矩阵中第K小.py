# 先转换成一维列表，排序后再输出
# def solution(matrix, k):
#     # print(len(matrix)) # 矩阵的行数  len(matrix[0])为矩阵的列数
#     lis = []
#     for item in matrix:
#         lis.extend(item)
#     lis.sort()
#     # print(lis[k-1])
#     return lis[k-1]
# 矩阵二分查找
# def solution(matrix, k):
#     row, col = len(matrix), len(matrix[0])
#     low = matrix[0][0]
#     high = matrix[row-1][col-1]
#     while(low < high):
#         mid = (low + high) / 2
#         # row = col 因为是方阵, 若不是方阵也简单，同时把row, col传进去即OK
#         count = find_count(matrix, mid, row)
#         if count < k:
#             low = mid + 1
#         else:
#             high = mid
#     ans = int(low)
#     return ans
# def find_count(matrix, mid, row):
#     i = row-1; j = 0; count = 0
#     # 定义搜索起点很重要，从左下角开始搜索
#     while(i > -1 and j < row):
#         if matrix[i][j] > mid:
#             i -= 1
#         else:
#             # 若 <= mid, 则此元素上方的此列元素必定小于mid，故将此列 <=mid的数目（i+1）
#             # 累加至count,然后向右走一格，继续循环
#             count += (i + 1)
#             j += 1
#     return count

# if __name__ == "__main__":
#     n, k = map(int, input().split())
#     # 二维矩阵输入，看作若干个一维列表，然后追加
#     matrix = []
#     for i in range(n):
#         tmp = list(map(int, input().split()))
#         matrix.append(tmp)
#     # print(matrix)
#     solution(matrix, k)

# 普通二分查找(复习回顾)
def bin_search(lis, val):
    if not lis:
        return
    # 下标从0开始的，返回的是真正索引
    begin = 0; end = len(lis) - 1
    while(begin < end):
        mid = int((begin + end) / 2)
        if lis[mid] == val:
            return mid
        elif lis[mid] > val:
            end = mid - 1
        else:
            begin = mid + 1
print(bin_search([1,2,3,4,5,6], 5))