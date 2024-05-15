from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\sahoo\OneDrive\Documents\credential.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://vivify-technocrats-default-rtdb.firebaseio.com/'
})

# Reference to the Firebase databases
ref_users = db.reference('Users2')
ref_other = db.reference('UserScores')
ref_question = db.reference('Question')  # Reference to the 'Question' node

# Retrieve data
data_users = ref_users.get()
data_other = ref_other.get()
data_question = ref_question.get()  # Fetch data from the 'Question' reference

# Function to extract relevant fields from nested objects in UserScores
def extract_user_scores_data(user_scores_data):
    extracted_data = []
    for user_id, user_data in user_scores_data.items():
        for session_id, session_data in user_data.items():
            extracted_data.append({
                'userId': user_id,
                'sessionId': session_id,
                'correctCount': session_data.get('correctCount', 0),
                'wrongCount': session_data.get('wrongCount', 0)
            })
    return extracted_data

@app.route('/')
def index():
    return open('index2.html').read()

@app.route('/data')
def get_data():
    return jsonify(list(data_users.values()))

@app.route('/data_other')
def get_data_other():
    return jsonify(list(data_other.values()))

@app.route('/data_question')  # Endpoint for the 'Question' reference
def get_data_question():
    return jsonify(data_question)

@app.route('/data_user_scores')  # Endpoint for the 'UserScores' reference
def get_data_user_scores():
    extracted_data = extract_user_scores_data(data_other)
    return jsonify(extracted_data)

# if __name__ == '__main__':
#     app.run(debug=True)
