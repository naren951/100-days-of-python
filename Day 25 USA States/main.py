from turtle import Screen, Turtle
import pandas as pd

states = pd.read_csv("50_states.csv")
correct_guesses = []
not_guessed = []
total = len(states)



screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
turtle.penup()
turtle.hideturtle()


while len(correct_guesses)!=total:
    answer = screen.textinput(title=f"{len(correct_guesses)}/{total} States Correct",prompt="What's another state's name??")
    answer = answer.title()
    if answer == 'Exit':
        for state in states['state'].to_list():
            if state not in correct_guesses:
                not_guessed.append(state)
        not_guessed = pd.DataFrame(not_guessed)
        not_guessed.to_csv("not_guessed.csv")
        break
    if answer in states['state'].to_list() and answer not in correct_guesses:
        correct_guesses.append(answer)
        x = int(states[states['state']==answer]['x'])
        y = int((states[states['state']==answer]['y']))
        turtle.goto((x,y))
        turtle.write(answer)
    

screen.exitonclick()