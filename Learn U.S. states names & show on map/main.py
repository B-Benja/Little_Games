import turtle
import pandas as pd

FONT = ("Courier", 50, "normal")

# get nfo about states coordinates
# nfo saved to 50_states.csv
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# US map background
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# load data from states csv & store as lists
states = pd.read_csv("50_states.csv")
states_list = states["state"].to_list()
# not needed if Alternative used (see below)
# x_coor = states["x"].to_list()
# y_coor = states["y"].to_list()

text = turtle.Turtle()

score = 0
gaming = True
already_guessed = []

while gaming:
    answer_state = screen.textinput("Guess the state", f"You guessed {score} out of {len(states_list)}"
                                                       f" states.\nName a state on the map.").title()
    # to end loop
    if answer_state == "Exit":
        break
    # check if answer is within the states_list
    if answer_state in states_list:
        # check that state wasn't guessed before
        if answer_state not in already_guessed:
            # write the state name at the extracted position on the map
            text.penup()
            text.hideturtle()
            # text.goto(x_coor[states_list.index(answer_state)], y_coor[states_list.index(answer_state)])
            # alternative:
            correct_state = states[states["state"] == answer_state]
            text.goto(int(correct_state.x), int(correct_state.y))
            text.write(f"{answer_state}")
            score += 1
            already_guessed.append(answer_state)
            if score == len(states_list):
                text.penup()
                text.hideturtle()
                text.goto(0, 0)
                text.write(f"Wow, you guessed\nall states!", align="center", font=FONT)
                gaming = False
    else:
        gaming = False
        text.penup()
        text.hideturtle()
        text.goto(0, 0)
        text.write(f"Game Over!\n{score}/{len(states_list)}", align="center", font=FONT)

# extract the missing states and store them in a csv
missing_states = [states for states in states_list if states not in already_guessed]
# alternative, long version without list comprehension
# missing_states = []
# for entry in states_list:
#     if entry not in already_guessed:
#         missing_states.append(entry)

missing_states_csv = pd.DataFrame({
    "Missed states": missing_states,
})
missing_states_csv.to_csv("missing_states.csv")

screen.exitonclick()