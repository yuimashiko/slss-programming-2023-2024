# Winter_Holidays review
# January 8th
# YUI MASHIKO

import random

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24

    Params:
        good_or_bad - indicate what kind of event to summarize

    Returns:
        an event that happened during the holidays
        the event is selected randomly"""

    good_events = [
        "I got a gift card.",
        "I went to Richmond Centre.",
        # Add more good events as needed
    ]

    bad_events = [
        "I spent time alone at xmas.",
        "I spent time alone at new year.",
        # Add more bad events as needed
    ]

    if good_or_bad.lower() == "good":
        return random.choice(good_events)
    elif good_or_bad.lower() == "bad":
        return random.choice(bad_events)
    else:
        return "Invalid input. Please provide 'good' or 'bad'."

def main() -> None:
    print(winter_holiday("good"))
    print(winter_holiday("bad"))

if __name__ == "__main__":
    main()