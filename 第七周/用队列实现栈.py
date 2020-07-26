from collections import deque
from queue import Queue
class Mystack(object):
    # 双端队列实现
    def __init__(self):
        self.q = deque()
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1): # 移动前 n-1 个元素就行了  最后一个自然就在前面了
            self.q.append(self.q.popleft()) # 这样一进一出就跟栈的顺序一样了
    def pop(self):
        return self.q.popleft() # 因为push那里已经调整过顺序了 所以这里直接popleft就行
    def top(self):
        return self.q[0] # 一样 已经调整过顺序了
    def empty(self):
        return not len(self.q)

    # 普通队列实现
    # def __init__(self):
    #     self.q = Queue()
    # def push(self, x):
    #     self.q.put(x)
    #     for _ in range(self.q.qsize() - 1):
    #         self.q.put(self.q.get())
    # def pop(self):
    #     return self.q.get()
    # def top(self): # top只返回栈顶并不删除
    #     r = self.q.get() # 删除了元素 因此后面还要把这个元素添加进去
    #     self.q.put(r)
    #     # 必须用for循环添加 这样才不会改变原来的相对顺序
    #     for _ in range(self.q.qsize() - 1):
    #         self.q.put(self.q.get())
    #     # 不能直接像上面那样直接返回 self.q[0] 因为这个队列不是具有下标操作的对象
    #     return r
    # def empty(self):
    #     return not self.q.qsize()


