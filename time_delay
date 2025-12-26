### Time Delay
"""Takes passenger and fleet lists as parameters. Loops through fleet data to check if plane is 
    late before looping through the passengers. Counts how many passengers on the late plane have a 
    layover. Returns 2D list of late planes with passengers that have layover."""
    
def time_delay(passengers, fleet):
    
    delay = []
    for plane in fleet:
        num = 0
        # Checks if plane is late and loops through all
        # passengers with same flgiht
        if plane[6] == "Late":
            for passenger in passengers:
                # Adds 1 to count if passenger has layover
                if len(passenger) == 8 :
                    if plane[4] == passenger[2] and passenger[7] == "Layover":
                        num +=1
            delay.append([plane[0], num])
                
    return delay