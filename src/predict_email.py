import joblib

# Load model + vectorizer
model = joblib.load('models/phishing_model.joblib')
vectorizer = joblib.load('models/vectorizer.joblib')

def predict_email(text):
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0]
    
    result = " PHISHING EMAIL" if pred == 1 else " SAFE EMAIL"
    confidence = prob[pred] * 100
    
    print(f"\nResult: {result}")
    print(f"Confidence: {confidence:.1f}%")
    return pred

# Test with sample emails
print("="*50)
print(" AI Phishing Email Detector - Testing")
print("="*50)

test1 = "URGENT! FREE MONEY CLICK NOW!!!"
test2 = "Meeting scheduled for Monday at 3pm"

print("\nTest 1:", test1)
predict_email(test1)

print("\n" + "-"*50)
print("\nTest 2:", test2)
predict_email(test2)

# Interactive mode
print("\n" + "="*50)
print(" Try Your Own Email:")
print("="*50)
email_text = input("\nPaste email text here: ")
predict_email(email_text)
