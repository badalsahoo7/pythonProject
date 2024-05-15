import firebase_admin
from firebase_admin import credentials, db
import pandas as pd
import matplotlib.pyplot as plt

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\sahoo\OneDrive\Documents\credential.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://vivify-technocrats-default-rtdb.firebaseio.com/'
})

# Reference to the Firebase database
ref = db.reference('UserScores')

# Retrieve data
data = ref.get()

# Convert data to pandas DataFrame
df = pd.DataFrame(data).transpose()

# Statistical analysis
print("Statistical Analysis:")

# Count of unique values for each column
for col in df.columns:
    print(f"\nColumn: {col}")
    print(df[col].value_counts())
    # Plot pie chart
    plt.figure(figsize=(6, 6))
    df[col].value_counts().plot.pie(autopct='%1.1f%%', startangle=140)
    plt.title(f'Distribution of {col}')
    plt.ylabel('')
    plt.show()
