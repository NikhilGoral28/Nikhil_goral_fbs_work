#Python Program to Sort a List According to the Length of the Elements within the list.



words = ["apple", "banana", "kiwi", "grape", "strawberry", "fig"]

words.sort(key=len)

print("Sorted list by length:", words)
