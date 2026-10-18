"""
RECORD CHECK  -  my version
===========================

Name  : Tanuri
Lane  : CyberSecurity 
Date  : 17/10/2026

Run it:   python template.py

"""

# =================================================================== FUNCTIONS
def check_record(value, limit):
    """this caluclates the difference, percent, and status"""
    difference = limit - value 
    percent = (value / limit) * 100
    
    if percent >= 100:
        status = "Over Limit"
    
    elif percent >= 90:
        status = "Warning"
    
    else:
        status = "Ok"
    
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """this will show the record details and results"""

    if status == "Total":
        print("Total records Over Limit:", value)
        return 

    if status == "Error":
        print(label)
        return

    print("=" * 34)
    print(f"Record Check - {label}")
    print("=" * 34)
    print(f"value           :{value:>10.2f}")
    print(f"limit           :{limit:>10.2f}")
    print(f"difference      :{difference:>10.2f}")
    print(f"percent         :{percent:>10.2}%")
    print(f"status          :{status:>10}")
    print("=" * 34)



# ====================================================================== STORE
def load_records(path):
    """this will open records.txt and read the records from it."""
    records = []

    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")

            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })
    return records 


try:
    records = load_records("records.txt")

except FileNotFoundError:
    records = []
    print_report("File is not found","","","","","Error")


# =============================================================== PROCESS + OUTPUT
over_count = 0

with open("results.txt", "w") as f:
    for record in records:
        label = record["label"]
        value = record["value"]
        limit = record["limit"]

        difference, percent, status = check_record(value, limit)

        print_report(label, value, limit, difference, percent, status)

        f.write(f"{label}, {status}\n")

        if status == "Over Limit":
            over_count += 1

print_report("", over_count, "","","","Total")

# ==========================================================================

