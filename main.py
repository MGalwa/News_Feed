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

import os  # Importing os module for file operations
from datetime import datetime  # Importing datetime to handle date and time functionalities

# Class GUI - manages the user interface
class GUI:
    # Initialize the GUI and display the menu to the user
    def __init__(self):
        print("=== News Feed Tool ===")  # Display the main application title
        print("Choose one of the options:")  # Prompt to make a choice
        print("1 - News Feed")  # Option 1: Add a News record
        print("2 - Private Ad")  # Option 2: Add a Private Ad
        print("3 - Book Review")  # Option 3: Add a Book Review

    # Get the user's choice (1, 2, or 3)
    def get_user_choice(self):
        while True:  # Repeat until a valid choice is received
            try:
                choice = int(input("Enter your choice (1, 2, 3): "))  # Request user input
                if choice in [1, 2, 3]:  # Ensure the input is a valid option
                    return choice  # Return the valid choice
                else:
                    print("Invalid choice. Please select 1, 2, or 3.")  # Error message for out-of-range input
            except ValueError:
                print("Invalid input. Please enter the number 1, 2, or 3.")  # Error message for non-integer input

    # Get user-provided parameters for News
    def get_news_feed_params(self):
        text = input("Enter the news text: ")  # Ask for news content
        city = input("Enter the city: ")  # Ask for the related city
        return {"text": text, "city": city}  # Return collected data as a dictionary

    # Get user-provided parameters for Private Ad
    def get_ad_params(self):
        text = input("Enter the ad text: ")  # Ask for ad content
        while True:  # Repeat until a valid expiration date is provided
            try:
                expire_date = input("Enter the expiration date (format YYYY-MM-DD): ")  # Ask for the expiration date
                expire_date = datetime.strptime(expire_date, "%Y-%m-%d").date()  # Parse the date to ensure it's valid
                # Ensure expiration date is in the future
                if expire_date > datetime.now().date():  # Check if the date is after today
                    return {"text": text, "expire_date": expire_date}  # Return collected data as a dictionary
                else:
                    print("The expiration date must be later than today's date. Please try again.")  # Error for past dates
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")  # Error message for invalid format

    # Get user-provided parameters for Book Review
    def get_book_review_params(self):
        text = input("Enter the book review text: ")  # Ask for book review text
        while True:  # Repeat until a valid rating is provided
            try:
                rate = int(input("Rate the book (1-5): "))  # Ask for book rating
                # Ensure the rate is between 1 and 5
                if 1 <= rate <= 5:  # Validate that the rate is within the range
                    return {"text": text, "rate": rate}  # Return collected data as a dictionary
                else:
                    print("Invalid rating. Please enter a number between 1 and 5.")  # Error message for invalid range
            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 5.")  # Error for invalid input type

# Class User - manages user input and choice handling
class User:
    def __init__(self):
        # Display the GUI to the user
        self.gui = GUI()  # Create an instance of the GUI to handle user interactions
        # Get the user's choice from the menu
        self.choice = self.gui.get_user_choice()  # Store the user's menu choice
        # Get the required data from the user based on their choice
        self.data = self.get_user_data()  # Collect input data based on user's selection

    # Based on the user's choice, collect the appropriate type of data from the user
    def get_user_data(self):
        if self.choice == 1:  # If the user chose News Feed
            return self.gui.get_news_feed_params()  # Prompt for News details
        elif self.choice == 2:  # If the user chose Private Ad
            return self.gui.get_ad_params()  # Prompt for Ad details
        elif self.choice == 3:  # If the user chose a Book Review
            return self.gui.get_book_review_params()  # Prompt for Book Review details

# News class - represents the News record
class News:
    def __init__(self, text, city):
        self.text = text  # News content
        self.city = city  # City related to the news
        # Current timestamp when the news is published
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")  # Store formatted current date and time

    # Convert the News object into a text format ready for saving
    def __str__(self):
        return f"News ------------------------\n{self.text}\n{self.city}, {self.timestamp}\n"  # Format News for saving

# Private Ad class - represents the Private Ad record
class AdPrivate:
    def __init__(self, text, expire_date):
        self.text = text  # Ad content
        self.expire_date = expire_date  # Expiration date of the ad

    # Convert the AdPrivate object into a text format ready for saving
    def __str__(self):
        # Calculate the number of days left until the ad expires
        days_left = (self.expire_date - datetime.now().date()).days  # Calculate remaining days
        return f"Private Ad ------------------------\n{self.text}\nActual until: {self.expire_date}, {days_left} days left\n"  # Format Ad for saving

# BookReview class - represents the Book Review record
class BookReview:
    def __init__(self, text, rate):
        self.text = text  # Book review content
        self.rate = rate  # Rating given to the book
        # Current publication date
        self.publication_date = datetime.now().strftime("%d/%m/%Y")  # Store formatted current date

    # Convert the BookReview object into a text format ready for saving
    def __str__(self):
        return f"Book Review ------------------------\n{self.text}\nRate: {self.rate}/5\nPublished on: {self.publication_date}\n"  # Format review for saving

# Function to save the record to a file
def save_to_file(record):
    file_path = "output.txt"  # File name where records will be saved
    record_str = str(record)  # Convert the record into a string

    # If the file doesn't exist, create it and write a header
    if not os.path.exists(file_path):  # Check if file exists
        with open(file_path, "w", encoding="utf-8") as file:  # Open file in write mode if it doesn't exist
            file.write("News Feed App\n\n")  # Write application header to the file

    # Append the new record to the file
    with open(file_path, "a", encoding="utf-8") as file:  # Open file in append mode
        file.write(record_str + "\n")  # Write the new record

    # Notify the user that the record has been saved
    print("Record has been successfully saved to 'output.txt'.")  # Display success message

# Main execution logic
user = User()  # Create a User object and gather input
if user.choice == 1:
    # Create a News object using user-provided data
    record = News(user.data["text"], user.data["city"])  # Initialize News with user input
elif user.choice == 2:
    # Create a Private Ad object using user-provided data
    record = AdPrivate(user.data["text"], user.data["expire_date"])  # Initialize AdPrivate with user input
elif user.choice == 3:
    # Create a Book Review object using user-provided data
    record = BookReview(user.data["text"], user.data["rate"])  # Initialize BookReview with user input
else:
    print("Invalid choice. Something went wrong.")  # Unexpected case (should not occur due to validation)

# Save the created record to the file
save_to_file(record)  # Save the record to the output file