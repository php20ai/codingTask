""" Below, created the variables price_per_night_hotel_GBP, daily_car_rent_cost
    city_flight, num_nights and rental_days.
"""
price_per_night_hotel_GBP = 100
daily_car_rent_cost=20
city_flight=input("Enter City of Destination: ").lower()

num_nights=float(input("Enter number of nights you will stay at hotel: "))
rental_days=float(input("Enter number of days you will hire a car: "))

# Below, created hotel_cost function which contains price_per_night_hotel_GBP and num_nights variables:
def hotel_cost(num_nights):
    return (price_per_night_hotel_GBP)*(num_nights)

# Below, created plane_cost function which contains if/elif/else statements:
def plane_cost(city_flight):
    if city_flight=="portugal":
        return 200
    elif city_flight=="turkey":
        return 300
    elif city_flight=="south africa":
        return 900
    elif city_flight=="america":
        return 700
    else:
        return 500

# Below, created car_rental function which contains daily_car_rent_cost and rental_days variables.
def car_rental(rental_days):
    return (daily_car_rent_cost)*(rental_days)

""" Below, created holiday_cost function which has no arguments, but it uses the car_rental, 
    plane_cost and hotel_cost functions. Also holiday_cost has an output which is total_holiday_cost
      (this is sum of all outputs from all functions created above)."""
def holiday_cost():
    car=car_rental(num_nights)
    
    plane=plane_cost(city_flight)
   
    hotel=hotel_cost(rental_days)
   
    total_holiday_cost=car+plane+hotel
    print(f"Your total holiday cost is £{total_holiday_cost}.")

# Below, telling python to run the holiday_cost function.
holiday_cost()

