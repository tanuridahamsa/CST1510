"""
RECORD CHECK  -  my version
===========================

Name  : Tanuri
Lane  : CyberSecurity
Date  : 10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def status_of(percent):
    if percent >= 100:
        return "Over Limit"
        
    elif percent >= 90:
        return "Warning"

    else:
        return "Ok" 

def check(value, limit):
        
        difference = limit - value
        percentage = (value / limit) * 100
        return difference, percentage

def print_report(label, value, limit, difference, percent, status):
        print(label)
        print("Value", value)
        print("Limit", limit)
        print("Difference", difference)
        print("Percent", percent)
        print("Status", status)


# ==================================================================== INPUT

label = input("Enter source IP:") 
value = float(input("Enter failed logins:"))  
limit = float(input("Enter total attempts: "))   


# ================================================================== PROCESS

difference, percent = check(value, limit)
status = status_of(percent)

# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Failed logins:  {value:>10.2f}")
print(f"Total attempts: {limit:>10.2f}")
print(f"Difference:     {difference:>10.2f}")
print(f"Percent:        {percent:>10.2f}")
print(f"Status:         {status}")


over_count = 0

while True:
    label=input("Enter source IP (or quit to stop):")

    if label == "quit":
        break 

    value = float(input("Enter failed logins:"))
    limit = float(input("Enter total attempts:"))

    difference, percent = check (value, limit)
    status = status_of(percent)

    if status == "Over Limit":
        over_count += 1

    print_report(label, value, limit, difference, percent, status)

print(f"Total records over limit: {over_count}")

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
