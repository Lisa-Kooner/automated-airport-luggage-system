# Automated Airport Luggage System

- **Type:** *Python*
- **Date:** *December 13th 2025*

---
This program is dedicated to analyzing information related to flights, passengers, and baggage within an airport.
It contains the functions passenger_data, fleet_data, daily_data, oversold, overweight, time_delay, layover, and
graphical_interface. **Passenger_data**, **fleet_data**, **daily_data** returns 2D lists containing the passenger complete 
information, the plane's information, and the gate and seat information respectively. **Overweight** returns the 
passengers information attached to how much they over the max limit for baggage weight. **Oversold** returns the
number of oversold economy seats as well as the number of oversold business seats, along with the name of the
plane model respectively. **Time delay** returns a 2D list containing late flights along with how many passenger 
on each of those flights that have a layover. **Layover** returns two lists, one 2D list with the plane model and 
how many passengers on each flight has a layover, and the second returns a list of the passengers with 
layovers' information. The **graphical_interface** outputs the a visual interface that contains the number of oversold
business seats, the number of oversold economy seats, the number of overweight bags, the number of layover passengers
and the number of late layover passengers for each plane. This **graphical_interface** also uses two helper functions to 
draw the boxes on the interface and to write the information with a specific font.