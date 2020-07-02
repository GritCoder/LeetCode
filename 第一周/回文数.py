# 最基本的思路，循环一半，逐一比较即可
def solution(inputs):
    length = len(inputs)
    res = True
    for i in range(int(length/2) + 1):
        if inputs[i] == inputs[length-i-1]:
            continue
        else:
            res = False
    # print(res)
    return res

if __name__ == "__main__":
    inputs = input()
    solution(inputs)