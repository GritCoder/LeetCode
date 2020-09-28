def isValid(s):
    left = []
    dic = {')':'(', ']':'[', '}':'{'}
    for c in s:
        if c == '(' or c == '[' or c == '{':
            left.append(c)
        else:
            if left and dic[c] == left[-1]:
                left.pop()
            else:
                return False
    # 如果left栈为空，说明已完全匹配完，否则就返回False
    return True if not left else False

print(isValid('(())'))
