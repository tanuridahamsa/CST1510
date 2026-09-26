"""
RECORD CHECK  -  my version
===========================

Name  : Tanuri
Lane  : Cyber    
Date  : 25/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT

label = input("Enter label: ")
first = float(input("Enter failed logins: "))
second = float(input("Enter total attempts: "))


# ================================================================== PROCESS

difference = 0.0   
percent = 0.0      

difference = second - first
percent = (first / second) * 100

# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f" failed logins: {first:>10.2f}")
print(f" total attempts: {second:>10.2f}")
print(f" successful: {difference:>+10.2f}")
print(f" percent: {percent:>10.2f}")

successful_percent = (difference / second) * 100
print(f" Success Rate: {successful_percent:>10.2f}%")

print("=" * 34)



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you

print(137 // 45)

print(137 % 45)
