"""
RECORD CHECK  -  my version
===========================

Name  : Tanuri Dahamsa
Lane  : IT
Date  : 02/10/2025

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.


label = input("Enter hostname:")
value = float(input("Enter GB used: "))
limit = float(input("Enter GB total: "))


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]


difference = limit - value
percent = (value / limit) * 100

if percent >= 100:
    status = ("Over limit")

elif percent >= 90:
    status = ("Warning")

else:
    status = ("Ok")


# =================================================================== OUTPUT
# 4. Print the report.
#

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f" Used: {value:>10.2f}")
print(f" Total: {limit:>10.2f}")
print(f" Difference: {difference:>10.2f}")
print(f" Percent: {percent:>10.2f}%")
print(f" Status: {status:>10}")

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
