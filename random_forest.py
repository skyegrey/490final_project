import sklearn
from sklearn.ensemble import RandomForestClassifier
import matplotlib
import pandas as pd
import numpy as np
from import_data import import_data
from sklearn import tree
from sklearn.tree import export_graphviz
import graphviz
import matplotlib.pyplot as plt

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

# for i in range(1, 4):
#    selectedSamples = train_data.sample(frac=.10, replace=True)
#    X_partial = selectedSamples[columns[:30]]
#    y_partial = selectedSamples['Safe Website']
#    dtc = tree.DecisionTreeClassifier(max_features="auto", max_depth=3)
#    dtc = dtc.fit(X_partial, y_partial)

#    dot_data = tree.export_graphviz(dtc, feature_names=X.columns, out_file=None)
#    graph = graphviz.Source(dot_data)
#    graph.render("Depth3-" + str(i) + " 10% of Samples, with Replacement")

X_test = test_data[columns[:30]]
y_test = test_data['Safe Website']
y_test[y_test < 1] = 0

testRange = []  # [2, 3, 5, 10]
colorSelect = 0
colors = ['Green', 'Blue', 'Red', 'Purple']
for x in testRange:
    partial = train_data.sample(frac=.10, replace=True)
    X_partial = partial[columns[:30]]
    y_partial = partial['Safe Website']
    results = []
    for i in range(1, 100):
        rf = RandomForestClassifier(i, max_depth=x, max_features="auto")
        rf.fit(X_partial, y_partial)
        # score = rf.score(X_partial, y_partial)

        # print('Score for training data:', score)

        rf.predict(X_test)
        score = rf.score(X_test, y_test)

        results.append([i, score])

        # print('Score for test data:', score)

        # print(i)
    graphFrame = pd.DataFrame(results)
    graphFrame.columns = ['Number of Trees', 'Accuracy']
    # print(graphFrame)

    plt.scatter(graphFrame['Number of Trees'], graphFrame['Accuracy'], c=colors[colorSelect])
    colorSelect = colorSelect + 1

    axis = plt.gca()
    axis.set_ylim([.75, .975])
    plt.ylabel('Accuracy')
    plt.xlabel('Number of Trees')
    plt.title('Accuracy of Depth ' + str(x) + ' Random Forest')
    plt.show()


rf = RandomForestClassifier(300)
rf.fit(X, y)
score = rf.score(X, y)

print("Score on Training Data:", score)

df = pd.DataFrame(list(zip(X.columns, np.transpose(rf.feature_importances_))))
df.columns = ['Feature', 'Weight']
print(df.sort_values('Weight', ascending=False))

score = rf.score(X_test, y_test)
print("Score on Test Data:", score)

# print('Predicted Probabilities:', rf.predict_proba(X_test))





