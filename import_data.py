import csv
import numpy as np
import pandas as pd

columns = ['Using IP Address', 'Long URL', 'Using URL Shortening', 'URL has @ Symbol',
           'Redirect Using //', 'Adding Prefix or Suffix to Domain', 'Subdomain and Multisubdomains',
           'HTTPS', 'Domain Registration Length', 'Favicon', 'Using Non-standard Port',
           'Existence of HTTPS Token in Domain', 'Request URL', 'URL Anchor',
           'Links in metascript and Link Tabs', 'Server Form Handler',
           'Submitting Information to Email', 'Abnormal URL', 'Website Forwarding',
           'Status Bar Customization', 'Disabling Right Click', 'Using Pop-up Window',
           'IFrame Redirection', 'Age of Domain', 'DNS Record', 'Website Traffic', 'Page Rank',
           'Google Index', 'Number of Links Pointing to Page', 'Statistical Reports Based Feature',
           'Safe Website']


def import_data(csv_string):
    """
    Takes in a csv string, returns a list of values as integers
    :param csv_string: name of the csv file to take in
    :return: data frame containing integer values of feature with labeled columns
    """
    values = []
    with open(csv_string, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            for i in range(0, len(row)):
                row[i] = int(row[i])
            values.append(row)

    values = np.array(values)
    value_table = pd.DataFrame(values)
    value_table.columns = ['Using IP Address', 'Long URL', 'Using URL Shortening', 'URL has @ Symbol',
                           'Redirect Using //', 'Adding Prefix or Suffix to Domain', 'Subdomain and Multisubdomains',
                           'HTTPS', 'Domain Registration Length', 'Favicon', 'Using Non-standard Port',
                           'Existence of HTTPS Token in Domain', 'Request URL', 'URL Anchor',
                           'Links in metascript and Link Tabs', 'Server Form Handler',
                           'Submitting Information to Email', 'Abnormal URL', 'Website Forwarding',
                           'Status Bar Customization', 'Disabling Right Click', 'Using Pop-up Window',
                           'IFrame Redirection', 'Age of Domain', 'DNS Record', 'Website Traffic', 'Page Rank',
                           'Google Index', 'Number of Links Pointing to Page', 'Statistical Reports Based Feature',
                           'Safe Website']
    # print(value_table)

    return value_table
