import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

# Download NLTK stopwords (first time only)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Load dataset
df = pd.read_csv('data/Phishing_Email.csv')

# Drop unused column and null rows
df = df.drop(columns=['Unnamed: 0'])
df = df.dropna(subset=['Email Text'])

# Lowercase & strip extra spaces
df['Email Text'] = df['Email Text'].astype(str).str.lower().str.strip()

# Remove special characters
df['Email Text'] = df['Email Text'].apply(lambda x: re.sub(r'[^\w\s]', ' ', x))

print("Sample cleaned emails:")
print(df.head())

# Define preprocessing function
def preprocess_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    return ' '.join([w for w in tokens if w.isalpha() and w not in stop_words])

# Apply preprocessing
df['Clean Text'] = df['Email Text'].apply(preprocess_text)

# Save cleaned dataset
df[['Email Text', 'Clean Text', 'Email Type']].to_csv('data/cleaned_phishing.csv', index=False)

# Show before/after comparison
print("Before stopwords:", df['Email Text'].iloc[0][:100])
print("After stopwords:", df['Clean Text'].iloc[0][:100])
print("\n Saved to cleaned_phishing.csv")
print("Final shape:", df.shape)

