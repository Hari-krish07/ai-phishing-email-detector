import pandas as pd

# Load cleaned data
df = pd.read_csv('data/cleaned_phishing.csv')

print("Data loaded:")
print(df.shape)
print(df.head())

# Encode Email Type: Safe=0, Phishing=1
df['Label'] = df['Email Type'].map({'Safe Email': 0, 'Phishing Email': 1})

print("\nLabel encoding:")
print(df[['Email Type', 'Label']].head())
print(f"\nSafe: {(df['Label']==0).sum()}, Phishing: {(df['Label']==1).sum()}")

df['Clean Text'] = df['Clean Text'].fillna('')
df = df.dropna(subset=['Clean Text'])
print(f"After cleaning NaN: {len(df)} emails")

# Step 3: TF-IDF (Convert Clean Text → numbers)
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X = vectorizer.fit_transform(df['Clean Text'])
y = df['Label']

print(f"\nTF-IDF shape: {X.shape}")
print("Features ready!")

# Step 4: Train/Test split (80/20)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"\nTrain: {X_train.shape[0]} emails, Test: {X_test.shape[0]} emails")
print(f"Train balance: Safe={(y_train==0).sum()}, Phishing={(y_train==1).sum()}")

# Step 6: SAVE the cleaned file for futurte modification (model training)
import joblib
joblib.dump(vectorizer, 'models/vectorizer.joblib')
joblib.dump(X_train, 'models/X_train.joblib')
joblib.dump(X_test, 'models/X_test.joblib')
joblib.dump(y_train, 'models/y_train.joblib')
joblib.dump(y_test, 'models/y_test.joblib')

print("\n Files saved:")
print("- models/vectorizer.joblib (word converter)")
print("- models/X_train.joblib (14K training emails)")
print("- models/X_test.joblib (3K test emails)")

