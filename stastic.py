import firebase_admin
import matplotlib.pyplot as plt
import pandas as pd
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\sahoo\OneDrive\Documents\credential.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://vivify-technocrats-default-rtdb.firebaseio.com/'
})

# Reference to the root of your database
ref = db.reference('/UserScores')

# Retrieve data
data = ref.get()

# Initialize lists to store correct and wrong counts
user_ids = []
correct_counts = []
wrong_counts = []

# Extract data and calculate counts
for key, value in data.items():
    user_ids.append(key)
    correct_counts.append(value.get('correctCount', 0))
    wrong_counts.append(value.get('wrongCount', 0))

# Create DataFrame
df = pd.DataFrame({'userId': user_ids, 'correctCount': correct_counts, 'wrongCount': wrong_counts})

# Plotting
plt.figure(figsize=(10, 5))
plt.bar(df['userId'], df['correctCount'], label='Correct Count')
plt.bar(df['userId'], df['wrongCount'], bottom=df['correctCount'], label='Wrong Count')
plt.xlabel('User ID')
plt.ylabel('Count')
plt.title('Correct and Wrong Counts by User')
plt.legend()
plt.show()
