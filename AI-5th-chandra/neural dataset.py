import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
# Create the dataset
data = pd.DataFrame({
    'Outlook': ['Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Sunny',
                'Overcast', 'Rainy', 'Rainy', 'Sunny', 'Rainy', 'Overcast',
                'Overcast', 'Sunny'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool',
                    'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal',
                 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Windy': ['FALSE', 'TRUE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'TRUE',
              'FALSE', 'FALSE', 'FALSE', 'TRUE', 'TRUE', 'FALSE', 'TRUE'],
    'Play': ['NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'YES', 'NO', 'YES', 'YES', 'YES',
             'YES', 'YES', 'NO']
})
# Encode categorical features using one-hot encoding
data_encoded = pd.get_dummies(data.drop('Play', axis=1))
# Encode the target variable
data['Play'] = data['Play'].map({'NO': 0, 'YES': 1})
# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data_encoded, data['Play'], test_size=0.3, random_state=42)
# Initialize the neural network model
model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
# Train the model
model.fit(X_train, y_train)
# Predict and evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("Predictions on test data:")
print(y_pred)