#Import the turtle module
import turtle

### Draw Rectangle
def draw_rectangle(x, y):
    """Function takes x and y paramter (both integers) and uses turtle graphics to draw a rectangle. This 
    is a helper function used for both graphical_teamID and layover functions. Does not return anything."""
    
    # Goes to desired location
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    # Sets color and draws rectangle
    turtle.fillcolor("lightgreen")
    turtle.begin_fill()
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(220)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(220)
    turtle.left(90)
    turtle.end_fill()


## Write Text
def write_text(x, y, text):
    """Function takes integer paramters, x and y, and string parameter, text. Goes to desired location in 
    window and writes text given. Function returns nothing but is used as a helper function for 
    graphical_teamID and layover functions."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.write(text, align="left", font=("Arial", 8, "normal"))


### Graphical Interface
def graphical_interface():
    """This function takes the output from all other functions as input, which are passenger_data(), fleet_data(),
    daily_data(), oversold(), overweight(), layover(), time_delay(), and uses the helper functions to help to
    buold the visual interface, by using Turtle. It stores the outputs in variables, then uses a for loop to
    iterate through each plane's information. Then it initializes count variables and uses if statements to ensure 
    that the loop variable does not exceed the length of the list concerned, in order to output the correct 
    information accordingly."""
    
    # Declare all values to be displayed
    fleet = fleet_data() # 2D list of fleet data
    layover_data, layover_passengers = layover()
    oversold_business_data, oversold_economy_data = oversold(passenger_data(), fleet_data(), daily_data(passenger_data()))
    overweight_bags_data, overweight_details_data = overweight(passenger_data(), fleet_data())
    timedelay_data = time_delay(passenger_data(), fleet_data())

    # Display and design screen output
    screen = turtle.Screen()
    screen.title("Plane Summary")
    screen.bgcolor("lightblue")
    screen.setup(width=1200, height=600)
    turtle.speed(100)
    turtle.hideturtle()
    screen_height = 600
    
    # Formatting box dimesions on the display
    box_height = 220
    line_spacing = 20
    num_lines = 7  
    total_box_height = box_height + (line_spacing * num_lines)


    # Start position of turtle
    start_y = screen_height / 2 - total_box_height / 2
    start_x = -600
    
    
    # Loop through each quare (7 planes)
    for i in range(len(fleet)):
        if i >= 7:
            break
        
        #Set the plan model variable
        plane_model = fleet[i][0]
        
        #Initialize values to default
        oversold_business_count = 0
        oversold_economy_count = 0
        overweight_count = 0
        layover_count = 0
        timedelay_count = 0
        
        # Updating the count variables for each catagory accordingly
        if i < len(oversold_business_data):
            oversold_business_count = oversold_business_data[i][1]
        if i < len(oversold_economy_data):
            oversold_economy_count = oversold_economy_data[i][1]
        if i < len(overweight_bags_data):
            overweight_count = overweight_bags_data[i][1]
        if i < len(layover_data):
            layover_count = layover_data[i][1]
        if i < len(timedelay_data):
            timedelay_count = timedelay_data[i][1]
        
        # New position of turtle for each rectangle
        x = start_x + i * 180
        y = start_y

        # Draw turtle and reset original coordinates
        draw_rectangle(x, y)
        current_y = y + box_height  

        # Display all info in the boxes
        write_text(x + 10, current_y, "Plane Name: " + str(plane_model))
        current_y -= line_spacing
        write_text(x + 10, current_y, "Oversold Business: " + str(oversold_business_count))
        current_y -= line_spacing
        write_text(x + 10, current_y, "Oversold Economy: " + str(oversold_economy_count))
        current_y -= line_spacing
        write_text(x + 10, current_y, "Overweight Bags: " + str(overweight_count))
        current_y -= line_spacing
        write_text(x + 10, current_y, "Layover Passengers: " + str(layover_count))
        current_y -= line_spacing
        write_text(x + 10, current_y, "Late Layover: " + str(timedelay_count))
    
    # Close turtle
    turtle.done()

graphical_interface() #output the final visual interface