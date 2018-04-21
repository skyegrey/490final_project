import csv
import numpy as np


def import_data(csv_string):
    """
    Takes in a csv string, returns a list of values as integers
    :param csv_string: name of the csv file to take in
    :return: a numpy array of feature values
    """
    values = []
    with open(csv_string, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            for i in range(0, len(row)):
                row[i] = int(row[i])
            values.append(row)

    values = np.array(values)

    print(values)

    return values
