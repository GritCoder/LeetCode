#给定一个长度为 n 的序列，每次向后数 m 个元素并删除，那么最终留下的是第几个元素？
'''
核心思想:
将上述问题建模为函数 f(n, m)，该函数的返回值为最终留下的元素的序号。
当我们知道了 f(n - 1, m) 对应的答案 x 之后，我们也就可以知道，
长度为 n 的序列最后一个删除的元素，应当是从 m % n 开始数的第 x 个元素
(因为n-1序列的元素是n序列删除第m个位置后的元素(位置为m % n)元素之后开始算的)
'''
# 数学 + 递归
def solution(n, m):

    def helper(n, m):
        if n == 0:
            return 0
        x = helper(n-1, m)
        return (m+x) % n

    return helper(n, m)

print(solution(10, 17))