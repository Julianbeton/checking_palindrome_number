# Exercise 9: Check Palindrome Number

# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

# Expected Output:
# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number

def palindrome(number):
    original_number = number
    reversed_number = int(str(number)[::-1])

    if original_number == reversed_number:
       print("\033[1;32;40mOriginal number:", original_number)
       print("Yes. given number is a palindrome")

    else:
        print("Original number:", original_number)
        print("No. given number is not a palindrome")

palindrome(121)
palindrome(125)