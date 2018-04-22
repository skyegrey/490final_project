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
X_test = test_data["Safe Website"]

model = KNeighborsClassifier()
model.fit(X,y)


print(model.score(X_test,y_test))