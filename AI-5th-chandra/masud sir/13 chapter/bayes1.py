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

def train_naive_bayes(data):
    label_counts = {}
    feature_counts = {}
    for row in data:
        outlook, temp, humidity, windy, label = row
        label_counts[label] = label_counts.get(label, 0) + 1
        if label not in feature_counts:
            feature_counts[label] = {"Outlook": {}, "Temp": {}, "Humidity": {}, "Windy": {}}
        feature_counts[label]["Outlook"][outlook] = feature_counts[label]["Outlook"].get(outlook, 0) + 1
        feature_counts[label]["Temp"][temp] = feature_counts[label]["Temp"].get(temp, 0) + 1
        feature_counts[label]["Humidity"][humidity] = feature_counts[label]["Humidity"].get(humidity, 0) + 1
        feature_counts[label]["Windy"][windy] = feature_counts[label]["Windy"].get(windy, 0) + 1
    return label_counts, feature_counts

def predict_naive_bayes(x, label_counts, feature_counts):
    total = sum(label_counts.values())
    probs = {}
    feature_names = ["Outlook", "Temp", "Humidity", "Windy"]
    for label in label_counts:
        probs[label] = label_counts[label] / total
        for i, feature in enumerate(feature_names):
            value = x[i]
            count = feature_counts[label][feature].get(value, 0)
            num_options = len(feature_counts[label][feature])
            probs[label] *= (count + 1) / (label_counts[label] + num_options)
    return probs, max(probs, key=probs.get)

label_counts, feature_counts = train_naive_bayes(dataset)
test_sample = ['sunny', 'cool', 'high', 'true']
probs, prediction = predict_naive_bayes(test_sample, label_counts, feature_counts)

print("Test Sample:", test_sample)
print("Predicted Class:", prediction)
print("Class Probabilities:", probs)
