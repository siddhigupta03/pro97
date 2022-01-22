print("Number guessing game.")
print("Guess a number between 1-9. You only have 5 chances.")
chances=5
while(chances<=5):
    guess=int(input("Enter your guess: "))
    if(guess<9):
        print("Your guess is very low. Enter a number greater than",guess)
    elif(guess==9):
        print("Congratulations!! You win!")
    chances = chances-1
    if(chances==0):
        print("You lose!!","The number is 9.")
        break