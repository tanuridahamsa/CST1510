total_seconds = 9137

hours = total_seconds // 3600
remaining = total_seconds % 3600

minutes = remaining // 60
seconds = remaining % 60

print(total_seconds, "seconds =", hours, "hours,", minutes, "minutes,", seconds, "seconds")