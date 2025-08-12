#Task 6 Electricity Bill Formatter
Full_Name = input("Enter Customer's full name: ")
Units_Consumed = int(input("Enter Units consumed in KWh: "))
Cost_per_Unit = float(input("Enter cost per Unit: "))
Total_bill = Units_Consumed * Cost_per_Unit
print(f"Dear {Full_Name},\nYour bill for the month of august is {Total_bill}")
