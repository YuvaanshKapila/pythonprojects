import requests
import json
import os

# Function to fetch random quotes from an external API
def get_random_quote(category="inspire"):
    url = f"https://api.quotable.io/random?tags={category}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f"{data['content']} — {data['author']}"
    else:
        return "Error fetching quote."

# Function to store favorite quotes in a text file
def save_favorite_quote(quote):
    with open("favorite_quotes.txt", "a") as file:
        file.write(quote + "\n")

# Function to display saved favorite quotes
def view_favorites():
    if os.path.exists("favorite_quotes.txt"):
        with open("favorite_quotes.txt", "r") as file:
            quotes = file.readlines()
            if quotes:
                print("\nYour Favorite Quotes:")
                for idx, quote in enumerate(quotes, 1):
                    print(f"{idx}. {quote.strip()}")
            else:
                print("You haven't saved any quotes yet.")
    else:
        print("No favorite quotes saved yet.")

def main():
    print("Welcome to the Advanced Quote Generator!")
    while True:
        print("\nSelect an option:")
        print("1. Get Random Quote")
        print("2. Save Favorite Quote")
        print("3. View Favorite Quotes")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            category = input("Enter a category (inspire, love, life, etc.): ")
            print(f"\nQuote: {get_random_quote(category)}\n")
        elif choice == '2':
            quote = input("Enter a quote to save: ")
            save_favorite_quote(quote)
            print("Quote saved successfully!")
        elif choice == '3':
            view_favorites()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
