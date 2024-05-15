import firebase_admin
from firebase_admin import credentials, db
import pandas as pd
import matplotlib.pyplot as plt

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\sahoo\OneDrive\Documents\credential.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://vivify-technocrats-default-rtdb.firebaseio.com/'
})

# Reference to the root of your database
ref = db.reference('/Users2')

# Retrieve data
data = ref.get()

# Convert data to DataFrame
df = pd.DataFrame.from_dict(data, orient='index')

# Statistical Analysis
# For example, let's count the occurrences of 'helmet' and 'shoe'
helmet_counts = df['helmet'].value_counts()
shoe_counts = df['shoe'].value_counts()

# Plotting
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Plot for helmet counts
axes[0].bar(helmet_counts.index.astype(str), helmet_counts.values)
axes[0].set_title('Helmet Counts')
axes[0].set_ylabel('Count')

# Plot for shoe counts
axes[1].bar(shoe_counts.index.astype(str), shoe_counts.values)
axes[1].set_title('Shoe Counts')
axes[1].set_ylabel('Count')

plt.tight_layout()
plt.show()
