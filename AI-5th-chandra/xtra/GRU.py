import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from keras import Sequential
from keras.layers import Dense, GRU, Dropout
from keras.utils import to_categorical
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

path = "/Users/udita/Desktop/exam/masud sir/13 chapter/content/Social_Network_Ads.csv"
data = pd.read_csv(path)

X = data[['Age', 'EstimatedSalary']].values
y = data['Purchased'].values
y_cat = to_categorical(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_cat, test_size=0.2, random_state=42)

sc = StandardScaler()
X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test)

X_train_gru = X_train_sc.reshape((X_train_sc.shape[0], X_train_sc.shape[1], 1))
X_test_gru = X_test_sc.reshape((X_test_sc.shape[0], X_test_sc.shape[1], 1))

model = Sequential()
model.add(GRU(16, activation='tanh', input_shape=(X_train_gru.shape[1], 1), return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(8, activation='relu'))
model.add(Dense(y_cat.shape[1], activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X_train_gru, y_train, epochs=50, batch_size=8, verbose=1)

pred = model.predict(X_test_gru)
pred_labels = np.argmax(pred, axis=1)
true_labels = np.argmax(y_test, axis=1)

acc = accuracy_score(true_labels, pred_labels)
print("Test Accuracy:", acc)

sample = X_test[[26]]
sample_sc = sc.transform(sample)
sample_gru = sample_sc.reshape((sample_sc.shape[0], sample_sc.shape[1], 1))
sample_pred = model.predict(sample_gru)
sample_label = np.argmax(sample_pred, axis=1)

print("Sample Features:", sample)
print("Predicted Probabilities:", sample_pred)
print("Predicted Class Label:", sample_label)

plt.plot(history.history['accuracy'], label='Accuracy')
plt.plot(history.history['loss'], label='Loss')
plt.title('GRU Model Performance')
plt.xlabel('Epochs')
plt.ylabel('Value')
plt.legend()
plt.show()
