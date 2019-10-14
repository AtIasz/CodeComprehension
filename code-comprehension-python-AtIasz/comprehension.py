import random #importing the random function from the built-in functions

guesses_taken = 0 #number of guesses held in a variable

print('Hello! What is your name?')#prints out a welcome and asks a name
myName = input()#this line is holding the name variable

number = random.randint(1, 20)#a variable which takes a number from 1 to 20 randomly
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')#it tells the user that the program chosen a number from 1 to 20

while guesses_taken < 6: # a cycle which's going to continue to run until the guesses number hits 6
    print('Take a guess.')#tells the user to guess the number
    guess = input()#the number variable is held in the guess variable
    guess = int(guess)#converts the number from string to integer

    guesses_taken += 1#the guess_taken variable increased by 1

    if guess < number:#condition which's gonna pop up if the number is higher than the number he think of
        print('Your guess is too low.')#prints out encouraging the user to think a higher number

    if guess > number:#condition which's gonna pop up if the number is lower than the number he think of
        print('Your guess is too high.')#prints out encouraging the user to think a lower number

    if guess == number:#condition which's gonna pop up if the number is equal with the number he think of
        break

if guess == number:#condition if the number what the think of is the same with the number the user put in 
    guesses_taken = str(guesses_taken)#converts the guess_taken integer into a string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')#prints out the user's name + the guesses taken until he found the number

if guess != number:#conditon if the number is not equal with the number he think of
    number = str(number)#converts the generated number into a string
    print('Nope. The number I was thinking of was ' + number)#prints out the correct answer
