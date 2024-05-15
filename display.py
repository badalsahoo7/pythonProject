import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd

# Initialize Firebase app with your service account credentials
cred = credentials.Certificate(r"C:\Users\sahoo\OneDrive\Documents\credential.json")
firebase_admin.initialize_app(cred, {
       'databaseURL': 'https://vivify-technocrats-default-rtdb.firebaseio.com/'
})

# Reference to your Firebase Realtime Database
ref = db.reference('Users2')

# Fetch data from Firebase Realtime Database
data = ref.get()

# Convert the data to a pandas DataFrame for tabular representation
df = pd.DataFrame.from_dict(data, orient='index')

# Display the DataFrame
print(df)
