parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]

parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print "This parrot is " + state

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
numbers_in_order = sorted(numbers)

print numbers_in_order

if numbers == numbers_in_order:
    print "The lists are equal"
else:
    print "The lists are not equal"

if numbers_in_order == sorted(numbers):
    print "The lists are equal"
else:
    print "The lists are not equal"

list1 =  []
list2 = list()

print "List 1: {}".format(list1)
print "List 2: {]".format(list2)

if list1 == list2:
    print "The list are equal"

print(list("The lists are equal"))

another_even_sort = even
another_even_sort.sort(reverse=True)
print even

for number_set in numbers:
    print number_set

    for value in number_set:
        print value
        
