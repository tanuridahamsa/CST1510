"""
RECORD CHECK  -  my version
===========================

Name  : Tanuri Dahamsa
Lane  : IT
Date  : 02/10/2025

Run it:   python template.py


"""

# ==================================================================== INPUT
# 1. Ask for your three values.


label = input("Enter hostname:")        #Asks the user to enter the hostname, GB used, and GB total. float is used for a decimal value
value = float(input("Enter GB used: "))
limit = float(input("Enter GB total: "))


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]


difference = limit - value
percent = (value / limit) * 100

if percent >= 100:
    status = ("Over limit")     #Checks if the percentage is 100 or above, or at least 90, to decide the status
elif percent >= 90:
    status = ("Warning")

else:
    status = ("Ok")             #Else statements are used when if and elif are false.


# =================================================================== OUTPUT
# 4. Print the report.
#

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f" Used:      {value:>10.2f}")
print(f" Total:     {limit:>10.2f}")
print(f" Difference:{difference:>10.2f}")      #Used for right-aligned and two decimal places.
print(f" Percent:   {percent:>10.2f}%")
print(f" Status:    {status:>10}")          #Shows the status right-aligned.

print("=" * 34)


# ==========================================================================
