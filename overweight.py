## Overweight
"""This code defines a function overweight() that calculates the number of overweight passengers 
    on each flight and their respective excess baggage weight from the previous data lists. It compares 
    each passenger's baggage weight to the flight's allowed baggage limit, and returns two lists: 
    one containing the flights with the count of overweight passengers, 
    and another with details of passengers exceeding the 
    weight limit, including their names and the amount they exceeded. """
    
def overweight(passenger_list,fleet_list):
    
    overweight_flight = []
    overweight_passenger = []
    #create two new list to contain overweight data
    for each_flight in fleet_list:
        overweight_amount = 0
        #to count how many passenger have over weight bag, and how much did they exceed
        for each_passenger in passenger_list:
            if each_flight[4] == each_passenger[2] and each_flight[5] == each_passenger[3]:
                #matching the passenegr with flight
                if each_passenger[6] > each_flight[7]:
                    #if they exceed the weight
                    overweight_amount+=1
                    #count the amount of over_weight
                    firstName=each_passenger[0].split()[0]
                    #copy their name from the list
                    weight_exceed=round(each_passenger[6]-each_flight[7],1)
                    #to calculate how much did they exceed
                    overweight_passenger.append([firstName, each_passenger[1], each_passenger[2], weight_exceed])
                    #add to overweight_passenger
        overweight_flight.append([each_flight[0], overweight_amount])
        #adding to overweight_flight
    return overweight_flight , overweight_passenger