from turtle import Turtle, Screen
from fuzzywuzzy import process, fuzz
import pandas as pd

screen = Screen()
screen.title("Shahin's Iran Provinces Game")
turtle = Turtle()
image = "Docs/Iran.gif"
screen.addshape(image)
screen.setup(width=770, height=758, starty=15)
turtle.shape(image)

data = pd.read_csv("Docs/31_provinces.csv")
provinces_list = data.province.to_list()
print(provinces_list)
game_is_on = True
score = 0
true_answers = []
def find_best_province_match(user_input, correct_provinces, threshold=80):
    """
    Finds the best matching province name from the correct_provinces list
    based on fuzzy string matching.

    Args:
        user_input (str): The name entered by the player.
        correct_provinces (list): A list of all correct province names.
        threshold (int): The minimum similarity score (0-100) to consider a match.

    Returns:
        str or None: The correctly spelled province name if a match is found,
                     otherwise None.
    """
    # Convert correct provinces to lowercase for comparison, but keep original for return
    lower_case_provinces = [p.lower() for p in correct_provinces]

    # Use process.extractOne with token_set_ratio for robustness
    # token_set_ratio is good for variations in word order or missing/extra small words
    best_match = process.extractOne(user_input.lower(), lower_case_provinces, scorer=fuzz.token_set_ratio)

    if best_match:
        matched_name_lower, f_score = best_match
        if f_score >= threshold:
            # Find the original casing from your correct_provinces list
            for p_original in correct_provinces:
                if p_original.lower() == matched_name_lower:
                    print(f"DEBUG: Input '{user_input}' matched '{p_original}' with score {f_score}")
                    return p_original # Return the original casing
    return None
while game_is_on:
    user_answer = screen.textinput(f"{score}/31 provinces correct", "What's another province name?").title()
    user_answer = find_best_province_match(user_answer, provinces_list, threshold=80)

    if user_answer not in true_answers:
        if user_answer in provinces_list:
            true_answers.append(user_answer)
            print(true_answers)
            score += 1
            province_info = data[data.province == user_answer]
            province_cor = (int(province_info.x.iloc[0])-20, int(province_info.y.iloc[0]))
            province_name = Turtle()
            province_name.penup()
            province_name.hideturtle()
            province_name.goto(province_cor)
            province_name.write(user_answer)
    if score == 31:
        game_is_on = False


screen.mainloop()













screen.exitonclick()