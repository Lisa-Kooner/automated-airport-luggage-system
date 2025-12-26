## Daily Data
"""This function takes the passenger list as a parameter and outputs a list of lists, where each list
    contain its gate number, along with its respective number of economy seats and business seats that 
    are taken by the passengers"""
    
def daily_data(passenger_list):
    
    daily_data = [] #creating the main empty list
    
    #For loop to iterate through each passenger information, in the passenger list
    for passenger in passenger_list:
        
        gate = passenger[2]  #get the gate number on index 2 in the inner list
        seating_class = passenger[4]   #get the gate number on index 4 in the inner list
        existing_gate = False
        
        
        for data in daily_data:
            
            if data[0] == gate:  #verifying if the gate already exists
                
                if seating_class == 'E':
                    data[2] += 1   #update the number of economy seats, which is on index 2 of the inner list
                
                elif seating_class == 'B':
                    data[1] += 1   #update the number of business seats, which is on index 1 of the inner list
                
                existing_gate = True #reverse the value of the boolean, to prevent the code below from running
                break
            
            
        if not existing_gate:  #create a new list whenever there is a new gate
            
            if seating_class == 'E':
                daily_data.append([gate, 0, 1]) #initialize the inner list with the gate number and the seats
            
            elif seating_class == 'B':
                daily_data.append([gate, 1, 0])
                
    return daily_data