# import firebase_admin
# from firebase_admin import credentials, db
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Initialize Firebase Admin SDK
# cred = credentials.Certificate(r"C:\Users\sahoo\OneDrive\Documents\credential.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://vivify-technocrats-default-rtdb.firebaseio.com/'
# })
#
# # Reference to the Firebase database
# ref = db.reference('Question')
#
# # Retrieve data
# data = ref.get()
#
# # Convert data to pandas DataFrame
# df = pd.DataFrame(data).transpose()
#
# # Statistical analysis and visualization
# for col in df.columns:
#     # Count unique values for the column
#     value_counts = df[col].value_counts()
#
#     # Plotting
#     plt.figure(figsize=(8, 6))
#     value_counts.plot(kind='bar', color='skyblue')
#     plt.title(f'Distribution of {col}')
#     plt.xlabel(col)
#     plt.ylabel('Count')
#     plt.xticks(rotation=45, ha='right')
#     plt.tight_layout()
#     plt.show()
