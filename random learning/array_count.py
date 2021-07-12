# def array_count9(nums):
#     count = 0
#     for num in nums:
#         if num == 9:
#             count = count + 1
#     print(count)

# array_count9([1, 2, 9, 9, 9])

def array_front9(nums):
    for num in nums:
        if num[:3] == 4:
            return True

array_front9([1, 2, 9, 3, 4])