# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
# 通俗点理解就是，b[i]的值就是除去a[i]之外，其余所有元素的乘积

# 暴力法 提交超时
def solution1(a):
    b = []
    for i in range(len(a)):
        left = a[:i]
        right = a[i+1:]
        if not left:
            left = [1]
        if not right:
            right = [1]
        tmp = 1
        for item in left:
            tmp *= item
        for item in right:
            tmp *= item
        b.append(tmp)
    return b

# 优化解法，上下三角，有一定规律和技巧
# 具体思路可以参考 https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/solution/mian-shi-ti-66-gou-jian-cheng-ji-shu-zu-biao-ge-fe/ 动画
# 本质上是dp，只不过省去了额外空间的申请
def solution2(a):
    b, tmp = [1] * len(a), 1
    for i in range(1, len(a)):
        b[i] = a[i-1] * b[i-1] # 下三角 b[0]不用算
    for i in range(len(a) - 2, -1, -1):
        tmp *= a[i+1] # 上三角
        b[i] *= tmp # 上下三角相乘
    return b
print(solution2([1,2,3,4,5]))

