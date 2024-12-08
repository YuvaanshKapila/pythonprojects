import random
import matplotlib.pyplot as plt

# Function to roll multiple dice and calculate stats
def roll_dice(sides=6, rolls=1):
    outcomes = [random.randint(1, sides) for _ in range(rolls)]
    return outcomes

# Function to simulate a large number of rolls and display stats
def simulate_dice(sides=6, num_simulations=10000):
    outcomes = {i: 0 for i in range(1, sides + 1)}
    
    for _ in range(num_simulations):
        roll = random.randint(1, sides)
        outcomes[roll] += 1
    
    return outcomes

# Function to display the histogram
def display_stats(outcomes, sides):
    plt.bar(outcomes.keys(), outcomes.values())
    plt.xlabel('Dice Number')
    plt.ylabel('Frequency')
    plt.title(f"Dice Roll Outcomes (1-{sides})")
    plt.show()

def main():
    print("Welcome to the Advanced Dice Simulation!")
    
    while True:
        print("\nChoose an option:")
        print("1. Roll Dice")
        print("2. Simulate Multiple Rolls")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            sides = int(input("Enter the number of sides on the dice: "))
            rolls = int(input("Enter the number of rolls: "))
            outcomes = roll_dice(sides, rolls)
            print(f"Outcomes: {outcomes}")
        elif choice == '2':
            sides = int(input("Enter the number of sides on the dice: "))
            num_simulations = int(input("Enter the number of simulations: "))
            outcomes = simulate_dice(sides, num_simulations)
            print("Simulation Results:")
            for outcome, count in outcomes.items():
                print(f"Number {outcome}: {count} times")
            display_stats(outcomes, sides)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
