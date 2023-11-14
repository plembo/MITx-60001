# Set initial state variables
portion_down_payment = 0.25   # Percent of home value for down payment
r = 0.04   # Rate of investment return

# Input salary, portion saved, and total cost of home
total_cost = float(input('How much is the home: '))
annual_salary = float(input('Please enter the annual salary of the job: '))
portion_saved = float(input('Enter the amount to be saved each month as ratio (example: 0.1 for 10%)'))

# Monthly salary and down payment
monthly_salary = annual_salary/12
monthly_return = r/12
down_payment = portion_down_payment*total_cost

# Months and current savings
months = 0
current_savings = 0

while current_savings <= down_payment:
    
    # Increase current savings using savings and return on investment
    current_savings += portion_saved*monthly_salary + current_savings*monthly_return
    months += 1

print('%s months required to save %s down payment for a %s dollary home with a salary of %s setting aside %s'
     % (months, down_payment, total_cost, annual_salary, portion_saved))
