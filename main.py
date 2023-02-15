import turtle
from turtle import Turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# all_states_text = []
# all_states_locations = []
answers = []
game_on = True

with open("50_states.csv") as file:
    file_data = csv.reader(file)
    # print(file_data)
    # all_states = []
    # answer = screen.textinput(title=f"{len(correct_answers)}/50 States Correct",
    #                           prompt="What's another state name?").lower()
    all_states = [data[0].lower() for data in file_data if data[0] != "state"]
    while game_on:

        answer = screen.textinput(title=f"{len(correct_answers)}/50 States Correct",
                                  prompt="What's another state name?").lower()
        # print(answer)
        # print(type(answer))
        # for data in file_data:
            # print(data)
            # if data[0] != "state":
            #     all_states.append(data[0].lower())
            # print(data)
            # if data[0] == "ohio":
            #     print(data[data[0] == "ohio"])
        # print(all_states)
        # print(data)
        #         if data[0] == answer:
        #             print(data[data[0] == answer])

        if answer in all_states:
            answers.append(answer)
            # print(answer)
            if answer in answers:
                pass
            # else:
            #     t = Turtle(f"{answer}")
            #     t.pu()
            #     t.ht()
            #     t.goto()

        correct_answers = set(answers)
        # print(correct_answers)

        # answer = screen.textinput(title=f"{len(correct_answers)}/50 States Correct",
        #                           prompt="What's another state name?").lower()

            # screen.addshape(answer)
            # turtle.shape(answer)
            # turtle.goto()




# get mouse-clicked x,y location
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)


turtle.mainloop()



