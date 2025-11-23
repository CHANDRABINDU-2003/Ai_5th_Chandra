import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score, classification_report

# Manually transcribing the dataset from the image
data = {
    "Outlook": [
        "sunny", "sunny", "overcast", "rainy", "rainy", "rainy", "overcast",
        "sunny", "sunny", "rainy", "sunny", "overcast", "overcast", "rainy"
    ],
    "Temperature": [
        "hot", "hot", "hot", "mild", "cool", "cool", "cool",
        "mild", "cool", "mild", "mild", "mild", "hot", "mild"
    ],
    "Humidity": [
        "high", "high", "high", "high", "normal", "normal", "normal",
        "high", "normal", "normal", "normal", "high", "normal", "high"
    ],
    "Windy": [
        False, True, False, False, False, True, True,
        False, False, False, True, True, False, True
    ],
    "Play": [
        "no", "no", "yes", "yes", "yes", "no", "yes",
        "no", "yes", "yes", "yes", "yes", "yes", "no"
    ]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Encoding categorical variables
label_encoders = {}
for column in df.columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Splitting the data into features (X) and target (y)
X = df.drop("Play", axis=1)
y = df["Play"]

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creating and training the Naive Bayes classifier
model = CategoricalNB()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=label_encoders["Play"].classes_)

print("Accuracy:", accuracy)
print("\nClassification Report:\n", report)
