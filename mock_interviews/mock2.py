"""
1. Basic Info (Data Types & Operators):
- Find the total sales in 14 days.
- Find the average daily sales.
- Find the highest and lowest sales days.
"""

sales = [1200, 1500, 1700, 800, 950, 2000, 2100, 1750, 1600, 1850, 1950, 2200, 2500, 3000]
total_sales=sum(sales)
print(total_sales)
avearge=total_sales/len(sales)
print("Average Sales:", avearge)
print(max(sales))
print(min(sales))


"""
3. List Operations:
- Create a new list that contains only the sales above ₹2000.
- Sort the sales list in descending order.
- Reverse the original sales list.

"""

sales = [2450, 2500, 2000, 3000, 2600, 2200, 2100, 2450, 2250, 2005, 2700, 2220]
sales.sort()
print(sales)
sales.sort(reverse=True)
print(sales)


"""
4. Decision Making (If-Else):
- If the total sales are above ₹20,000, print "Good Performance".
- Else print "Needs Improvement".

"""

sales = [2450, 2500, 2000, 3000, 2600, 2200, 2100, 2450, 2250, 2005, 2700, 2220]
total_sales = sum(sales)
if total_sales > 20000:
    print('good performance')
else:
    print('needs improvement')



"""
5. Bonus (Optional - for extra points):
- Accept a user input for a target sales number (e.g., ₹1800).
- Find how many days met or exceeded this target.

"""

sales = [2450, 2500, 2000, 1800, 2600, 2200, 2100, 2450, 2250, 2005, 2700, 2220]
target = int(input("Enter your target sales: "))

count = 0   

for i in sales:
    if i >= target:
        count += 1

print(count)

