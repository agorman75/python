# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
# # answer = dict(zip(list1, list2))

# # print(answer)

# def answer(list1,list2):
#     return dict(zip(list1,list2))

# print(answer(list1, list2))

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
print({k:v for k,v in person})
print(dict(person))