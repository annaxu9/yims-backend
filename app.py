from flask import Flask, request, jsonify
from flask_cors import CORS
from data_access_layer import CollegeDAO

app = Flask(__name__)
CORS(app)

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    college_dao = CollegeDAO()
    leaderboard = college_dao.get_leaderboard()
    print(jsonify(leaderboard))
    return leaderboard