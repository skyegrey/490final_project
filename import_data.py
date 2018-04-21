import csv


def import_data(csv_string):
    values = []
    with open(csv_string, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            for i in range(0, len(row)):
                row[i] = int(row[i])
            values.append(row)

    for i in range(0, 100):
        print(values[i])

    return values