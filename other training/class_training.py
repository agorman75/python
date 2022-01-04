

def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    print(count)
array_count9([1, 2, 9, 9])