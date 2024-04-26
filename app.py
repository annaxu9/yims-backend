from flask import Flask, request, jsonify
from flask_cors import CORS
import cas
import json
from business.College import College
from business.User import User
from business.Sport import Sport
from business.Match import Match
from data_access.CollegeDataAccess import CollegeDAO
from data_access.UsersDataAccess import UsersDAO
from data_access.SportsDataAccess import SportsDAO
from data_access.MatchesDataAccess import MatchDAO
from utils import get_college_id

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

# Instantiate DAOs
college_dao = CollegeDAO()
user_dao = UsersDAO()
sport_dao = SportsDAO()
match_dao = MatchDAO()

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    try:
        leaderboard = College.get_leaderboard(college_dao)
        return jsonify([college.to_dict() for college in leaderboard])
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/score', methods=['GET'])
def score():
    try:
        college_name = request.args.get('college')
        college = College.get_college_by_name(college_name, college_dao)
        if not college:
            return jsonify({"status": "error", "message": "College not found"}), 404
        return jsonify(college.to_dict())
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/login", methods=["POST"])
def login():
    try:
        cas_client = cas.CASClient(
            version=2,
            service_url='http://127.0.0.1:5000/',
            server_url='https://secure.its.yale.edu/cas/'
        )
        data = request.get_json()
        user, _, _ = cas_client.verify_ticket(data['ticket'])
        return jsonify({"status": "success", "username": user}), 200
    except Exception as ex:
        return jsonify({"status": "error", "message": str(ex)}), 404

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    user = User.add_user(user_dao, **data)
    if user:
        return jsonify(user.to_dict()), 201
    else:
        return jsonify({"status": "error", "message": "Unable to create user"}), 400

@app.route('/edit-user', methods=['PUT'])
def edit_user():
    data = request.get_json()
    if not data or 'netid' not in data:
        return jsonify({"status": "error", "message": "Bad Request: Required field 'netid' missing"}), 400

    try:
        # Assume a function updateUser() that updates user details and returns the updated user
        updated_user = user_dao.update_user(**data)
        if not updated_user:
            return jsonify({"status": "error", "message": "User not found"}), 404
        return jsonify(updated_user), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/add-user-points', methods=['POST'])
def add_user_points():
    data = request.get_json()
    if not data or 'netid' not in data or 'points' not in data:
        return jsonify({"status": "error", "message": "Bad Request: Required fields 'netid' or 'points' missing"}), 400

    try:
        # Assuming addUserPoints() adds points to the user and returns the updated user info
        updated_user = user_dao.add_user_points(data['netid'], data['points'])
        if not updated_user:
            return jsonify({"status": "error", "message": "User not found"}), 404
        return jsonify(updated_user), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/add_match', methods=['POST'])
def add_match():
    data = request.json
    try:
        is_added = Match.add_match(match_dao, **data)
        if is_added:
            return jsonify({"status": "success", "message": "Match added successfully"}), 201
        else:
            return jsonify({"status": "error", "message": "Unable to add match"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/validate_matches', methods=['POST'])
def validate_matches():
    matches = request.json
    invalid_matches = []
    try:
        for i, match_data in enumerate(matches):
            match = Match(**match_data, college_dao=college_dao, sport_dao=sport_dao, user_dao=user_dao)
            is_available_1, message_1 = match_dao.is_college_available(match.colleges[0], match.date, match.start_time, match.location)
            if not is_available_1:
                invalid_matches.append({'index': i, 'message': message_1})
                continue
            is_available_2, message_2 = match_dao.is_college_available(match.colleges[1], match.date, match.start_time, match.location)
            if not is_available_2:
                invalid_matches.append({'index': i, 'message': message_2})
        return jsonify(invalid_matches)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/matches', methods=['GET'])
def get_matches():
    try:
        college_name = request.args.get('college')
        sport_name = request.args.get('sport')
        college = College.get_college_by_name(college_name, college_dao) if college_name else None
        sport = Sport.get_sport_by_name(sport_name, sport_dao) if sport_name else None
        matches = Match.get_filtered_matches(match_dao, college=college, sport=sport)
        return jsonify([match.to_dict() for match in matches])
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/update-match/<int:match_id>', methods=['POST'])
def update_match(match_id):
    data = request.json
    try:
        match = MatchDAO.update_match(match_id, data.get('college_pts1'), data.get('college_pts2'))
        if match:
            return jsonify({"status": "success", "message": "Match updated successfully"}), 200
        else:
            return jsonify({"status": "error", "message": "Match not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
