# 最小生成树(Minimum Spanning Tree) ：带权连通图中代价最小的生成树称为最小生成树
# 加点算法Prim和加边算法Kruskal(略过 不细研究了)
'''
prim
1）以某一个点开始，寻找当前该点可以访问的所有的边
2）在已经寻找的边中发现最小边，这个边必须有一个点还没有访问过，将还没有访问的点加入我们的集合，记录添加的边
3）寻找当前集合可以访问的所有边，重复2的过程，直到没有新的点可以加入
4）此时由所有边构成的树即为最小生成树
# 多少跟最短路径的思路有点类似
'''
'''
样例 输入n个城市，然后接着输入n x n矩阵代表任意两城市间代价，求最小代价连接n个城市
3
0 1 2
1 0 4
2 4 0
'''
def prim(n, matrix):
    flag =  [0] * n
    flag[0] = True  # 标记第一个节点
    totalcost = 0
    min_cost, index = float('inf'), 0
    for i in range(n):
        for j in range(n):
            if not flag[j] and matrix[i][j] < min_cost:
                min_cost = matrix[i][j]
                index = j
        flag[index] = True
        totalcost += matrix[i][index]
        # print(matrix[i][index])
        for j in range(n):
            if not flag[j] and matrix[i][index] < matrix[i][j]:
                matrix[i][j] = matrix[i][index]
    return totalcost

n = int(input())
matrix = []
for i in range(n):
    lis = list(map(int, input().split()))
    matrix.append(lis) # 实际输入最好采用双循环 这样不可到的点可以标记为无穷  知道就行
# print(matrix)
print(prim(n, matrix))