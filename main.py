# Magdalena Galwa
# 15/09/2025
# Description:
# Homework:
    # Create a tool, which will do user generated news feed:
    # User select what data type he wants to add
    # Provide record type required data
    # Record is published on text file in special format

# You need to implement:
    # News – text and city as input. Date is calculated during publishing.
    # Private ad – text and expiration date as input. Day left is calculated during publishing.
    # Book review - text and mark as an input. Date is calculated during publishing.

# Each new record should be added to the end of file. Commit file in git for review.

import os
from datetime import datetime

# Class GUI - manages the user interface
class GUI:
    # Initialize the GUI and display the menu to the user
    def __init__(self):
        print("=== News Feed Tool ===")
        print("Choose one of the options:")
        print("1 - News Feed")
        print("2 - Private Ad")
        print("3 - Book Review")

    # Get the user's choice (1, 2, or 3)
    def get_user_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice (1, 2, 3): "))
                if choice in [1, 2, 3]:  # Valid choices
                    return choice
                else:
                    print("Invalid choice. Please select 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter the number 1, 2, or 3.")

    # Get user-provided parameters for News
    def get_news_feed_params(self):
        text = input("Enter the news text: ")
        city = input("Enter the city: ")
        return {"text": text, "city": city}

    # Get user-provided parameters for Private Ad
    def get_ad_params(self):
        text = input("Enter the ad text: ")
        while True:
            try:
                expire_date = input("Enter the expiration date (format YYYY-MM-DD): ")
                expire_date = datetime.strptime(expire_date, "%Y-%m-%d").date()
                # Ensure expiration date is in the future
                if expire_date > datetime.now().date():
                    return {"text": text, "expire_date": expire_date}
                else:
                    print("The expiration date must be later than today's date. Please try again.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    # Get user-provided parameters for Book Review
    def get_book_review_params(self):
        text = input("Enter the book review text: ")
        while True:
            try:
                rate = int(input("Rate the book (1-5): "))
                # Ensure the rate is between 1 and 5
                if 1 <= rate <= 5:
                    return {"text": text, "rate": rate}
                else:
                    print("Invalid rating. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 5.")

# Class User - manages user input and choice handling
class User:
    def __init__(self):
        # Display the GUI to the user
        self.gui = GUI()
        # Get the user's choice from the menu
        self.choice = self.gui.get_user_choice()
        # Get the required data from the user based on their choice
        self.data = self.get_user_data()

    # Based on the user's choice, collect the appropriate type of data from the user
    def get_user_data(self):
        if self.choice == 1:
            return self.gui.get_news_feed_params()  # News Feed
        elif self.choice == 2:
            return self.gui.get_ad_params()  # Private Ad
        elif self.choice == 3:
            return self.gui.get_book_review_params()  # Book Review

# News class - represents the News record
class News:
    def __init__(self, text, city):
        self.text = text  # News content
        self.city = city  # City related to the news
        # Current timestamp when the news is published
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")

    # Convert the News object into a text format ready for saving
    def __str__(self):
        return f"News ------------------------\n{self.text}\n{self.city}, {self.timestamp}\n"

# Private Ad class - represents the Private Ad record
class AdPrivate:
    def __init__(self, text, expire_date):
        self.text = text  # Ad content
        self.expire_date = expire_date  # Expiration date of the ad

    # Convert the AdPrivate object into a text format ready for saving
    def __str__(self):
        # Calculate the number of days left until the ad expires
        days_left = (self.expire_date - datetime.now().date()).days
        return f"Private Ad ------------------------\n{self.text}\nActual until: {self.expire_date}, {days_left} days left\n"

# BookReview class - represents the Book Review record
class BookReview:
    def __init__(self, text, rate):
        self.text = text  # Book review content
        self.rate = rate  # Rating given to the book
        # Current publication date
        self.publication_date = datetime.now().strftime("%d/%m/%Y")

    # Convert the BookReview object into a text format ready for saving
    def __str__(self):
        return f"Book Review ------------------------\n{self.text}\nRate: {self.rate}/5\nPublished on: {self.publication_date}\n"

# Function to save the record to a file
def save_to_file(record):
    file_path = "output.txt"  # File name where records will be saved
    record_str = str(record)  # Convert the record into a string

    # If the file doesn't exist, create it and write a header
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("News Feed App\n\n")

    # Append the new record to the file
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(record_str + "\n")

    # Notify the user that the record has been saved
    print("Record has been successfully saved to 'output.txt'.")

# Main execution logic
user = User()  # Create a User object and gather input
if user.choice == 1:
    # Create a News object using user-provided data
    record = News(user.data["text"], user.data["city"])
elif user.choice == 2:
    # Create a Private Ad object using user-provided data
    record = AdPrivate(user.data["text"], user.data["expire_date"])
elif user.choice == 3:
    # Create a Book Review object using user-provided data
    record = BookReview(user.data["text"], user.data["rate"])
else:
    print("Invalid choice. Something went wrong.")

# Save the created record to the file
save_to_file(record)