## Oversold
"""The function takes in passenger_data, daily_data, and fleet_data, which contains flight details like
    the plane model, gate number, and the seating capacity for both business and economy classes.
    It then calculates and returns a list that includes the flight model and the number of oversold economy
    seats for each flight in the fleet_data. To start, it sets up two empty lists to track the oversold 
    seat information for business and economy classes."""
        
def oversold(passenger_data, fleet_data, daily_data):
    
    # Lists to store oversold seat data
    oversold_business = []
    oversold_economy = []
    
    # Loop through fleet data
    for flight in fleet_data:
        model = flight[0]
        gate = flight[4]
        business_capacity = int(flight[1])
        economy_capacity = int(flight[2])

        # Match gate with daily bookings
        for daily in daily_data:
            if gate == daily[0]:
                business_booked = int(daily[1])
                economy_booked = int(daily[2])

                # Calculate oversold business seats
                oversold_business_seats = max(0, business_booked - business_capacity)
                oversold_business.append([model, oversold_business_seats])
                
                # Calculate oversold economy seats
                oversold_economy_seats = max(0, economy_booked - economy_capacity)
                oversold_economy.append([model, oversold_economy_seats])
                
                break  # Stop when gate is matched

    return oversold_business, oversold_economy