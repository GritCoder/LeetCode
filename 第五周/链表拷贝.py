class Node(object):
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
# 链表(深)拷贝 深搜 哈希表(字典)
def linkCopy(head):
    def dfs(head):
        if not head: return None
        if head in visited: # 若已访问 直接返回值 类似于剪枝了
            return visited[head]
        # 创建新节点
        copy = Node(head.val, None, None)
        visited[head] = copy
        copy.next = dfs(head.next)
        copy.random = dfs(head.random)
        return copy # 返回头结点的拷贝
    visited = {}
    return dfs(head)

# 广搜
# import collections
# def linkCopy(head):
#     visited = {}
#     def bfs(head):
#         if not head: return None
#         copy = Node(head.val, None, None)
#         queue = collections.deque()
#         queue.append(head)
#         visited[head] = copy
#         while queue:
#             tmp = queue.pop()
#             if tmp.next and tmp.next not in visited: # next节点 入队
#                 visited[tmp.next] = Node(tmp.next.val, None, None)
#                 queue.append(tmp.next)
#             if tmp.random and tmp.random not in visited: # random节点 入队
#                 visited[tmp.random] = Node(tmp.random.val, None, None)
#                 queue.append(tmp.random)
#             # 上面是入队操作 不是赋值 而且上面赋值的地方只是给head赋值了 还没有给两个指针赋值
#             # 理解区别和必要性 如果不加 会报错
#             visited[tmp].next = visited.get(tmp.next) # 设置节点的next值
#             visited[tmp].random = visited.get(tmp.random) # 设置节点的random值
#         return copy
#     return bfs(head)