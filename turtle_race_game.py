import turtle
import random

# Set Start Positions
START_X = 200
START_Y = 100


# Set End Positions
END_X = 300
END_Y = 100

# Set Radius
RADIUS = 40

# Ready Player One
player_one = turtle.Turtle()
player_one.shape("turtle")
player_one.color("green")
player_one.penup()
player_one.goto(-START_X, START_Y)

# Ready Player Two
player_two = turtle.Turtle()
player_two.shape("classic")
player_two.color("blue")
player_two.penup()
player_two.goto(-START_X, -START_Y)

# Create Circle of Player One
player_one.goto(END_X, END_Y-RADIUS)
player_one.pendown()
player_one.circle(RADIUS)
player_one.penup()
player_one.goto(-START_X, START_Y)

# Create Circle of Player Two
player_two.goto(END_X, -(END_Y+RADIUS))
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-START_X, -START_Y)


# Create a dice
die = [i for i in range(1, 7)]


# Lets Begin the Fun Game
while True:
	if player_one.pos() >= (END_X, END_Y):
		print("Player One Wins!")
		break

	elif player_two.pos() >= (END_X, -END_Y):
		print("Player Two Wins!")
		break

	else:
		for j in range(2):
			input(f"Player {j+1}: Press 'Enter' to roll the die")
			result = random.choice(die)
			steps = (20*result)

			player_one.fd(steps) if j==0 else player_two.fd(steps)


turtle.mainloop()


