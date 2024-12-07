#3. Sum of Numbers
#Write a program that keeps asking the user to input a number.

#Stop when the user enters 0.
#Print the sum of all entered numbers (excluding 0).

num = int(input("enter a number(except 0): "))
print(num)

while num == 0:
    num = int(input("enter a number(except 0): "))
    print(num)