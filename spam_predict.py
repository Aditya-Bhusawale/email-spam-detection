import pickle
import re

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    return text

def predict_spam(message):
    message = clean_text(message)
    data = vectorizer.transform([message])
    return model.predict(data)[0]
