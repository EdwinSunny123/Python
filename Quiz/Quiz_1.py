
#1
sales = ["200", " 340", "N/A", "500", "None", " 150 ", "800"]
total_sales = 0

for value in sales:
    if value != "N/A" and value != "None":
        total_sales += int(value)  

print("Total Sales:", total_sales)


#2
temp = [22.5, 25.1, 27.0, 30.5, 21.2, 33.1, 35.2]

fahrenheit = [c * 9/5 + 32 for c in temp]

print(fahrenheit)


#3
customer_ids = [101, 102, 103, 102, 101, 104, 105, 103]
unique_customers = set(customer_ids)

print("Unique customer count:", len(unique_customers))


#4
products = ["Pen", "Book", "Bag"]
prices = [10, 100, 500]

product_price = {products[i]: prices[i] for i in range(len(products))}

print(product_price)


#5
ratings = (4.5, 2.3, 3.8, 4.9, 1.8, 4.2)

for r in ratings:
    if r >= 4.0:
        print(r)


#6
attendance = [1, 1, 0, 1, 1, 0, 1]

total_present = attendance.count(1)
total_absent = attendance.count(0)

attendance_percentage = (total_present / len(attendance)) * 100

print("Total Present Days:", total_present)
print("Total Absent Days:", total_absent)
print("Attendance Percentage:", attendance_percentage)


#7
comments = ["Great!", "bad product", "Excellent", "worst!", "Good", "awful experience"]

positive_words = ["Great", "Excellent", "Good"]

for comment in comments:
    for word in positive_words:
        if word in comment:
            print(comment)
            break


#8
revenue = int(input("Enter revenue: "))

if revenue < 1000:
    print("Low")
elif 1000 <= revenue <= 5000:
    print("Medium")
else:
    print("High")


#9
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def display(self):
        print("Name:", self.name)
        print("Monthly Salary:", self.salary)
        print("Annual Salary:", self.annual_salary())


#10
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Final Balance:", self.balance)


account = BankAccount(0)
account.deposit(5000)
account.withdraw(2000)
account.show_balance()


