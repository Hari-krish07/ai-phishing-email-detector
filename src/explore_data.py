import pandas as pd

# Load dataset
df = pd.read_csv('data/Phishing_Email.csv')

# Basic info
print("Dataset shape:", df.shape)
print("\nColumn names:", df.columns)
print("\nFirst 5 rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nNull values:")
print(df.isnull().sum())
print("\nDuplicate rows:")
print(df.duplicated().sum())
# Drop useless column + missing rows
df = df.drop(columns=['Unnamed: 0'])
df = df.dropna(subset=['Email Text'])

print("After cleaning:", df.shape)  # Expect: (18634, 2)

# Basic text cleaning
df['Email Text'] = df['Email Text'].astype(str).str.lower().str.strip()
import re
df['Email Text'] = df['Email Text'].apply(lambda x: re.sub(r'[^\w\s]', ' ', x))
df = df.drop_duplicates(subset=['Email Text'])

print("Sample cleaned:")
print(df[['Email Text', 'Email Type']].head())
print("\nAfter cleaning info:")
print("Shape:", df.shape)
print("Columns:", df.columns)
print("Null values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
