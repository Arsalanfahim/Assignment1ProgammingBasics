print("Welcome to Global Energy bill calculator")

Account_Number = input("Enter your account number: ")
print(Account_Number)

Month = input("Enter the month number (e.g., for January, enter 1): ")
print(Month)

Electricity_Plan = input("Enter your electricity plan (EFIR or EFLR): ")
print(Electricity_Plan)

Electricity_Usage = input("Enter the amount of electricity you used in month " + Month + " (in KWh): ")
print(Electricity_Usage)

Gas_Plan = input("Enter your gas plan (GFIR or GFLR): ")
print(Gas_Plan)

Gas_Usage = input("Enter the amount of gas you used in month " + Month + " (in GJ): ")
print(Gas_Usage)

Province = input("Enter the abbreviation for your province of residence (two letters): ")
print(Province)


# Setting up Calculations
fixed_monthly_fee = 120.62
fixed_natural_gas_fee = 1.32

EFIR_Price = 8.36
GFIR_Price = 4.56

kWh_usage = int(Electricity_Usage)
GJ_usage = int(Gas_Usage)

# This is for Electric Usage 
if kWh_usage <= 1000:
    kWh_cost = kWh_usage * (EFIR_Price * 0.01)
elif kWh_usage > 1000:
    EFIR_Price_Overlimit = 9.41
    kWh_cost = 1000 * (EFIR_Price * 0.01) + (kWh_usage - 1000) * (EFIR_Price_Overlimit * 0.01)
else:
    EFLR_Price = 9.11 * 0.01
    kWh_cost = kWh_usage * EFLR_Price

# This is for Gas Usage
if GJ_usage <= 950:
    GJ_cost = GJ_usage * (GFIR_Price * 0.01)
elif GJ_usage > 950:
    GFIR_Price_Overlimit = 5.89
    GJ_cost = 950 * (GFIR_Price * 0.01) + (GJ_usage - 950) * (GFIR_Price_Overlimit * 0.01)
else:
    GFLR_Price = 3.93 * 0.01
    GJ_cost = GJ_usage * GFLR_Price

# Tax Rate
province = ""

five_percent_tax_rate = ("AB", "BC", "MB", "NT", "NU", "QC", "SK", "YT")
thirteen_percent_tax_rate = ("ON")
fifteen_percent_tax_rate = ("NB", "NL", "NS", "PE")

if province in five_percent_tax_rate:
    tax_rate = 0.05
elif province in thirteen_percent_tax_rate:
    tax_rate = 0.13
elif province in fifteen_percent_tax_rate:
    tax_rate = 0.15
else:
    tax_rate = 0.00  

# Apply tax to kWh and GJ costs
kWh_cost_with_tax = kWh_cost + (kWh_cost * tax_rate)
GJ_cost_with_tax = GJ_cost + (GJ_cost * tax_rate)

total_amount_due = fixed_monthly_fee + fixed_natural_gas_fee + kWh_cost_with_tax + GJ_cost_with_tax

print("Thank you! Your total amount due now is: $","%.2f" % total_amount_due)