### Layover
"""Function which returns the layover planes and their corresponding information in a list and
    a 2D list of passengers which have a layover and their corresponding information"""

def layover():
    
    #sets fleet and passenger data to their respective variables
    fleet = fleet_data()
    passengers = passenger_data()
    
    #makes two empty lists, the first is for the planes with layovers and the second is for passengers
    plane_layover = []                                                                 # with layovers
    layover_passengers = []  

    #runs through index of the fleet list
    for plane in fleet:
        #count for number of layover passengers on each plane
        layover_count = 0  
        #sets the gate of the plane to a variable gate
        gate = plane[4]  
        
        #runs through every person in the passenger list
        for person in passengers:
            #checks that the gate is the same as the current plane and that they do have a layover
            if len(person) >= 8 and person[2] == gate and person[7] == "Layover":
                layover_count += 1
             
                #adds the list consisting of their first name, initial of last nam, and their gate to the list
                layover_passengers.append([person[0], person[1], person[2]])     #of passengers with layovers   
      
        #adds the list of the planes name/ID and the num of passengers with layovers to the list of all
        plane_layover.append([plane[0], layover_count])                               #planes layovers

    #returns both lists 
    return plane_layover, layover_passengers