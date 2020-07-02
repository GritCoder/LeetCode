# 对于序列化，从根节点开始，如果节点存在，则将值存入输出字符串流，然后分别对其左右子节点递归调用序列化函数
# 对于反序列化，先读入第一个字符生成一个根节点，然后再对根节点的左右子节点递归调用去序列化函数
class binTree():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

import collections
class Solution:
    def serialize(self, root):
        # lis = collections.deque()
        # lis.appendleft(5)
        vals = []
        def preOrder(root):
            if not root:
                vals.append('#')
            else:
                vals.append(str(root.data))
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ''.join(vals)
    def deserialize(self, data):
        # 具体执行的时候data是从文件等里面加载的，知晓一下
        # vals 此时为 deque ,本质上是一个list，只不过可以从左边追加/弹出元素
        vals = collections.deque(val for val in data.split())
        def build():
            if vals:
                val = vals.popleft()
                if val == '#':
                    return None
                root = binTree(int(val)) # 创立节点
                root.left = build()
                root.right = build()
                return root
        return build()



# 建立二叉树是以层序遍历方式输入，节点不存在时以 'None' 表示
# def creatTree(nodeList):
#     if nodeList[0] == None:
#         return None
#     head = binTree(nodeList[0])
#     Nodes = [head]
#     j = 1
#     for node in Nodes:
#         if node != None:
#             node.leftChild = (binTree(nodeList[j]) if nodeList[j] != None else None)
#             Nodes.append(node.leftChild)
#             j += 1
#             if j == len(nodeList):
#                 return head
#             node.rightChild = (binTree(nodeList[j])if nodeList[j] != None else None)
#             j += 1
#             Nodes.append(node.rightChild)
#             if j == len(nodeList):
#                 return head

