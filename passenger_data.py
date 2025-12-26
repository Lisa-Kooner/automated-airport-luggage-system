## Passenger Data
"""Opens passenger data text and creates lists for each passenger containing their individual 
    information then stores it all into one large list. Returns major list."""
    
def passenger_data():
    
    file = open("passenger_data_v2.txt", 'r')
    all_passenger_info = []
    
    # Loops through each passenger's information and creates a list for them
    for line in file:
        z = line.strip()
        x = z.split(",")
        # Declare major list and count of passengers 
        current_passenger = []
        
        count = 0
        for item in x:
            y = item.strip()
            
            if y and count!=6: 
                current_passenger.append(y)
                count += 1
                
            elif count == 6:
                current_passenger.append(float(y))
                count += 1

        all_passenger_info.append(current_passenger)
    
    file.close()
    return all_passenger_info