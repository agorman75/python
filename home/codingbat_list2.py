# def count_evens(nums):
#     count = 0
#     for num in nums:
#       if num % 2:
#           count = count + 1
#     print(count)

# print(count_evens([2, 1, 2, 3, 4]))# → 3
# print(count_evens([2, 2, 0]))# → 3
# print(count_evens([1, 3, 5]))# → 0

# def big_diff(nums):
#     return max(nums) - min(nums)


# print(big_diff([10, 3, 5, 6]))# → 7
# print(big_diff([7, 2, 10, 9]))# → 8
# print(big_diff([2, 10, 7, 2]))# → 8

# def count_hi(str):
#   count = 0
#   for i in range(len(str)-1):
#     if str[i:i+2] == 'hi':
#       count += 1
#   return count

# print(count_hi('abc hi ho'))
# print(count_hi('ABChi hi'))
# print(count_hi('hihi'))
# print(count_hi('Hi is no HI on ahI'))
# print(count_hi('hiho not HOHIhi'))



# def sum13(nums):
#   if nums == [] or nums == '':
#     return 0
#   if 13 not in nums:
#     return sum(nums)
#   while 13 in nums:
#     del nums[nums.index(13):nums.index(13) + 2]
#   return sum(nums)

# print(sum13([1, 2, 2, 1]))# → 6
# print(sum13([1, 1]))# → 2
# print(sum13([1, 2, 2, 1, 13, 12]))# → 6
# print(sum13([]))
# print(sum13([13, 1, 2, 13, 2, 1, 13]))


# WORKING ON THIS #
# def sum67(nums):
#   if nums == [] or nums == '':
#     return 0
#   if 6 not in nums:
#     return sum(nums)
#   while 6 in nums:
#     del nums[nums.index(6):nums.index(7) + 1]
#   return sum(nums)


# print(sum67([1, 2, 2]))# → 5
# print(sum67([1, 2, 2, 6, 99, 99, 7]))# → 5
# print(sum67([1, 1, 6, 7, 2]))# → 4

def has22(nums):
  for num in nums:
    return num

print(has22([1, 2, 2]))# → True
# print(has22([1, 2, 1, 2]))# → False
# print(has22([2, 1, 2]))# → False