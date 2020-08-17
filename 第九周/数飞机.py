'''
给出飞机的起飞和降落时间的列表，用 interval 序列表示. 请计算出天上同时最多有多少架飞机？
对于每架飞机的起降时间列表：[[1,10],[2,3],[5,8],[4,7]], 返回3
解释:
第一架飞机在1时刻起飞, 10时刻降落.
第二架飞机在2时刻起飞, 3时刻降落.
第三架飞机在5时刻起飞, 8时刻降落.
第四架飞机在4时刻起飞, 7时刻降落.
在5时刻到6时刻之间, 天空中有三架飞机.
如果多架飞机降落和起飞在同一时刻，我们认为降落有优先权。
'''
# 思路：记录每一辆飞机的起始时间和降落时间，map中按key值排序，所以，从较小时刻开始，有飞机上升则飞机数+1，降落则-1，记录出现的最大值即可
def solution(nums):
    if not nums:
        return 0
    count, count_max = 0, 0
    time_dict, time_list = {}, []
    # 初始化 某个时刻飞机起飞为1 下降为-1
    for i in range(len(nums)):
        # 把开始时间和结束时间分别添加进列表 if判断是避免相同的时刻重复添加
        if nums[i][0] not in time_list:
            time_list.append(nums[i][0])
        if nums[i][1] not in time_list:
            time_list.append(nums[i][1])
        # time_dict实际上是个计数器
        if nums[i][0] in time_dict:
            time_dict[nums[i][0]] += 1
        else:
            time_dict[nums[i][0]] = 1
        if nums[i][1] in time_dict:
            time_dict[nums[i][1]] -= 1
        else:
            time_dict[nums[i][1]] = -1
    time_list.sort() # 必须要排序，因为存在区间包含的情况，不排序的话，各个飞机之间就是独立的了
    for i in range(len(time_list)):
        count += time_dict[time_list[i]]
        count_max = max(count, count_max)
    return count_max
print(solution([[1,10],[2,3],[5,8],[4,7]]))