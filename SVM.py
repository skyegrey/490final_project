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

# Getting the data

training_data = import_data('train.csv')
test_data = import_data('test.csv')

y_test = test_data["Safe Website"]
y_test[y_test<1] = 0
X_test = test_data[columns[:30]]

y = training_data["Safe Website"]
y[y<1] = 0
X = training_data[columns[:30]]

#################################################################################

# Building the linear model
linear_model = svm.SVC(kernel = 'linear', C=1.0)
linear_model.fit(X,y)

# Printing variable weights and accuracy on test data

linear_variables = pd.DataFrame(list(zip(X.columns, np.transpose(linear_model.coef_))))
linear_variables.columns = ['Feature', 'Weight']
#print("Variable and Weights:\n", linear_variables, "\n\n\n")
#print("Percentage Accuracy on Test Data:",linear_model.score(X_test,y_test))

################################################################################

# Choosing 5 random sample of 10% of the training data to test a polynomial kernel
# For each sample, test different polynomial kernels (degree from 1 to 20)
# Report degree of kernel and percentage accuracy

list_of_colors = ["green","red","blue","orange","teal"]
for j in range(0,5):

    partial = training_data.sample(frac=.10, replace=True)
    X_partial = partial[columns[:30]]
    y_partial = partial["Safe Website"]
    x_value = []
    y_value = []

    for i in range(1,21):
        poly_model = svm.SVC(kernel = 'poly', degree=i, C=1.0)
        poly_model.fit(X,y)

        print("Using polynomial with degree:",i)
        print("Percentage Accuracy on Test Data:",poly_model.score(X_partial,y_partial))
        print("")

        x_value.append(i)
        y_value.append(poly_model.score(X_partial,y_partial))

        plt.scatter(x_value,y_value, c=list_of_colors[j])

plt.show()

################################################################################


# Used for determining feature importance by running SVM with 2 features
# best_pair_list prints 15 distinct pairs of feature indices, ordered by best accuracy based on test data

score_list = []

#for i in range(30):
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