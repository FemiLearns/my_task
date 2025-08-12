#Task 10 School fees breakdown
School_Name = input("Enter School Name: ")
Tuition = float(input("Enter Tuition Fee: "))
Hostel_Fee = float(input("Enter Hostel fee: "))
Feeding_Fee = float(input("Enter Feeding fee: "))
Total_fees = Tuition + Hostel_Fee + Feeding_Fee
print(f"Total Fees is {Total_fees}")
print(f"""    {School_Name},
            Idi-Aba, Abeokuta.
            Fees Breakdown
      Tuition fees = {Tuition}
      Hostel fees = {Hostel_Fee}
      Feeding fees = {Feeding_Fee}
      Total Fees payable = {Total_fees}
      Thanks for your patronage""" )
