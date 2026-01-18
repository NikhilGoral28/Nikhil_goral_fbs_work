#Write a program to print list after removing even numbers.



lst = [20,23,34,54,66,75,86,87,43,21]

odd_number = [x for x in lst if x % 2 != 0]

print("Original list: ", lst)
print("List after removing the even numbers: ", odd_number)