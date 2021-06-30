#Sets - blazingly fast unordered Lists 
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}
# print(friends)
# print(friends_tuple)
# print(friends_set)

print(friends_set.intersection(my_friends_set)) # search result that are in both sets
print(friends_set.difference(my_friends_set)) # search result that are different
print(friends_set.union(my_friends_set)) # search result that has a set of names in all of the sets that have no duplicates

#Sets - blazingly fast unordered Lists 
#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()