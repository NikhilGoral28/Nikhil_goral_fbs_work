#Write a program to input any alphabet and check whether it is vowel or consonant.


alphabet = input("Enter an alphabet: ").lower()


if alphabet in ['a', 'e', 'i', 'o', 'u']:
    print(f"The alphabet '{alphabet}' is a vowel.")
else:
    print(f"The alphabet '{alphabet}' is a consonant.")