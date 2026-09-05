import turtle
import pandas as pd

# Setting turtle screen image
screen = turtle.Screen()
screen.setup(width=400, height=467)
screen.title("India States Game!")
img = "india-state.gif"
screen.addshape(img)
turtle.shape(img)

# reading data from csv
data = pd.read_csv("india_states.csv")

# turning data.state series into a list
state_list = data.state.to_list()

#an empty list fro correct gusses
correct_guess__list = []

# The loop to allow the user to keep gussing
while len(correct_guess__list) <= 30:
    # User Input box                    # Keep track of the score
    user_input = screen.textinput(title=f"{len(correct_guess__list)}/30 States.", prompt="What's another state's name?").title()# Convert to Title Case

    if user_input == "Exit":
        missing_states = []
        for state in state_list:
            if state not in correct_guess__list:
                missing_states.append(state)
        # TODO- the states which the user haven't gussed when they exit.
        df = pd.DataFrame(missing_states, columns=["State"])
        df.to_csv("states_to_learn.csv")
        break

    # Check if the guess is among 30 states
    if user_input in state_list:
        state_row = data[data.state == user_input]
        x_cood = state_row.x.item()
        y_cood = state_row.y.item()
        # Write correct gusses onto the map
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(x_cood, y_cood)  
        pen.write(user_input)
        # Record the correct guesses in a list
        correct_guess__list.append(user_input)


