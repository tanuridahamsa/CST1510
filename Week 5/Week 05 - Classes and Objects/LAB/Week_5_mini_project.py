"""
RECORD CHECK  -  my version
===========================

Name  : Tanuri
Lane  : Cybersecurity
Date  : 25/10/2026

Run it:   python template.py


"""

# ====================================================================== CLASS
class Record:
    over_limit_count = 0    #This will start the counter from 0.

    """this stores the label,value, and limit of a record"""
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    """this will check the status of the report which is based on the percentage"""
    def status(self):
        percent = (self.value / self.limit) * 100       #It's going to calculate the percentage of the record.

        if percent >= 100:
            return "OVER LIMIT"

        elif percent >= 90:
            return "WARNING"

        else:
            return "OK"

# ==================================================================== RECORDS
def load_records(path):
    """This will read the file and store the records in a list"""
    records = []    #It's going to create an empty list to store the records.

    with open(path) as f:   #This will open the file and read the records from it.
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))   #This is going to add each record into the list.

    return records

records = load_records("Week 5/Week 05 - Classes and Objects/LAB/cyber_records.txt")   #It's going to call the function and load the records from the file.

# ==================================================================== OUTPUT
over_limit_count = 0
for record in records:  #This loop will go through each record and show it details.
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here
    print(f"Source IP           :{record.label}")
    print(f"Failed attempts     :{record.value}")
    print(f"Total Attempts      :{record.limit}")
    print(f"Status              :{record.status()}")

    if record.status() == "OVER LIMIT":     #This is going to add 1 to the counter if the record is Over the limit.
        over_limit_count += 1

    print("=" * 34)
    
print(f"Total over limit count: {over_limit_count}")    #It will show the total number of records which will be over the limit.

# ==========================================================================

