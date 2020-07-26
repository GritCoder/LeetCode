class Myqueue(object):
    def __init__(self):
        self.stack1 = [] # 主栈
        self.stack2 = [] # 辅栈
    def push(self, x):
        self.stack1.append(x)
    def pop(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop()) # 这样 stack2 的顺序就跟队列一样了
        r = self.stack2.pop()
        while self.stack2: # 模拟完了再还原回去
            self.stack1.append(self.stack2.pop())
        return r
    def peek(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        r = self.stack2[-1]
        while self.stack2: # 模拟完了再还原回去
            self.stack1.append(self.stack2.pop())
        return r
    def empty(self):
        return not len(self.stack1)