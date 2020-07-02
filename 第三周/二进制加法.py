def solution(a:str, b:str):
    # 转成二进制整数
    num_a = int(a, 2)
    num_b = int(b, 2)
    # 返回整数的二进制形式
    # 结果是正数的情况，从2切片，因为前两位为0b
    # 结果是负数的情况，从3切片，因为前三位为-0b
    return bin(num_a+num_b)[2:]
