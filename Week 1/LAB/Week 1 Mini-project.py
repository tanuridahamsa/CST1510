"""
RECORD CHECK  -  my version
===========================

Name  : Tanuri
Lane  : Cyber    
Date  : 25/09/2026

Run it:   python template.py


"""

# ==================================================================== INPUT

label = input("Enter label: ")
first = float(input("Enter failed logins: "))       #Asks the users to enter a label, failed logins, and total attempts.
second = float(input("Enter total attempts: "))


# ================================================================== PROCESS

difference = 0.0   
percent = 0.0      

difference = second - first         #Checks the difference by subtracting the second and first number.
percent = (first / second) * 100    #Checks the percentage by dividing the first and second number and then multiplying it by 100.

# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")        #This is used to format the results correctly and show the record label.
print("=" * 34)

print(f" failed logins: {first:>10.2f}")
print(f" total attempts: {second:>10.2f}")
print(f" successful: {difference:>+10.2f}")     # "+" is used to show a positive value
print(f" percent: {percent:>10.2f}")

successful_percent = (difference / second) * 100            #This will calculate the percentage of successful login attempts.
print(f" Success Rate: {successful_percent:>10.2f}%")

print("=" * 34)



# ==========================================================================

