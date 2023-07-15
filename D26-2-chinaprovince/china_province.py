import turtle
import pandas

screen = turtle.Screen()
screen.title("China.Province Game")
image = "blank_province_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("34_provinces.csv")
all_provinces = data.province.to_list()

guessed_provinces = []

while len(guessed_provinces) < 34:
    answer_province = screen.textinput(title=f"{len(guessed_provinces)}/34 Provinces Correct", prompt="What's another province's name?").title()

    if answer_province == "Exit":
        missing_province = []
        for province in all_provinces:
            if province not in guessed_provinces:
                missing_province.append(province)
            new_data = pandas.DataFrame(missing_province)
            new_data.to_csv("province_to_learn.csv")

        break
    if answer_province in all_provinces:
        guessed_provinces.append(answer_province)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # pull out the row of answer_province
        province_data = data[data.province == answer_province]
        t.goto(int(province_data.x), int(province_data.y))
        t.write(answer_province)


