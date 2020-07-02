# C++ 用双链表+哈希
# Java用LinkedHashMap
# Python用OrderedDict
# class LRUCache:
#     def __init__(self, capacity: int):
#         from collections import OrderedDict
#         self.capacity=capacity
#         self.visited=OrderedDict()
#     def get(self, key: int) -> int:
#         if key not in self.visited: return -1
#         # last=True: 移动到末尾(默认为真)
#         # last=False: 移动到开头
#         self.visited.move_to_end(key)
#         return self.visited[key]
#     def put(self, key: int, value: int) -> None:
#         if key not in self.visited and len(self.visited)==self.capacity:
#             # last=True: LIFO(默认为真) 栈
#             # last=False: FIFO 队列
#             self.visited.popitem(last=False)
#         self.visited[key]=value
#         self.visited.move_to_end(key)

# 调用示例
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 有序字典来解决问题
class LRUCache:
    def __init__(self, capacity):
        from collections import OrderedDict
        self.capacity = capacity
        self.visited = OrderedDict()
    def get(self, key):
        # 取，先判空
        if key not in self.visited: return -1
        # 访问过,就移动到最后
        self.visited.move_to_end(key)
        return self.visited[key]
    def put(self, key, value):
        # 存，先判满
        # 只有这两个条件同时满足了才删除,其他情况都不用
        if key not in self.visited and len(self.visited) == len(self.capacity):
            # last=False 确保是从头部开始删的
            self.visited.popitem(last=False)
        self.visited[key] = value
        # 访问过,就移动到最后
        self.visited.move_to_end(key)

