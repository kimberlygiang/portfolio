start = '''
You're camping with your family in the forrest and wake up by yourself in the morning to wash up. 
All of a sudden, you hear rumbling from the bushes. You turn around and find that there is a bear behind you --
it is trying to eat you. Run away from the bear. There is a path to your right and to your left. 
Type "I'm done" to end game whenever you're bored. 
'''

print(start)

print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("You decide to go left and you run into a swarm of bees.") 
    print("Type 'stand still' if you do not want to get stung by the bees or 'run' to pass them.")
    user_input2 = input()
    if user_input2 == "stand still":
    	print("You got eaten by the bear!")
    elif user_input2 == "run":
    	print("You got stung to death by the bees!")
    else:
    	print("That was not an option!")
elif user_input == "right":
    print("You choose to go right and run into a river.") 
    print("Type 'swim' to cross the river or 'stay' to not cross the river.")
    user_input3 = input()
    if user_input3 == "swim":
    	print("The bear couldn't cross the river and you're safe!")
    elif user_input3 == "stay":
    	print ("The bear caught up and ate you!")
    else:
    	print("That was not an option!")
else:
	print("That was not a choice!")

print("Game over!")



 
