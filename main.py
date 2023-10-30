import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

previous_guesses = []

while len(previous_guesses) < 50:
    guess = screen.textinput(title=f"{len(previous_guesses)}/50 States Correct", prompt="Name a US State").title()

    if guess == "Exit":
        missing_states = [state for state in all_states if state not in previous_guesses]
        # missing_states = []           The above line replaced all 4 of these code lines
        # for state in all_states:
        #     if state not in previous_guesses:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    for answer_states in all_states:
        if guess == answer_states:
            previous_guesses.append(answer_states)
            t = turtle.Turtle()
            t.ht()
            t.penup()
            state_data = data[data.state == answer_states]  # This pulls the coordinates for the required state
            t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
            # the '.iloc[0]' is there to fix an error message, and doesn't do much else
            t.write(answer_states)

screen.exitonclick()
