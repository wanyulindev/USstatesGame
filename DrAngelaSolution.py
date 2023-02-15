import turtle
import pandas

screen = turtle.Screen()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_answers = []

while len(correct_answers) < 50:
    answer = screen.textinput(title=f"{len(correct_answers)}/50 States Correct",
                              prompt="What's another state name?").title()
    if answer == "Exit":
        break
    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        if answer not in correct_answers:
            correct_answers.append(answer)
        # print(correct_answers)
        # print(set(all_states) - set(correct_answers))

print(f"What you have covered today so far: {correct_answers}, \n"
      f"yet there are more to be covered, like: {set(all_states) - set(correct_answers)}")



screen.exitonclick()



