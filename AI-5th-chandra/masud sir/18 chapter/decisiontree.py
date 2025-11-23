from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

dataset = [
    ['sunny', 'hot', 'high', 'false', 'no'],
    ['sunny', 'hot', 'high', 'true', 'no'],
    ['overcast', 'hot', 'high', 'false', 'yes'],
    ['rainy', 'mild', 'high', 'false', 'yes'],
    ['rainy', 'cool', 'normal', 'false', 'yes'],
    ['rainy', 'cool', 'normal', 'true', 'no'],
    ['overcast', 'cool', 'normal', 'true', 'yes'],
    ['sunny', 'mild', 'high', 'false', 'no'],
    ['sunny', 'cool', 'normal', 'false', 'yes'],
    ['rainy', 'mild', 'normal', 'false', 'yes'],
    ['sunny', 'mild', 'normal', 'true', 'yes'],
    ['overcast', 'mild', 'high', 'true', 'yes'],
    ['overcast', 'hot', 'normal', 'false', 'yes'],
    ['rainy', 'mild', 'high', 'true', 'no']
]

X = [row[:-1] for row in dataset]
y = [row[-1] for row in dataset]

encoders = []
X_encoded = []
for i in range(len(X[0])):
    le = LabelEncoder()
    col = [row[i] for row in X]
    X_encoded.append(le.fit_transform(col))
    encoders.append(le)
X_encoded = list(map(list, zip(*X_encoded)))

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X_encoded, y)

test_sample = ['sunny', 'cool', 'high', 'true']
for i in range(len(test_sample)):
    test_sample[i] = encoders[i].transform([test_sample[i]])[0]

prediction = clf.predict([test_sample])[0]
print("Test Sample:", ['sunny', 'cool', 'high', 'true'])
print("Predicted Class:", prediction)

plt.figure(figsize=(12,8))
plot_tree(clf, feature_names=['Outlook','Temp','Humidity','Windy'], class_names=['no','yes'], filled=True)
plt.show()
