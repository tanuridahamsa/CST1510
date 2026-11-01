"""
RECORD CHECK  -  my version
===========================

Name  : Tanuri
Lane  : CyberSecurity
Date  : 10/10/2026

Run it:   python template.py

"""

# =================================================================== FUNCTIONS

def status_of(percent):       #Defines the function called status_of. It checks the percentage and returns Over Limit, Warning, and Ok.
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

def print_report(label, value, limit, difference, percent, status):     #Shows the record details and the results
        print(label)
        print("Value", value)
        print("Limit", limit)
        print("Difference", difference)
        print("Percent", percent)
        print("Status", status)


# ==================================================================== INPUT

label = input("Enter source IP:")       #It will ask the user to enter a source IP, failed logins, and total attempts.
value = float(input("Enter failed logins:"))  
limit = float(input("Enter total attempts: "))   


# ================================================================== PROCESS

difference, percent = check(value, limit)    #This will call the function and calculate the difference and percent.
status = status_of(percent)     #It will call the function and checks for the status.

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


over_count = 0      #It will start counting the records which are over the limit


while True:     #It will keep asking the user to enter the records until they type quit.
    label=input("Enter source IP (or quit to stop):")

    if label == "quit":     #The loop will stop when the user enters quit
        break

    value = float(input("Enter failed logins:"))
    limit = float(input("Enter total attempts:"))

    difference, percent = check (value, limit)
    status = status_of(percent)

    if status == "Over Limit":
        over_count += 1     #It will add 1 to the counter when a record is over the limit.

    print_report(label, value, limit, difference, percent, status)

print(f"Total records over limit: {over_count}")       #This will show the total number of records which are over the limit.

print("=" * 34)


# ==========================================================================


