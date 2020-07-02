class LinkNode:
    def __init__(self, x):
            self.val = x
            self.next = None
class LinkList:
    def __init__(self):
        self.head = None
    def initList(self, data):
        self.head = LinkNode(data[0])
        r = self.head
        p = self.head
        for i in data[1:]:
            node = LinkNode(i)
            p.next = node
            p = p.next
        return r
    def printList(self, head):
        if head == None:
            return
        node = head
        while(node != None):
            print(node.val, end=' ')
            node = node.next
    def search(self, head, keyword):
        pass
    def insertList(self, head, keyword, newNode): # keyword是查找关键字
        newNode = LinkNode(newNode) # 创建结点
        pGuard = self.search(head, keyword) # pGuard是插入位置前的结点指针
        # 插入pGuard之后
        newNode.next = pGuard.next # 先连
        pGuard.next = newNode # 后断
    def delLink(self, head, keyword):
        pGuard = head
        if(head.val == keyword):
            p = head # 此时的头结点是待删结点
            head = head.next # 先连
            del p # 后删
        else:
            while(pGuard.next != None):
                if(pGuard.next.val == keyword):
                    p = pGuard.next # p为待删结点
                    pGuard.next = p.next # 先连
                    del p # 后删

if __name__ == "__main__":
    data = [1, 3, 11, 9, 5]
    l = LinkList()
    l1 = l.initList(data)
    l.printList(l1)
