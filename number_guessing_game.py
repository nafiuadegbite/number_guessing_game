import random

def number_guess_game(level, range):
    number_of_guess = level
    player_name = input("Hello! What's your name: ")
    print('Well, ' + player_name + ', I am thinking of a number between 1 and '+ str(range) + ".")
    print("You have "+ str(number_of_guess) +" guesses")
    number = random.randint(1, range)
    while number_of_guess > 0:
        try:
            guess = int(input("Guess a number: "))
            if guess == number:
                print("You got it right!")
                break
            elif guess < number:
                print("Your guess is too low")
            else:
                print("Your guess is too high")
            number_of_guess -= 1
            print("That was wrong, you have "+str(number_of_guess)+" remaining guess(es)")
            if number_of_guess == 0:
                print("GAME OVER!!! The number is", number)
        except ValueError:
            print("Please enter a valid number")
                
while True:
    print("Welcome, please enter a number to start the game \n 1. Easy \n 2. Medium \n 3. Hard \n 4. End Game")
    try:
        choose_level = int(input(""))
        if choose_level == 1:
            number_guess_game(6, 10)
        elif choose_level == 2:
            number_guess_game(4, 20)
        elif choose_level == 3:
            number_guess_game(3, 50)
        elif choose_level == 4:
            print("Thanks for playing")
            break
        else:
            print("Please Choose a number between 1 to 4")
    except ValueError:
        print("Please Choose a number between 1 to 4")