hours = input("Enter Hours:")
hours = float(hours)
rate = input("Enter rate per hour:")
rate = float(rate)

pay = 0

if hours > 40:
    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * (rate * 1.5)
    pay = regular_pay + overtime_pay
else:
    pay = hours * rate

print(pay)