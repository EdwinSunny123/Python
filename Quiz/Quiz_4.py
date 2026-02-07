# Section A: Control Structures & Logic Building (Use Cases 1–5)

# 1. Flight class Validation
from ast import Lambda

flight_class = "Business"  

if flight_class == "Economy":
    print("Seat benefits: Standard seat with limited legroom.") 
elif flight_class == "Business":
    print("Seat benefits: Spacious seat with extra legroom and premium services.")
elif flight_class == "First":
    print("Seat benefits: Luxurious seat with full recline and exclusive amenities.")
else:
    print("Invalid flight class. Please choose Economy, Business, or First.")

# 2. Passenger Age Eligibility
age = 15

if age >= 15:
    print("Allowed")
else:
    print("Not Allowed")

# 3. International Flight Availablity 
country = "India" 

if country in ["USA", "UK", "Canada", "Australia"]:
    print("International flights are available.")
else:
    print("International flights are not available.")

# 4. Baggage Allowance Check

allowed_bags = 2
current_bags = 3

if current_bags > allowed_bags:
    print("Excess baggage! Please check the baggage allowance policy.")
else:
    print("Baggage within the allowed limit.")

# 5. Flight Delay Alert
delay_hours = 4

if delay_hours > 3:
    print("You are eligible for compensation due to the delay.")
else:
    print("No compensation available for delays under 3 hours.")

# Section B : Loops & iterations

# 6. Passenger Boarding List
passengers =["Amit", "Sara", "John", "Meera", "Raj"]

for passenger in passengers:
    print(f"Boarding passenger: {passenger}") 

# 7. Seat Number Assignment 
total_seats  = 10 

for seat_number in range(1, total_seats + 1):
    print(f"Seat Assigned: {seat_number}")

# 8. Flight Status Announcement

while count < 3:
    print("Reminder: Boarding will begin shortly. Please be ready.")
    count += 1

# 9. Skip Cancelled Flights
flight = ["AI101","Cancelled","AI203","AI405"]

for flight_code in flight:
    if flight_code == "Cancelled":
        continue
    print(f"Active flight: {flight_code}")

# 10. Stop Boarding 

passenger_count = 0
while True: 
    if passenger_count >= 5:
        print("Boarding stopped after 5 passengers.")
        break
    print(f"Boarding passenger number: {passenger_count + 1}")
    passenger_count += 1

# Section c : List , Tuples,  sets & Dictionaries

# 11. Flight bookking Management(List)
bookings = ["AI101", "AI202", "AI303"]

bookings.append("AI404")
bookings.remove("AI202")
print(f"Total bookings: {len(bookings)}")

# 12. Unique Destinations (Set)
destinations = ["Delhi", "Mumbai", "Delhi", "Dubai", "Mumbai"]

unique_destinations = set(destinations)
print(f"Unique destinations: {unique_destinations}")

# 13.Immutable Aircraft Details (Tuple)

aircraft = ("Boeing 737", 180, 2015)

print(f"Aircraft details: {aircraft}")

# 14. Passenger Profile (Dictionary)
profile = {"name": "Alex", "seat": "12A", "class": "Economy"}

profile["class"] = "Business"
for key, value in profile.items():
    print(f"{key}: {value}")

# 15. Flight Ratings Analysis

ratings = {"AI101": 4.2, "AI202": 4.8, "AI303": 4.1}
highest_rated_flight = max(ratings, key=ratings.get)
print(f"Highest rated flight: {highest_rated_flight} with rating {ratings[highest_rated_flight]}")


# Section D :  Strings & Built-in Functions 

#16. Airport Code Formatting

airport = "indira gandhi international airport"
print(airport.upper())
print(airport.title())

#17. Ticket PNR Validation

pnr = "A12X9"
if len(pnr) >= 6:
    print("Valid PNR")
else:
    print("Invalid PNR")

#18. Frequent Route Analysis

routes = ["Delhi-Mumbai", "Delhi-Mumbai", "Delhi-Dubai"]
route_counts = {}
for route in routes:
    route_counts[route] = route_counts.get(route, 0) + 1

most_frequent_route = max(route_counts, key=route_counts.get)
print(f"Most frequently searched route: {most_frequent_route}")


# Section E: Functions & Lambda (Use Cases 19–22)

#19. User-Defined Function: Total Flight Time

def calculate_total_journey_time(flight_hours, layover_hours):
    return flight_hours + layover_hours

#20. Ticket Fare Calculator

def calculate_ticket_price(class_type, base_price):
    if class_type == "Business":
        return base_price * 1.5
    elif class_type == "Economy":
        return base_price
    else:
        return base_price * 0.8  # Default for other classes

#21. Lambda Function: Fare Discount

apply_discount = lambda price: price * 0.85  # Apply 15% discount


#22. Flight Recommendation Function

def recommend_flight(budget, time, comfort):
    if budget < 300 and time > 5:
        return "Economy Flight"
    elif budget >= 300 and comfort == "High":
        return "Business Flight"
    else:
        return "Standard Flight"
    
#Section F: Comprehensions 

#23. Filter International Flights
flights = [
    {"flight": "AI101", "type": "Domestic"},
    {"flight": "AI202", "type": "International"}
]

international_flights = [flight for flight in flights if flight["type"] == "International"]
print(f"International flights: {international_flights}")


#24. Convert Fare Currency

fares = {"AI101": 8000, "AI202": 15000}
fares_usd = {flight: fare * 0.012 for flight, fare in fares.items()}  # Assuming 1 USD = 83.33 INR (approximate rate)
print(f"Fares in USD: {fares_usd}")

#25. Popular Routes Set
route_count = {
    "Delhi-Mumbai": 1500000,
    "Delhi-Goa": 600000,
    "Delhi-Dubai": 2000000
}

popular_routes = {route for route, count in route_count.items() if count > 1000000}
print(f"Popular routes: {popular_routes}")


