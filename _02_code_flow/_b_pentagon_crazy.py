import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


def get_next_color(i):
    return colors[i % len(colors)]


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('black')
    window.setup(width=0.75, height=0.5, startx=0, starty=0)
    
    colors = ('red', 'blue', 'green', 'yellow', 'orange')
    
    # Make a new turtle
    turtleme = turtle
    # Make the turtle shape 'turtle', .shape('turtle')
    turtleme.shape('turtle')
    # Set the turtle speed to max (0)
    turtleme.speed(0)
    # Set the turtle width to 1
    turtleme.width(1)
    # Create a variable to hold the number of sides in a pentagon
    sides = 4
    # Create a variable to be the angle of 360 divided by the sides variable
    angle = 360 / sides
    # Use a for loop to repeat ALL the following lines of code 360 times. 
    for i in range(36000):
        # If the loop variable (i) is equal to 100, set the turtle width to 2
        if i == 100:
            turtleme.width(2)
        # If the loop variable (i) is equal to 200, set the turtle width to 3
        if i == 200:
            turtleme.width(3)
        if i == 300:
            turtleme.width(4)
        if i == 400:
            turtleme.width(5)
        if i == 500:
            turtleme.width(6)
        if i == 600:
            turtleme.width(7)
        # Use the get_next_color function to set the turtle pencolor,
        # *hint .pencolor(get_next_color(i))
        turtleme.pencolor(get_next_color(i))
        # Move the turtle forward by the loop variable, *hint .forward(i)
        turtleme.forward(i)
        # Turn the turtle to the right by the angle variable + 1
        turtleme.right(angle + 1)
    # Hide your turtle so you can see the pattern.
        turtleme.hideturtle()
    # Check the pattern against the picture in the recipe. If it matches, you are done!
    
    # Variations:
    # *Make the pattern really huge
    # *Change the colors
    # *Experiment with different shapes
    
    # Call the turtle.done() method
    turtle.done()
