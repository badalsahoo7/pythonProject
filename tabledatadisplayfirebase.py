# from flask import Flask, jsonify
# import firebase_admin
# from firebase_admin import credentials, db
#
# app = Flask(__name__)
#
# # Initialize Firebase Admin SDK
# cred = credentials.Certificate(r"C:\Users\sahoo\OneDrive\Documents\credential.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://vivify-technocrats-default-rtdb.firebaseio.com/'
# })
#
# # Reference to the Firebase database
# ref = db.reference('Users2')
#
# # Retrieve data
# data = ref.get()
#
#
# @app.route('/')
# def index():
#     return open('C:\\realtime data in table format\\index2.html').read()
#
#
# @app.route('/data')
# def get_data():
#     return jsonify(list(data.values()))
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
