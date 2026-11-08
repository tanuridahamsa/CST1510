"""
RECORD CHECK  -  my version
===========================

Name  : Tanuri
Lane  : CyberSecurity
Date  : 8/11/2026

Run it:   python template.py


"""

import pandas as pd

# ==================================================================== LOAD
df = pd.read_csv(r"C:\Users\tanur\Documents\CST1510\Week 6\Week 06 - Pandas\Week 06 - Pandas\LAB\cyber_records.csv")   #This will read the csv file and load the data into a DataFrame

# ================================================================= PROCESS
df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100   #This is going to calculate the percentage of failed logins

df["status"] = df["percent"].apply(   #This will choose a status which will be based on the percentage
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p>= 90 else "OK"
)

# ================================================================== OUTPUT
print(df)  #This is used to show all the records

warning_records = df[df["status"] != "OK"]  #This will show the group of records that are not OK
print(warning_records)

status_count = df.groupby("status").size()  #This is going to the group the records by their status and count them
print(status_count)

df.to_csv(r"C:\Users\tanur\Documents\CST1510\Week 6\Week 06 - Pandas\Week 06 - Pandas\LAB\cyber_report.csv", index=False)  #This will save all the records into a new CSV file

import matplotlib.pyplot as plt

status_count.plot(kind = "bar")  #This will create a bar chart which will show the status counts
plt.title("Cyber Security Status")
plt.savefig(r"C:\Users\tanur\Documents\CST1510\Week 6\Week 06 - Pandas\Week 06 - Pandas\LAB\cyber_status.png")  #This is going to save the bar chart as an image
plt.show()   #This is going to display the bar chart

# ==========================================================================
