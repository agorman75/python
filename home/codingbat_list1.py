# def first_last6(nums):
#   if 6 == nums[0] or 6 == nums[-1]:
#     return True
#   return False

# print(first_last6([1, 2, 6]))# → True
# print(first_last6([6, 1, 2, 3]))# → True
# print(first_last6([13, 6, 1, 2, 3]))# → False

# def same_first_last(nums):
#   if len(nums) >= 1 and nums[0] == nums[-1]:
#     return True
#   return False

# print(same_first_last([1, 2, 3]))# → False
# print(same_first_last([1, 2, 3, 1]))# → True
# print(same_first_last([1, 2, 1]))# → True

# def make_pi():
#   return [3,1,4]
# print(make_pi())

# def common_end(a, b):
#     if a[0] == b[0] or a[-1] == b[-1]:
#         return True
#     return False


# print(common_end([1, 2, 3], [7, 3]))# → True
# print(common_end([1, 2, 3], [7, 3, 2]))# → False
# print(common_end([1, 2, 3], [1, 3]))# → True

# def sums(nums):
#     return sum(nums)
# print(sum([1, 2, 3]))

# def rotate_left3(nums):
#   return nums[1:] + nums[:1]

# print(rotate_left3([1, 2, 3]))# → [2, 3, 1]
# print(rotate_left3([5, 11, 9]))# → [11, 9, 5]
# print(rotate_left3([7, 0, 0]))# → [0, 0, 7]

# def reverse3(nums):
#   return nums[::-1]
# print(reverse3([1, 2, 3]))

# def max_end3(nums):
#     if nums[0] >= nums[-1]:
#         return [nums[0]] * 3
#     return [nums[-1]] * 3

# print(max_end3([1, 2, 3]))# → [3, 3, 3]
# print(max_end3([11, 5, 9]))# → [11, 11, 11]
# print(max_end3([2, 11, 3]))# → [3, 3, 3]

# def sum2(nums):
#   if len(nums) == 1:
#     return nums[0]
#   if len(nums) == 0:
#     return 0
#   return nums[0] + nums[1]

# print(sum2([1, 2, 3]))# → 3
# print(sum2([1, 1]))# → 2
# print(sum2([1, 1, 1, 1]))# → 2

# def middle_way(a, b):
#     return [a[1], b[1]]

# print(middle_way([1, 2, 3], [4, 5, 6]))# → [2, 5]
# print(middle_way([7, 7, 7], [3, 8, 0]))# → [7, 8]
# print(middle_way([5, 2, 9], [1, 4, 5]))# → [2, 4]


# def make_ends(nums):
#     return [nums[0], nums[-1]]

# print(make_ends([1, 2, 3]))# → [1, 3]
# print(make_ends([1, 2, 3, 4]))# → [1, 4]
# print(make_ends([7, 4, 6, 2]))# → [7, 2]

# def has23(nums):
#     if 2 in nums or 3 in nums:
#         return True
#     return False

# print(has23([2, 5]))# → True
# print(has23([4, 3]))# → True
# print(has23([4, 5]))# → False

# def double_char(str):
#   for i in range(len(str)):
#       return i

# print(str('The'))


def count_evens(nums):
    count = 0
    for num in nums:
      if num % 2:
          count = count + 1
    print(count)

count_evens([2, 1, 2, 3, 4])