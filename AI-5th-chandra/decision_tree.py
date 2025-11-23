from sklearn import tree
import pandas as pd
import matplotlib.pyplot as plt

# Prepare the data
golf = pd.DataFrame()
golf['Outlook'] = ['Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Sunny',
                     'Overcast', 'Rainy', 'Rainy', 'Sunny', 'Rainy', 'Overcast',
                     'Overcast', 'Sunny']
golf['Temperature'] = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool',
                         'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild']
golf['Humidity'] = ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal',
                      'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High']
golf['Windy'] = ['FALSE', 'TRUE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'TRUE',
                   'FALSE', 'FALSE', 'FALSE', 'TRUE', 'TRUE', 'FALSE', 'TRUE']
golf['Play'] = ['NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'YES', 'NO', 'YES', 'YES', 'YES',
                  'YES', 'YES', 'NO']
print(golf)

# One-hot encoding
one_hot_data = pd.get_dummies(golf[['Outlook', 'Temperature', 'Humidity', 'Windy']])

# Train the model
clf = tree.DecisionTreeClassifier()
clf_train = clf.fit(one_hot_data, golf['Play'])

# Visualize the tree in text format
tree_text = tree.export_text(clf_train, feature_names=list(one_hot_data.columns.values))
print(tree_text)

# If you want a simple visualization using matplotlib (optional)
fig = plt.figure(figsize=(12, 8))
_ = tree.plot_tree(clf_train, feature_names=list(one_hot_data.columns), class_names=['Not_Play', 'Play'], filled=True)

plt.show()

# Make a prediction
prediction = clf_train.predict([[0, 0, 1, 0, 1, 0, 0, 1, 1, 0]])
print(prediction)