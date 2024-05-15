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
ref = db.reference('Users2')

# Retrieve data
data = ref.get()

# Convert data to pandas DataFrame
df = pd.DataFrame(data).transpose()

# Convert columns to numeric if possible
df = df.apply(pd.to_numeric, errors='coerce')

# Statistical analysis and visualization
for col in df.columns:
    # Skip non-numeric columns
    if pd.api.types.is_numeric_dtype(df[col]):
        # Calculate fluctuation in values
        fluctuation = df[col].diff()

        # Plotting
        plt.figure(figsize=(8, 6))
        fluctuation.plot(color='skyblue', marker='o', linestyle='-')
        plt.title(f'Fluctuation of {col}')
        plt.xlabel('Index')
        plt.ylabel('Fluctuation')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
