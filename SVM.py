from import_data import import_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import svm

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

column_dict = {}
for i in range(0,30):
    column_dict[i] = columns[i]

training_data = import_data('train.csv')
test_data = import_data('test.csv')


y = training_data["Safe Website"]
y[y<1] = 0
X = training_data[columns[:30]]


model = svm.SVC(kernel = 'linear', C=1.0)
model.fit(X,y)

score_list = []

for i in range(30):
    for j in range(i+1,30):
        X = training_data[[columns[i],columns[j]]]
        model.fit(X,y)
        score_list.append(list([model.score(X,y),i,j]))

score_list.sort(reverse=True)


best_pair_list = []
repeats = []

for item in score_list:

    i = item[1]
    j = item[2]

    if i not in repeats and j not in repeats:
        best_pair_list.append(item)

        repeats.append(i)
        repeats.append(j)


print(best_pair_list)