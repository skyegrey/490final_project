import sklearn
from sklearn.ensemble import RandomForestClassifier
import matplotlib
import pandas as pd
import numpy as np
from import_data import import_data

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

y = train_data['Safe Website']
y[y < 1] = 0

X = train_data[columns[:30]]

rf = RandomForestClassifier(200)
rf.fit(X, y)
score = rf.score(X, y)

print('Score for training data:', score)
df = pd.DataFrame(list(zip(X.columns, np.transpose(rf.feature_importances_))))
df.columns = ['Feature', 'Weight']
print(df.sort_values('Weight', ascending=False))

X_test = test_data[columns[:30]]
y_test = test_data['Safe Website']
y_test[y_test < 1] = 0

rf.predict(X_test)
score = rf.score(X_test, y_test)

print('Score for test data:', score)
print('Predicted Probabilities:', rf.predict_proba(X_test))





