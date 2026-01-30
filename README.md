#  Email Spam Detection Web App

This project is a machine learning–based web application that detects whether an email message is **Spam** or **Not Spam (Ham)**.  
The application uses **TF-IDF vectorization** with **Logistic Regression** and is deployed using **Streamlit**.

---

## 🚀 Features
- Detects spam emails in real time
- Simple and user-friendly web interface
- Machine learning model trained offline
- Fast and accurate predictions
- Deployed as a web application

---

## 🧠 Model Used
- **TF-IDF Vectorizer** for text feature extraction
- **Logistic Regression** for classification

This combination provides better accuracy and stability compared to basic models.

---

## 🛠️ Tech Stack
- Python
- scikit-learn
- pandas
- Streamlit
- Pickle (for model saving)

---

## 📂 Project Structure
Email_spam/
│
├── app.py # Streamlit web app
├── spam_predict.py # Prediction logic
├── model.pkl # Trained ML model
├── vectorizer.pkl # TF-IDF vectorizer
├── requirements.txt # Required libraries


---

## ▶️ How to Run Locally

### 1️⃣ Install Dependencies
```bash
python -m pip install -r requirements.txt

