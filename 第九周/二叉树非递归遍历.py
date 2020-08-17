# 先序
def preOrder(root):
    stack = []
    # 循环条件必须这样写，不然里面循环结束了就没啥事了，右孩子没有遍历出来
    while stack or root:
        while root:
            print(root.val)
            stack.append(root)
            root = root.lchild
        root = stack.pop()
        root = root.rchild
# 中序
def inOrder(root):
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.lchild
        root = stack.pop()
        print(root.val)
        root = root.rchild
# 后序 注意要用两个栈 第一个按左-右-根入栈 则出栈顺序为根-右-左 把这个顺序入栈stack2中 最后stack2再依次出栈即为左-右-根后序结果
def postOrder(root):
    stack1 = [root]
    stack2 = []
    while stack1:
        root = stack1.pop()
        stack2.append(root)
        if root.lchild:
            stack1.append(root.lchild)
        if root.rchild:
            stack1.append(root.rchild)
    while stack2:
        print(stack2.pop().val)
# 层序 用队列
def levelOrder(root):
    from collections import deque
    q = deque([root])
    while q:
        root = q.popleft() # 注意这是双端队列，如果当普通队列必须用popleft，用pop的话就不是队列了 等价于栈了
        print(root.val)
        if root.lchild:
            q.append(root.lchild)
        if root.rchild:
            q.append(root.rchild)

