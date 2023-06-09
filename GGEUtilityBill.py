print ("Welcome to Global Energy bill calculator")

# Account_Number = input("Enter your account number: ")
# print(Account_Number)

Month = input("Enter the month number (e.g, for January, enter 1): ")
print(Month)

# Electricity_Plan = input("Enter your electricity plan (EFIR or EFLR): ")
# print(Electricity_Plan)

Electricity_Usage = input("Enter the amount of electricity you used in month " + Month + " (in KWh): ")
print(Electricity_Usage)


# Gas_Plan = input("Enter your gas plan (GFIR or GFLR):")
# print(Gas_Plan)

# Gas_Usage = input("Enter the amount of gas you used in month " + Month + " (in GJ): ")
# print(Gas_Plan)

# Province = input("Enter the abbreviation for your province of residence (two letters): ")
# print(Province)

# kWh_usage = input("Enter the amount of electricity you used in month (in KWh): ")
# print(kWh_usage)

fixed_monthly_fee = (120.62)

EFIR_Price = 8.36
EFLR_Price = 9.11

GFIR_Price = 4.56
GFLR_Price = 3.93

kWh_usage = int(Electricity_Usage)
GJ_usage = 800


if kWh_usage <= 1000:
    kWh_cost = kWh_usage * (EFIR_Price * 0.01)
elif kWh_usage > 1000:
    EFIR_Price_Overlimt = 9.41

    kWh_cost = 1000 * (EFIR_Price * 0.01) + (kWh_usage - 1000) * (EFIR_Price_Overlimt * 0.01)

Total_Cost = fixed_monthly_fee + kWh_cost
print(Total_Cost)









print("Thank you! Your total amount due now is:")
















