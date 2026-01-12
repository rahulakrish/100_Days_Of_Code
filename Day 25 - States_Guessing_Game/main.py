
#importing the csv file
import pandas as pd
df = pd.read_csv('50_states.csv')

#creating a new cloumn with lower case characters to account for user input being all lowercase
df['lower_case'] = df['state'].str.lower()

#importing the image using the turtle library
from turtle import Turtle, Screen

#creating a screen object
screen = Screen()

#setting the title of the screen: this will show up in the window
screen.title("U.S. States Guessing Game")

#creating a variable for the image
image = "blank_states_img.gif"

#first, you have to add the shape to the turtle's shapelist to call upon later
#you do that using the register_shape method. you can also use screen.addshape()
screen.register_shape(image)

#create the turtle object and set the shape as the image
t = Turtle()
t.shape(image)


#this is how you get the x,y co-ordinates of the mouse click point.
#you do not need this, but this is how the CSV file with the x,y coords for of all the states was gathered. 

# def get_mouse_click_coor(x, y):
#     print(x, y)

# screen.onscreenclick(get_mouse_click_coor)



#keep track of correct guesses 
correct_guess_count = 0

#flag for the while loop
game_on = True

#create a new turtle object to write the values 
new_turtle = Turtle()
new_turtle.hideturtle()
new_turtle.penup()

#getting the answer from the user
answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")

#creating a list to check for duplicate guesses
guessed_states = []

#creating a list for states not guessed
states_not_guessed = []

while game_on:
    #if the user hits cancel, None is returned. use break to exit the while loop
    if answer_state == None:
        break
 
    #if not, convert the answer to lower case and check the df
    else:
        answer_state = answer_state.lower()
        
    #check the df for the answer and also the guessed_state list if it's already been guessed. if it satisfies both,
    #then do the following:
    if answer_state in df['lower_case'].values and answer_state not in guessed_states:
        #add the guess to the list to check in the future
        guessed_states.append(answer_state)
        #amend the guess count
        correct_guess_count += 1  
        
        #get the x and y position from the df of the state
        #df.loc[rows,column]
        x_position = int(df.loc[df['lower_case'] == answer_state,'x'])
        y_position = int(df.loc[df['lower_case'] == answer_state,'y'])

        #send the new turtle to the x and y co-ord
        new_turtle.goto(x_position,y_position)
        #write the state's name
        new_turtle.write(answer_state.capitalize(),align='center',font=("Arial", 8, "normal"))
        
        #ask for the next state
        #the title is modified to show the number of correct guesses
        answer_state = screen.textinput(title=f"{correct_guess_count}/50 States guessed", prompt="What's another state's name?")
        answer_state = answer_state.lower()

        #if the guess is incorrect, just prompt again
    else:
        answer_state = screen.textinput(title=f"{correct_guess_count}/50 States guessed", prompt="What's another state's name?")
        answer_state = answer_state.lower()
        
        #if all states are guessed
    if correct_guess_count == 50:
        new_turtle.goto(0,0)
        new_turtle.write('ALL STATES GUESSED CORRECTLY! GAME OVER!',align='center',font=("Arial", 8, "normal"))
        game_on = False
        
    #secret word to exit the game: 'exit'
    #if user types exit, the game should shut down and also, the list of states that were not guessed should show.
    #this will serve as an educational tool for the user
    
    if answer_state == 'exit':
        break
for value in df['lower_case'].values:
    if value not in guessed_states:
        state = df.loc[df['lower_case'] == value,'state'].iloc[0]
        states_not_guessed.append(state)

states_not_guessed_df = pd.DataFrame(states_not_guessed,columns=['Missing States'])
print(states_not_guessed_df)

screen.mainloop()
