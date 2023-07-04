# Write your code here

print("Earned amount:")
Bubblegum = "202"
Toffee = "118"
Ice_cream = "2250"
Milk_chocolate = "1680"
Doughnut = "1075"
Pancake = "80"
print("Bubblegum: $" + Bubblegum)
print("Toffee: $"+ Toffee)
print("Ice cream: $" + Ice_cream)
print("Milk chocolate: $" + Milk_chocolate)
print("Doughnut: $" + Doughnut)
print("Pancake: $" + Pancake)
income = ( int(Bubblegum) +
           int(Toffee) +
           int(Ice_cream) +
           int(Milk_chocolate) +
           int(Doughnut) +
           int(Pancake))
inc = str(income)
print("Income: $" + inc)
staff_expenses = int(input("Staff expenses: "))
other_expenses = int(input("Other expenses "))
raw_income = income - staff_expenses - other_expenses
print("Net income: $"+str(raw_income),sep="")