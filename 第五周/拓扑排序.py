# 注意 只有DAG图(有向无环图)才能产生拓扑序列
# 广搜
'''
我们使用一个队列来进行广度优先搜索。初始时，所有入度为 0 的节点都被放入队列中，它们就是可以作为拓扑排序最前面的节点，并且它们之间的相对顺序是无关紧要的。
在广度优先搜索的每一步中，我们取出队首的节点 u：我们将 u 放入答案中；
我们移除 u 的所有出边，也就是将 u 的所有相邻节点的入度减少 1。如果某个相邻节点 v 的入度变为 0，那么我们就将 v 放入队列中。
在广度优先搜索的过程结束后。如果答案中包含了这 n 个节点，那么我们就找到了一种拓扑排序，否则说明图中存在环，也就不存在拓扑排序了。
'''
# def solution(n, node_list):
#     import collections
#     edges = collections.defaultdict(list) # 用到了字典
#     indeg = [0] * n
#     res = []
#     # 这里算的是边 如 [1,0]表示1的先驱是0 即为边 0->1 即符合人的直观感受
#     for node in node_list:
#         edges[node[1]].append(node[0]) # 先驱节点是键，指向的边是值，一个先驱可能指向多个边(节点)
#         indeg[node[0]] += 1
#     print(edges)
#     q = collections.deque([u for u in range(n) if indeg[u] == 0])
#     # 等价写法
#     # q = collections.deque()
#     # for i in range(n):
#     #     if indeg[i] == 0:
#     #         q.append(i)
#     print(q)
#     while q:
#         u = q.popleft()
#         res.append(u)
#         for v in edges[u]: # 跟先驱相连的几条边
#             indeg[v] -= 1 # 每一条的入度都减去 1
#             if indeg[v] == 0:
#                 q.append(v)
#     if len(res) != n:
#         res = []
#     return res
# 深搜  python中list和stack等价
'''
visited[i] = 0 -> 未访问
visited[i] = 1 -> 有环
visited[i] = 2 -> 已正常访问
'''
def solution(n, node_list):
    import collections
    edges = collections.defaultdict(list)
    res = []
    visited = [0] * n
    for node in node_list:
        edges[node[1]].append(node[0]) # return res[::-1] 因为此时dfs先入栈的是后继节点
        # edges[node[0]].append(node[1]) # return res 因为此时dfs先入栈的是前驱节点
    # print(edges)
    import functools
    @functools.lru_cache(None)
    def dfs(i):
        if visited[i] == 1: # 有环
            return False
        if visited[i] == 2: # 正常访问 可以入栈
            return True
        visited[i] = 1 # 为 1 说明已访问，若又碰到 1 说明有环
        for j in edges[i]:
            if not dfs(j):
                return False
        visited[i] = 2
        res.append(i)
        return True
    for i in range(n):
        if not dfs(i): # 有环返回 False 因此前面判断加 not
            return [] # 如果这里的return执行了，那么程序就执行结束了
    return res[::-1]
print(solution(4, [[1,0],[2,0],[3,1],[3,2]]))