import random
import json
import os

# Function to load and save leaderboard
def load_leaderboard():
    if os.path.exists("leaderboard.json"):
        with open("leaderboard.json", "r") as file:
            return json.load(file)
    else:
        return {}

def save_leaderboard(leaderboard):
    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file, indent=4)

# Function to set difficulty
def set_difficulty():
    print("Select Difficulty: 1. Easy 2. Medium 3. Hard")
    choice = input("Choose difficulty: ")
    if choice == '1':
        return 10, 50  # Easy: 10 max guesses, range 1-50
    elif choice == '2':
        return 7, 100  # Medium: 7 max guesses, range 1-100
    else:
        return 5, 200  # Hard: 5 max guesses, range 1-200

# Function to provide hints
def give_hint(number, guess):
    if guess < number:
        return "Try a higher number!"
    elif guess > number:
        return "Try a lower number!"
    else:
        return "Correct!"

# Main function for the game
def number_guessing_game():
    leaderboard = load_leaderboard()
    print("Welcome to the Advanced Number Guessing Game!")

    player_name = input("Enter your name: ")
    score = 0
    play_again = 'yes'
    
    while play_again.lower() == 'yes':
        max_attempts, range_limit = set_difficulty()
        number_to_guess = random.randint(1, range_limit)
        attempts = 0
        game_won = False
        
        print(f"Guess the number between 1 and {range_limit}! You have {max_attempts} attempts.")
        
        while attempts < max_attempts:
            guess = int(input(f"Attempt {attempts + 1}: "))
            attempts += 1
            
            print(give_hint(number_to_guess, guess))
            
            if guess == number_to_guess:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                game_won = True
                score += max(0, max_attempts - attempts + 1)
                break
        
        if not game_won:
            print(f"Sorry, you couldn't guess the number. It was {number_to_guess}.")
        
        print(f"Your score: {score}")
        
        # Update leaderboard
        leaderboard[player_name] = score
        save_leaderboard(leaderboard)
        
        print("\nLeaderboard:")
        for player, score in leaderboard.items():
            print(f"{player}: {score}")
        
        play_again = input("Do you want to play again? (yes/no): ")

number_guessing_game()
