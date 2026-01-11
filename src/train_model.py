import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

print("Loading Day 5 files...")
vectorizer = joblib.load('models/vectorizer.joblib')
X_train = joblib.load('models/X_train.joblib')
X_test = joblib.load('models/X_test.joblib')
y_train = joblib.load('models/y_train.joblib')
y_test = joblib.load('models/y_test.joblib')

print(f"Train: {X_train.shape[0]} emails, Test: {X_test.shape[0]} emails")

# Step 1: Train Logistic Regression
print("\nTraining Logistic Regression...")
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Step 2: Test accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\n Model Accuracy: {accuracy*100:.2f}%")
print("\nDetailed Report:")
print(classification_report(y_test, y_pred, target_names=['Safe', 'Phishing']))

# Step 3: Save model
joblib.dump(model, 'models/phishing_model.joblib')
print("\n Model saved: models/phishing_model.joblib")


#importing Naive bayes(importing a pre-built ML algorithm (Naive Bayes) from scikit-learn) to compare my ai model 
from sklearn.naive_bayes import MultinomialNB

print("\nTraining Naive Bayes...")

nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)

# Predict
nb_pred = nb_model.predict(X_test)

# Evaluate
from sklearn.metrics import accuracy_score, classification_report
nb_accuracy = accuracy_score(y_test, nb_pred)

print(f"\n Naive Bayes Accuracy: {nb_accuracy*100:.2f}%")
print("\nNaive Bayes Report:")
print(classification_report(y_test, nb_pred, target_names=['Safe', 'Phishing']))


# Model Comparison & Final Decision
print("\n" + "="*50)
print("MODEL COMPARISON:")
print(f"Logistic Regression: {accuracy*100:.2f}%")
print(f"Naive Bayes: {nb_accuracy*100:.2f}%")
print("\n FINAL MODEL: Logistic Regression")
print("Reason: Higher accuracy (96.24%) and better phishing recall (97%)")
print("="*50)

