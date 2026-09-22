"""
Garden Advice App
=================
Provides gardening tips and advice based on the month and the season.

Author: Faadhil Khan
Student ID: FA25090019005
"""

# CHANGELOG / TODO LIST
# ---------------------
# [2026-09-23] TODO: Add proper module-level docstring. (DONE)
# [2026-09-23] TODO: Add author information. (DONE)
# [2026-09-23] TODO: Replace hardcoded month names with a data structure.
# [2026-09-23] TODO: Refactor get_season() to use dictionary mapping.
# [2026-09-23] TODO: Add input validation for month parameter.

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
    TODO: Add input validation for the month parameter.
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

# TODO: Add a main function to organize the program flow
month_number = 5 # TODO: Replace hardcoded value with user input
season = get_season(month_number)
advice = get_gardening_advice(month_number)
print(f"Month: {months[month_number - 1]}")
print(f"Season: {season}")
print(f"Advice: {advice}")