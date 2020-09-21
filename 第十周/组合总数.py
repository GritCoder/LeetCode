# 一般碰见求所有解的问题，都是回溯+减枝的思路(递归或者深搜)
# 没有严格按照回溯算法来写，这里需要了解的知识点是
# [1, 2] + [3] 语法生成了新的列表，一层一层传到根结点以后，直接 res.append(path) 就可以了；
# 基本类型变量在传参的时候，是复制，因此变量值的变化在参数里体现就行
def solution(arrs, target):
    # n = len(arrs)
    ans = []
    def backtrack(arrs, tmp):
        # 下面的return就相当于减枝了，减小了搜索空间，不用继续往前走了  
        if sum(tmp) > target:
            return
        if sum(tmp) == target:
            ans.append(tmp)
            return
        # 注意range里面不能是 n 因为递归的时候，对arrs进行了切片，这样长度就变了，不是原来的长度了，写 n 的话会报index错误
        for i in range(len(arrs)):
            backtrack(arrs[i:], tmp + [arrs[i]])
    backtrack(arrs, [])
    return ans
print(solution([2,3,6,7], 7))