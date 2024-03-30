from flask import Flask, request, jsonify
from flask_cors import CORS
from data_access_layer import CollegeDAO
from data_access_layer import UsersDAO

app = Flask(__name__)
CORS(app)

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    college_dao = CollegeDAO()
    leaderboard = college_dao.get_leaderboard()
    return leaderboard

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    netid = data.get('netid')
    user_dao = UsersDAO()
    print(netid)
    if netid:  # Replace this condition with your actual authentication logic
        user = user_dao.get_user(netid)
        return user
    return 'Login failed', 401

# @app.route('/api/users/<netid>')
# def get_user(netid):
#     user_data_access = UsersDataAccess(session)
#     user = user_data_access.get_user(netid)
#     if user:
#         return jsonify({
#             'netid': user.netid,
#             'firstname': user.firstname,
#             'lastname': user.lastname,
#             'college': user.college.name,  # Assuming CollegeDB has a name attribute
#             'role': user.role
#         })
#     else:
#         return jsonify({'error': 'User not found'}), 404