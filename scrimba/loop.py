for num in range(1,5):
    a = "*" * num
    print(f"{a}{num}.Loops are great{a}")


num = 0
while num < 5:
    num += 1
    a = "*" * num
    print(f"{a}{num}.Loops are great{a}") 

# while num > -5:
#     num += -1
#     a = "*" * num
#     print(f"{a}{num}.Loops are great{a}") 

i=0
while i < 5:
    i+=1
    print(f"{i}."+ "*"*i + "Loops are awesome" + "*"*i*2)
    
# Three Loop Questions:
#1. What do I want to repeat?
#  -> message
#2. What do I want to change each time?
#  -> stars
#3. How long should we repeat?
#  -> 5 times
