import bisect
nums = [5,7,7,8,8,10]
begin = bisect.bisect_left(nums, 6)
end = bisect.bisect_right(nums, 6)
if begin != end:
    print([begin, end-1])
else:
    print([-1, -1])