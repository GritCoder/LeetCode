def solution(s):
    # 与上一题不同，这里res可能代表左括号，也可能代表右括号，上一题只考虑左括号就行了，因此用left表示了，明白区别
    res = 0
    # need 含义在两个题中都一样
    need = 0
    for c in s:
        if c == '(':
            need += 2
            # 一个隐含的条件，右括号的数量必须为偶数
            if need % 2 == 1:
                # 插入一个右括号
                res += 1
                # 右括号的需求 -1
                need -= 1
        if c == ')':
            need -= 1
            if need == -1:
                # 需要一个左括号
                res += 1
                # 右括号需求置为 1
                need = 1
    return res + need
print(solution("(()))"))
        