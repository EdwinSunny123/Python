#1 Ticket Fare Validation

Ticket_fare = "1500"
print(type(Ticket_fare))
Ticket_fare = int(Ticket_fare)
print(type(Ticket_fare))
GST = Ticket_fare * 18/100
print(GST)


#2 Concession Eligibility Check

ticket_amount = 4800
if ticket_amount >= 5000:
    print("Concession Applied")
else:
    print("No Concession")


#3 Seat Availability Status

status_available_seats = 0
if status_available_seats > 0:
    print("Seats Available")
else:
    print("No Seats Available")


#4 Railway Wallet Deduction

Railway_wallet_balance = 2000
ticket_cost = 1500
Railway_wallet_balance -= ticket_cost
print(Railway_wallet_balance)


#5 Monthly Season Ticket EMI

Monthly_ticket_price = 12000
months = 6
EMI = Monthly_ticket_price / months
print(EMI)


#6 Ticket Booking Status Checker

status = "confirmed"

if status == "confirmed":
    print("Your ticket is confirmed. Have a happy journey!")
elif status == "waiting":
    print("Your ticket is on the waiting list. Please check again later.")
elif status == "cancelled":
    print("Your ticket has been cancelled.")
else:
    print("Invalid booking status.")


#7 Multiple Ticket Processing

Ticket = 5
for i in range(Ticket):
    print("Ticket Processed")


#8 Payment Retry System

retry_count =0
while retry_count<3:
  print("Attempt Failed",retry_count+1)
  retry_count+=1


#9 Login Attempt Lock

login_count=0
while login_count<3:
  print("Wrong Attempts exceeds",login_count+1)
  login_count+=1
  if login_count==3:
    print("Account Lock")
    break
  

#10 Skip Cancelled Tickets

Ticket=["confirm","cancelled","cancelled","confirm","cancelled","confirm"]
for T in Ticket:
  if T== "cancelled":
    continue
  else:
       print("Ticket Confirmed")


#11 Stop Tatkal Booking

Available_seats=0
while Available_seats<5:
  print("Booking Confirmed")
  Available_seats+=1
  if Available_seats==5:
    print("Booking Cancelled")
    break
  

#12 Skip Invalid Station Code

station_code=[909,404,103,"xxx",202,"303","xxx"]
for s in station_code:
  if s=="xxx":
    continue
  else:
    print(s)


#13 Placeholder for Refund Logic

Placeholder="NOt Refunded"
if Placeholder=="NOt Refunded":
  pass


#14 Prime Ticket Number Check 

ticket_number = int(input("Enter ticket number: "))

if ticket_number <= 1:
    print("Not a Prime Ticket Number")
else:
    is_prime = True

    for i in range(2, ticket_number):
        if ticket_number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Ticket Number")
    else:
        print("Not a Prime Ticket Number")



#15 Even–Odd Coach Numbers

for i in range(1,21):
  if i%2==0:
    print("Even Coach Number",i)
  else:
    print("Odd Coach Number",i)


#16 Passenger Rating Stars

rows =4
for i in range(1,rows+1):
  for j in range(i):
     print("*",end=" ")
  print ()


#17 Railway Sale Banner

rows =4
for i in range(1,rows+1):
  for j in range(i,rows+1):
     print("*",end=" ")
  print ()


#18 Booking Count Pyramid


bookings = int(input("Enter number of bookings: "))

for i in range(1, bookings + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


#19 Passenger Username Validation

username = input("Enter passenger username: ")

if len(username) >= 6:
    print("Valid Username")
else:
    print("Invalid Username")


#20 Email Domain Checker

email = input("Enter passenger email: ")

if email.endswith("@gmail.com"):
    print("Valid email: Gmail account detected")
else:
    print("Invalid email: Only @gmail.com is allowed")


#21 Train Name Formatting

train_name = input("Enter train name: ")

print("Uppercase :", train_name.upper())
print("Title Case:", train_name.title())


#22 Passenger Cart Items

cart = ["Sleeper Ticket", "AC Ticket", "Meal"]

# Add new item
cart.append("Water Bottle")

# Remove an item
cart.remove("Meal")

# Display cart size
print("Cart Items:", cart)
print("Cart Size:", len(cart))


# 23 Ticket Fare List

Ticket_Fare=[101,103,104,105,106]
print("Maximum Fare",max(Ticket_Fare))
print("Minimum Fare",min(Ticket_Fare))
print("Total Fare",sum(Ticket_Fare))


#24 Immutable Ticket Details (Tuple)

Ticket_Number=(101,102,103,104,105)
Ticket_Number[0]=106


#25 Top 3 Most Booked Trains

trains = [
    "Rajdhani Express",
    "Shatabdi Express",
    "Duronto Express",
    "Garib Rath",
    "Intercity Express"
]

# Top 3 most booked trains using list slicing
top_3_trains = trains[:3]

print("Top 3 Most Booked Trains:")
for train in top_3_trains:
    print(train)

