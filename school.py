#append
my_list=[1,2,3]
number=4
my_list.append(number)
print(my_list)


#+=
my_list=[1,2,3]
my_list+=[4,5]
print(my_list)


#extend
my_list=[1,2,3]
my_list.extend([4,5,6])
print(my_list)


#unpack
my_list=[1,2,3]
second_list=[4,5,6]
print(*my_list,*second_list)



#itertools
import itertools
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
combain=itertools.chain(a,b,c)
print=(list(combain))


#list
my_list=[1,2,3]
new_list=list(my_list)+[4]
print(new_list)


#insert
my_list=[1,2,3]
my_list.insert(len(my_list),4)
print(my_list)


#append
my_list=[1,2,3]
number=4
my_list.append(number)
print(my_list)

#extend
my_list=[1,2,3]
my_list.extend([4,5])
print(my_list)


#+=
my_list=[1,2,3]
my_list+=[4,5]
print(my_list)


#insert
my_list=[1,2,3]
my_list.insert(len(my_list),4)
print(my_list)


#new_list
my_list=[1,2,3]
new_list=my_list+[4,5]
print(new_list)
print(my_list)


#unpacking
my_list=[1,2,3]
second_list=[4,5,6]
print(*my_list,*second_list)


#iter tools
import itertools
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
combain=itertools.chain(a,b,c)
print(list(combain))


#list
my_list=[1,2,3]
new_list=list(my_list)+[4]
print=(new_list)