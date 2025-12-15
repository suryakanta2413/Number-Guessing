import random

lowest_num = 1
heighest_num = 100

answer = random.randint(lowest_num, heighest_num)
guesses = 0
is_running = True

print("----- Number Guessing Game ------")
print(f"select a number between {lowest_num} to {heighest_num}")

while is_running:
    guess = input("Enter your guess 🤔 : ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num and guess > heighest_num:
            print("That number is out of range 😤")
            print(f"please select a number between {lowest_num} to {heighest_num} 🤔")
        elif guess < answer :
            print("Too low! Try again 😖")
        elif guess > answer :
            print("Too high! Try again 😖")
        else:
            print(f"Correct 😉! The answer was {answer} ")
            print(f"Number of guess : {guesses}")
            is_running = False
    else:
        print("Invalid 🥱")
        print(f"select a number between {lowest_num} to {heighest_num} 🤔")
print("-----Game Over-----")


