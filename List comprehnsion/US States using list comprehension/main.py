import turtle
import pandas

screen = turtle.Screen()
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
screen.title("U.S. States")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
states_done = []
score = 0
game_is_on = True
states_data = pandas.read_csv("50_states.csv")
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Guessed.", prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        states_not_done = [states for states in states_data.state if states not in states_done]
        new_data = pandas.DataFrame(states_not_done)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False

    answer_correct = ""
    correct_answer_coordinate = ''
    for state in states_data.state:
        if answer_state.title() == state and answer_state.title() not in states_done:
            correct_answer_coordinate = states_data[states_data.state == answer_state.title()]
            answer_correct = True
            states_done.append(answer_state.title())
            score += 1
        elif answer_correct is not True:
            answer_correct = False

    if answer_correct:
        writer.goto(x=int(correct_answer_coordinate.x), y=int(correct_answer_coordinate.y))
        writer.write(arg=answer_state.title(), align="center", font=("Courier", 10, "normal"))
    if score == 50:
        game_is_on = False
