
import firebase_admin
from firebase_admin import credentials, db
import pandas as pd

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\sahoo\OneDrive\Documents\credential.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://vivify-technocrats-default-rtdb.firebaseio.com/'
})

# Reference to the Firebase database
ref = db.reference('Users2')

# Retrieve data
data = ref.get()

# Convert data to pandas DataFrame
df = pd.DataFrame(data).transpose()

# Display the DataFrame
print("Data from Firebase:")
print(df)

# Statistical analysis
print("\nStatistical Analysis:")

# Count of unique values for each column
for col in df.columns:
    print(f"\nColumn: {col}")
    print(df[col].value_counts())
