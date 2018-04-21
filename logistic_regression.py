from import_data import import_data
import matplotlib.pyplot as plt
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

test_data = import_data('train.csv')
for i in range(0, 30):
    pd.crosstab(test_data[columns[i]], test_data['Safe Website']).plot(kind='bar')
    plt.title(columns[i])
    plt.xlabel(columns[i])
    plt.ylabel('Frequency')

    plt.show()
