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

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      count += 1
  return count

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))
print(count_hi('Hi is no HI on ahI'))
print(count_hi('hiho not HOHIhi'))