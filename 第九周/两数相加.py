# 考虑两种情况: 位数不相等和进位
class linkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def solution(L1, L2):
    # 链表相关操作，哑结点一般是必备的
    dummy = linkNode(None)
    p = dummy
    # 进位
    s = 0
    # 这个循环体写的妙
    while L1 or L2 or s:
        s += (L1.val if L1 else 0) + (L2.val if L2 else 0)
        p.next = linkNode(s % 10) # 值
        p = p.next
        s //= 10 # 进位数
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
    return dummy.next