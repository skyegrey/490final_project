from import_data import import_data
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

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

################################################################################
# Getting the data

column_dict = {}
for i in range(0,30):
    column_dict[i] = columns[i]

training_data = import_data('train.csv')
test_data = import_data('test.csv')

y = training_data["Safe Website"]
y[y<1] = 0
X = training_data[columns[:30]]

y_test = test_data["Safe Website"]
y_test[y_test<1] = 0
X_test = test_data[columns[:30]]
################################################################################

# Choosing 5 random sample of 10% of the training data to test different values of k
# For each sample, choose different values of k
# Report choice of k and percent accuracy of the model
# This was done for Euclidean distance and Hamming distance. Just change argument of model.

list_of_colors = ["green","red","blue","orange","teal"]
for j in range(0,5):

    partial = training_data.sample(frac=.10, replace=True)
    X_partial = partial[columns[:30]]
    y_partial = partial["Safe Website"]
    x_value = []
    y_value = []

    for k in range(1,21):
        model = KNeighborsClassifier(n_neighbors=k, metric="hamming")
        model.fit(X, y)

        print("Using k=",k)
        print("Percentage Accuracy on Test Data:",model.score(X_partial,y_partial))
        print("")

        x_value.append(k)
        y_value.append(model.score(X_partial,y_partial))

        plt.scatter(x_value,y_value, c=list_of_colors[j])

plt.show()
