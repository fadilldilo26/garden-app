"""
Garden Advice App
=================
Provides gardening tips and advice based on the month and the season.

Author: Faadhil Khan
Student ID: FA25090019005
Date: 2026-09-23
"""

# CHANGELOG / TODO LIST
# ---------------------
# [2026-09-23] TODO: Add proper module-level docstring. (DONE)
# [2026-09-23] TODO: Add author information. (DONE)
# [2026-09-23] TODO: Replace hardcoded month names with a data structure.
# [2026-09-23] TODO: Refactor get_season() to use dictionary mapping.
# [2026-09-23] TODO: Add input validation for month parameter. (DONE - See main function)

# TODO: Replace these hardcoded month names with a proper data structure
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

def get_season(month):
    """Returns the season for a given month number (1-12)."""
    # TODO: Refactor this into a cleaner implementation using a dictionary
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month"

def get_gardening_advice(month):
    """
    Returns gardening advice based on the month.
    TODO: Expand this function to include more detailed advice per season.
    """
    season = get_season(month)
    # TODO: Replace hardcoded advice strings with a structured data source
    if season == "Spring":
        advice = "Time to plant seeds! Prepare your soil and start sowing."
    elif season == "Summer":
        advice = "Keep plants well-watered. Mulch to retain moisture."
    elif season == "Autumn":
        advice = "Harvest your crops and prepare beds for winter."
    elif season == "Winter":
        advice = "Plan next year's garden. Protect sensitive plants from frost."
    else:
        advice = "No specific advice available."
    return advice

# --- NEW FEATURE: Input Validation & User Prompts (Fixes Issue #2) ---
def main():
    """Main function to run the Garden Advice App with error handling."""
    try:
        # Get user input instead of hardcoded value
        user_input = input("Enter a month number (1-12): ")
        month_number = int(user_input)
        
        # Validate range
        if month_number < 1 or month_number > 12:
            print("Error: Please enter a number between 1 and 12.")
            return
            
        month_name = months[month_number - 1]
        season = get_season(month_number)
        advice = get_gardening_advice(month_number)
        
        print(f"\nMonth: {month_name}")
        print(f"Season: {season}")
        print(f"Advice: {advice}")
        
    except ValueError:
        # Handle non-integer input (e.g., typing "abc")
        print("Error: Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()