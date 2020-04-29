import csv


def shopping_cost(filename):
    account = None
    total = 0.0
    total_items = 0

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

    return account, total, total_items, (i+1)


def read_shopping_data(filename):
    data = []
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(f)
        for row in rows:
            record = tuple(row)
            data.append(record)
    return data

