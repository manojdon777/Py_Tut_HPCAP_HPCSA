# a = "111222"
# b = True
# c = 3.14
# print(type(a))
# print(type(b))
# print(type(c))

# if 2>3:
# 	print("Yes")

# else:
# 	print("No")


# if 7>3:
# 	print("Yes")

# elif 3>2:
# 	print("No")


# 80>A
# 50>B
# 30>C
# mark = 29
# if mark > 80:
# 	print("A")
# elif mark > 50:
# 	print("B")
# elif mark > 30:
# 	print("C")
# else:
# 	print("FAIL")


# for i in range(5):
# 	print(i)

# for i in range(2, 5):# 5 is excluded
# 	print(i)
# print()



# for i in [2, 3, 4]:# 5 is excluded
	# print(i)

# print(type(range(5))) # 0, 1, 2, 3, 4

list1 = [1, 2, 55, 7, 'XYZ', True]
# for element in list1:
# 	print(element)
# for element in list1:
# 	print(type(element))
# for index in range(len(list1)):
# 	print( list1[index] )
# for index in range(len(list1)):
# 	print( type(list1[index] ))

# *
# **
# ***
# ****


# abc = input("Enter number: ")
# print(abc, type(abc))


# print(11, end = ' %%%%%%')
# print(22)

# print('1','2','3','4', sep = '')

# while condition:
# 	block
# i = 0
# while i < 5:
# 	print(i)
# 	i += 1

# 100 < 100 is always false
# 100 == 100	is true
# 100 <= 100	is true
# 100 >= 100	is true
# if 100 < 100:
# 	print("True")
# else:
# 	print("False")
# if 100 == 100:
# 	print("True")
# else:
# 	print("False")

# list1 = [11,22,33,44,55] # Mutable
# list1[2] = 'ABC'
# print(list1)

# tup1 = (11,22,33,44,55) # Immutable
# # tup1[2] = 'ABC'
# print(tup1)

# tup1 = (55, 77, 77, 99, 87)
# # print(tup1)

# list1 = list(tup1)
# list1.append("CDAC")
# list1[2] = 'ABC'
# print(list1)
# tup1 = tuple(list1)
# print(tup1)

# print(type(list1))
# print(type(tup1))






# list, tuple, set, dictionary, frozenset

# list1 = []
# print(list1)
# list1 = list()
# print(list1)

# list1 = []
# list1.append(11)
# # print(list1)
# list1.append(22)
# # print(list1)
# list1.append(11)
# # print(list1)
# list1.append(44)
# print(list1)
# list1.insert(2, 'XYZ')
# print(list1)

# list1 = ['11','22','33','44','55','66']
# list1.pop()
# print(list1)

# list1.pop(2)
# print(list1)

# list1 = ['11','22','33','44','55','66', 2]
# list1.remove(2)
# print(list1)
# list1 = ['11','22','33','44','55','66']
# list1.reverse()
# print(list1)



# tup1 = (55, 77, 77, 99, 87)
# print(tup1)
# tup1 = ()
# print(tup1)
# tup2 = tuple()
# print(tup1)


# tup1 = (55, 77, 123, 99, 87)

# print(tup1[2])
# tup1 = (55, 77, 123, 99, 87)
# for tup_element in tup1:
# 	print(tup_element)

# set1 = {5,1,4,8} # unordered
# print(set1)
# print(type(set1))

# # ordered
# list1 = [55, 77, 123, 99, 87]
# for index in range(len(list1)):
# 	print(index, list1[index])

# # unordered
# set1 = {55, 77, 123, 99, 87}
# for index in range(len(set1)):
# 	print(index, set1[index])


# set1 = set()
# print(type(set1))
# set2 = {}
# print(type(set2))

# Slicing
# abc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# [:]
# print(abc[2:10]) # second arg after : is excluded
# print(abc[:7])
# print(abc[4:])

# [::]
#        [start_index                 : end_index         : step]
#default [starting from first element : all list upto end : step by 0]
# print(abc[2:10:2])
# print(abc[2:10:3])
# print(abc[2:10:])

# #Negative indexing
# xyz = [00,11,22,33,44,55,66,77,88,99]
# # print(xyz[4])
# print(xyz[-3])
# print(xyz[-10])

# abc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(abc[9:1:-2])
# print(abc[2:])
# print(abc[2:10])
# print(abc[2:10:])
# print(abc[-8:])
# print(abc[::-1])
# abc.reverse()
# print(abc)

# string1 = "0123456789"
# for i in string1:
# 	print(i, end = '')

# for index in range(len(string1)):
# 	print(index, string1[index])

# print(string1[9:1:-2])
# print(string1[2:])
# print(string1[2:10])
# print(string1[2:10:])
# print(string1[-8:])
# print(string1[::-1])

# tup1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# print(tup1[9:1:-2])
# print(tup1[2:])
# print(tup1[2:10])
# print(tup1[2:10:])
# print(tup1[-8:])
# print(tup1[::-1])


# abc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(abc[::])
# print(abc[0:10:1])
# print(abc[2::3])

# dict1 = {}
# print(type(dict1))
# dict2 = dict()	
# print(type(dict2))

# {key : value}
# {Immutable : Mutable or Immutable}
# DD  ={}
# DD[3] = 'ABC'
# DD[290] = (44,66,88)
# print(DD)
# DD = {1:"aaa", 2:"bbb", 3:"ccc"}
# print(DD.keys())
# print(DD.values())
# print(DD.items())
# print(DD)
DD = {1:"aaa", 2:"bbb", 3:"ccc"}
for abc in DD.keys():
	print(abc)
for abc in DD.values():
	print(abc)
for abc in DD.items():
	print(abc)

print(type(DD.items()))