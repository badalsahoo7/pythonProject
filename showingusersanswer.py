import firebase_admin
from firebase_admin import credentials, db
import pandas as pd

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\sahoo\OneDrive\Documents\credential.json")  # Path to your service account key JSON file
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://vivify-technocrats-default-rtdb.firebaseio.com/'
})

# Reference to the Firebase database
ref = db.reference()

# Fetch data from Firebase
data = {
    "Questions": {
        "Question1": {
            "Question": "Who is founder of tesla car ?",
            "ans": "Elon musk",
            "qA": "Elon musk",
            "qB": "Jeff Bejos",
            "qC": "Steve Jobs",
            "qD": "Mark Zukerberg"
        },
        "Question2": {
            "Question": "Who is CEO of Google",
            "ans": "Sundar Pichai",
            "qA": "Sundar Pichai",
            "qB": "Elon Musk",
            "qC": "Jeff Bejos",
            "qD": "Mark Zukerberg"
        }
    },
    "UserScores": {
        "6yvOF9y5cdQTpMrzmHt2G7kALQI2": {
            "-NvVEt1ZN2RgdiRssYpa": {
                "correctCount": 2,
                "userId": "6yvOF9y5cdQTpMrzmHt2G7kALQI2",
                "wrongCount": 0
            },
            "-NvVJdv7GfmzQpQHe4p5": {
                "correctCount": 2,
                "userId": "6yvOF9y5cdQTpMrzmHt2G7kALQI2",
                "wrongCount": 0
            }
        }
    }
}

# Flatten the data
questions_data = []
for _, question_data in data["Questions"].items():
    questions_data.append(question_data)

user_scores_data = []
for _, user_data in data["UserScores"].items():
    for _, score_data in user_data.items():
        user_scores_data.append(score_data)

# Create DataFrames
questions_df = pd.DataFrame(questions_data)
user_scores_df = pd.DataFrame(user_scores_data)

# Display the DataFrames
print("Questions Data:")
print(questions_df)

print("\nUser Scores Data:")
print(user_scores_df)
