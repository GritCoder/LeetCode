def solution(lists):
    # 按第一个值(左端点排序)
    lists.sort(key=lambda x: x[0])
    # lists.sort() # 与上面等价，不指定的话，默认就是第一个排序
    merged = []
    for item in lists:
        if not merged or merged[-1][1] < item[0]: # 左端点比上一个右端点值还大 那这俩区间不可能有交集
            merged.append(item)
        else:
            merged[-1][1] = max(merged[-1][1], item[1])
    return merged
print(solution([[1,3],[2,6],[8,10],[15,18]]))
