# def array_count9(nums):
#     count = 0
#     for num in nums:
#         if num == 9:
#             count = count + 1
#     print(count)

# array_count9([1, 2, 9, 9, 9])

# def array_front9(nums):
#   # First figure the end for the loop
#   end = len(nums)
#   if end > 4:
#     end = 4
  
#   for i in range(end):  # loop over index [0, 1, 2, 3]
#     if nums[i] == 9:
#       return True
#   return False