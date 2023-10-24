#create a guessing game, user have access to 3 attempts to enter
#any number btw 0 and 9 after which the game will end, if the
#user entered the right number, the user win the game.

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 0 and 9. Can you guess it? You have just 3 attempts")
correctnumber = 6
for i in range(3):
    guess = int(input('Enter your guess:'))
    if guess < correctnumber:
        print("Too low!")
    elif guess > correctnumber:
        print("Too high")
    else:
     print(f"Congratulations! You guessed the correct number in {i + 1} attempts" )
     break
 
 
right_number = 4
number_of_guesses = 3
guess_count = 0
print('you have 3chances to choose a number between 0 and 9, after 3 attempts, this game will terminate')
while guess_count < number_of_guesses:
    guess = int(input('Guess the right number:'))
    guess_count += 1
    if guess == right_number:
        print('Correct, you won this game')
        break
    else:
        print('you have exceeded the number of attempts')