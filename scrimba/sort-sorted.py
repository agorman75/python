# print('sort() and sorted()')
# print('Immutability and return values')

my_list = [1,5,3,7,2] #mutable -- can be changed
my_dict = {'car':4,'dog':2,'add':3,'bee':1} #mutable
my_tuple = ('d','c','e','a','b') #immutable
my_string = 'python' #immutable

#lists
# print(my_list, 'original')
# print(my_list.sort())
# print(sorted(my_list)) #new list
# print(reversed(my_list)) #needs to have an object like below
# print(list(reversed(my_list)))
# # print(my_list, 'new')
# Can use slicing: print(my_list[::-1])

#dictionary
# print(my_dict,'original')
# print(sorted(my_dict.items()))
# print(sorted(my_dict.values(), reverse=True))
# print(my_dict,'new')



my_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_list, key = abs)) #abs = absolute function
print(sorted(my_llist)) #sorted by the first element
print(sorted(my_llist, key = lambda item :item[-1]))