import sys
import csv

if len(sys.argv) != 2:
    raise SystemExit('Usage: reading_file.py filename')

account = None
total = 0.0
total_items = 0

filename = sys.argv[1]

with open(filename) as f:
    rows = csv.reader(f)
    header = next(f)
    for i, row in enumerate(rows):
        row[2] = int(row[2])
        row[6] = float(row[6])

        if account is None:
            account = row[1]

        total_items += row[2]
        total += row[2] * row[6]

print("Account name: {}".format(account))
print("Total items: {:<5}".format(total_items))
print("Total: {:<10.2f}".format(total))
print("Number of lines processed: {:<5}".format(i+1))