# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)


# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print(f"The 'i' variable, which is now '{i}' is no logner less than 6")


# fruits = ["apple", "banana", "cherry"]
# # for x in fruits:
# #     print(x)

# # In the loop, when the item value is "banana", jump directly to the next item.
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

# Exit the loop when x is "banana".
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         break
#     print(x)
    

#Use the range function to loop through a code set 6 times.
# for x in range(6):
#     print(x)

# def my_function(x):
#     return x + 5

# If you do not know the number of arguments that will be passed into your function,
# there is a prefix you can add in the function definition, which prefix? The * arguement
# def my_function(*x):
#     print("hello " + x[2])

# If you do not know the number of keyword arguments that will be passed into your function,
# there is a prefix you can add in the function definition, which prefix? The ** arguement

# same_first_last = ([1, 2, 3, 4, 5, 13])
# def same_first_last(nums):
#     if len(nums) >= 1 and elif nums[0] == nums[nums]:
#         return True

#     else:
#         return False
#     print(same_first_last(nums))

# cigars = range(40,61)
# for a in cigars:
#     print(a)

# def cigar_party(cigars, is_weekend):
#   if is_weekend:
#     return (cigars >= 40)
#   else:
#     return (cigars >= 40 and cigars <= 60)

# print(cigar_party(20,False))

input1 = input("Give me the inputs \n")
input2 = input("Tell me two \n")
if input1 or input2 == int():
  a = str(input1)
  b = str(input2)
print(a + " " + b)