import random

human_is_batsman = True
human_runs = 0
computer_runs = 0

print("Welcome to Hand Cricket!")
print("You are batting first. Enter your runs (0-6):")
while human_is_batsman:
    human_choice = int(input("Your number (1-6): "))
    computer_guess = random.randint(1, 6)
    print(f"Computer (bowler) guessed: {computer_guess}")
    if human_choice == computer_guess:
        print("You are out! Now you will bowl.")
        human_is_batsman = False
        break
    else:
        human_runs += human_choice
        print(f"You scored {human_choice} runs. Total: {human_runs}")

while not human_is_batsman:
    computer_choice = random.randint(1, 6)
    human_guess = int(input("Your guess (1-6): "))
    print(f"Computer chose: {computer_choice}")

    if computer_choice == human_guess:
        print("Computer is out! You win!")
        break
    else:
        computer_runs += computer_choice
        print(f"Computer scored {computer_choice} runs. Total: {computer_runs}")

    if computer_runs > human_runs:
        print("Computer wins!")
        break
