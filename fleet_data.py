## Fleet Data
"""Opens fleet data text and creates lists for each plane containing their individual 
    information then stores it all into one large list. Returns major list."""
    
def fleet_data():
    
    filename = open("fleet_data.txt")
    full_list = []
    
    # Loops through each plane's information and creates a list
    for line in filename:
        fleet_list = line.split(",")
        for n in range(0, len(fleet_list)):
            # Converts appropriate objects into integers
            if n == 1 or n == 2 or n == 3 or n == 7:
                fleet_list[n] = int(fleet_list[n])
        
        # Adds to major list and returns major list
        full_list.append(fleet_list)
    
    filename.close()
    return full_list