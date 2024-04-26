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
        return jsonify({'error': str(e)}), 500
    
@app.route('/score', methods=['GET'])
def score():
    try:
        college_name = request.args.get('college')
        college = College.get_college_by_name(college_name, college_dao)
        if not college:
            return jsonify({'error': 'College not found'}), 404
        return jsonify(college.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/login", methods=["POST"])
def login():
    """
    CAS Authentication for login
    """
    output = None 
    try:
        cas_client = cas.CASClient(
            version=2,
            service_url='http://127.0.0.1:5000/',
            server_url='https://secure.its.yale.edu/cas/'
        )

        data = request.get_json()
        user, _, _ = cas_client.verify_ticket(data['ticket'])
        response = {
            "username": user,
        }
        output = json.dumps(response)
    except Exception as ex:
        print(ex)
        return jsonify(error=404, text=str(ex)), 404
    return output, 200

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     netid = data.get('netid')

#     if netid:
#         user = User.get_user(netid, user_dao)
#         if user:
#             return jsonify(user.to_dict())
#     return jsonify({'message': 'Login failed'}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    user = User.add_user(user_dao, **data)
    if user:
        return jsonify(user.to_dict()), 201
    else:
        return jsonify({'message': 'Unable to create user'}), 400


@app.route('/sports', methods=['GET'])
def get_sports():
    sports = Sport.get_all_sports(sport_dao)
    return jsonify([sport.to_dict() for sport in sports])

@app.route('/add_match', methods=['POST'])
def add_match():
    data = request.json
    print(data)
    is_added = Match.add_match(match_dao, **data)

    if is_added:
        return jsonify({'message': 'Match added successfully'}), 201
    else:
        return jsonify({'message': 'Unable to add match'}), 400

@app.route('/validate_matches', methods=['POST'])
def validate_matches():
    matches = request.json
    invalid_matches = []

    print(matches)

    for i, match_data in enumerate(matches):
        match = Match(**match_data, college_dao=college_dao, sport_dao=sport_dao, user_dao=user_dao)

        # Check availability for the first college
        is_available_1, message_1 = match_dao.is_college_available(match.colleges[0], match.date, match.start_time, match.location)
        if not is_available_1:
            invalid_matches.append({'index': i, 'message': message_1})
            continue  # Skip checking the second college if the first one is already unavailable

        # Check availability for the second college
        is_available_2, message_2 = match_dao.is_college_available(match.colleges[1], match.date, match.start_time, match.location)
        if not is_available_2:
            invalid_matches.append({'index': i, 'message': message_2})

    return jsonify(invalid_matches)


@app.route('/matches', methods=['GET'])
def get_matches():
    college_name = request.args.get('college')
    sport_name = request.args.get('sport')
    college = College.get_college_by_name(college_name, college_dao) if college_name else None
    sport = Sport.get_sport_by_name(sport_name, sport_dao) if sport_name else None
    matches = Match.get_filtered_matches(match_dao, college=college, sport=sport)
    return jsonify([match.to_dict() for match in matches])

@app.route('/past-unscored-matches', methods=['GET'])
def get_past_unscored_matches():
    matches = Match.get_past_unscored_matches(match_dao)
    return jsonify([match.to_dict() for match in matches])

@app.route('/update-match/<int:match_id>', methods=['POST'])
def update_match(match_id):
    data = request.json
    match = MatchDAO.update_match(match_id, data.get('college_pts1'), data.get('college_pts2'))
    if not match:
        return jsonify({'error': 'Match not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
