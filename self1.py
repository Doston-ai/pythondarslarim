#Create a program that asks the user to guess a number between 1 and 10.

#If the guess is incorrect, the loop should continue prompting the user.
#Exit the loop when the correct number is guessed.

num = int(input("Enter a number beetwen 1 and 10: "))
print(num)

while num>10 or num<1:
    
    print(int(input("Enter a number beetwen 1 and 10: ")))
        
