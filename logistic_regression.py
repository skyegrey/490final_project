from import_data import import_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

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

train_data = import_data('train.csv')
test_data = import_data('test.csv')

# for i in range(0, 30):
#    pd.crosstab(train_data[columns[i]], test_data['Safe Website']).plot(kind='bar')
#    plt.title(columns[i])
#    plt.xlabel(columns[i])
#    plt.ylabel('Frequency')
#    plt.show()

y = train_data['Safe Website']
y[y < 1] = 0

X = train_data[columns[:30]]

regression = LogisticRegression()
regression.fit(X, y)
score = regression.score(X, y)
guessing = y.mean()

print("Score by guessing always unsafe:", guessing)
print("Score on Training Data:", score, "\n\n\n")


variables = pd.DataFrame(list(zip(X.columns, np.transpose(regression.coef_))))
print("Variable and Weights:\n", variables, "\n\n\n")

regression.predict(test_data[columns[:30]])
y = test_data['Safe Website']
y[y < 1] = 0
score = regression.score(test_data[columns[:30]], y)
print("Percentage Accuracy on Test Data:", score)

