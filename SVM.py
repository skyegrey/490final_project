from import_data import import_data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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

y_test = test_data["Safe Website"]
y_test[y_test<1] = 0
X_test = test_data[columns[:30]]

y = training_data["Safe Website"]
y[y<1] = 0
X = training_data[columns[:30]]


model = svm.SVC(kernel = 'linear', C=1.0)
model.fit(X,y)

variables = pd.DataFrame(list(zip(X.columns, np.transpose(model.coef_))))
variables.columns = ['Feature', 'Weight']
print("Variable and Weights:\n", variables, "\n\n\n")
print("Percentage Accuracy on Test Data:",model.score(X_test,y_test))

score_list = []

#for i in range(30):
    #print("It's working")
    #print(i)
    #for j in range(i+1,30):
        #X = training_data[[columns[i],columns[j]]]
        #X_test = test_data[[columns[i],columns[j]]]
        #model.fit(X,y)
        #score_list.append(list([model.score(X_test,y_test),column_dict[i],column_dict[j]]))

#score_list.sort(reverse=True)


best_pair_list = []
repeats = []

#for item in score_list:

    #i = item[1]
    #j = item[2]

    #if i not in repeats and j not in repeats:
        #best_pair_list.append(item)

        #repeats.append(i)
        #repeats.append(j)


#print(best_pair_list)

#model = svm.SVC(kernel = 'linear', C=1.0)

#X = training_data[[columns[5],columns[7],columns[13],columns[27],columns[6],columns[25],columns[8],columns[29]]]
#X_test = test_data[[columns[5],columns[7],columns[13],columns[27],columns[6],columns[25],columns[8],columns[29]]]
#model.fit(X,y)
#print(model.score(X,y))
