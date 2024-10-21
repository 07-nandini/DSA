age = int(input("Enter your age: "))
num_tickets = int(input("Enter number of tickets: "))

# Initialize ticket prices
regular_price = 50
senior_citizen_price = 30
children_price = 20

# Determine the price based on age
if age >= 60:
    ticket_price = senior_citizen_price
elif age <= 12:
    ticket_price = children_price
else:
    ticket_price = regular_price

# Calculate total cost
total_cost = ticket_price * num_tickets

# Display the total cost
print(f"Total cost for {num_tickets} tickets: {total_cost}")
