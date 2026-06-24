import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from features import extract_features

df = pd.read_csv("urls.csv")

X = df["url"].apply(extract_features).tolist()
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

url = input("Enter URL: ")

prediction = model.predict([extract_features(url)])

if prediction[0] == 1:
    print("⚠️ Phishing Website")
else:
    print("✅ Safe Website")