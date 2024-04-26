# YIMS Endpoints 

This document outlines the details of the API endpoints provided by the YIMS API.

## Table of Contents
- [Leaderboard](#leaderboard)
- [College](#college)
- [Login](#login)
- [Signup](#signup)
- [Special Users](#special-users)
- [Edit User](#edit-user)
- [Add User Points](#add-user-points)
- [Matches](#matches)
- [Validate Match](#validate-match)
- [Add Match](#add-match)
- [Update Match](#update-match)
- [Sign Up For Match](#signup-for-match)
- [Match Info](#match-info)

## Endpoint Details

### Leaderboard
- **URL**: `/leaderboard`
- **Method**: `GET`
- **Description**: Retrieves a list of colleges sorted by score points.
- **Parameters**: None
- **Headers**: None
- **Response**:
  - **200 OK**: 
    ```json
    [
      {
        "id": "1", 
        "name": "Benjamin Franklin",
        "abbreviation": "BF", 
        "points": 99,
        "matches": []
      } 
       // all the other colleges as well in descending point order
    ]
    ```
  - **500 Internal Server Error**: 
    ```json
    {
        "status": "error",
        "message": "Internal Service Error"
    }
    ```

### College
- **URL**: `/college`
- **Method**: `GET`
- **Description**: Retrieves detailed information about a specific college. This endpoint requires the client to specify the name of the college to retrieve its data.
- **Query Parameters**:
  - `college_name` (string, required): The name of the college to retrieve information for. This parameter is mandatory and must exactly match the college's name in the database.
- **Headers**: None
- **Responses**:
  - **200 OK**: Successfully retrieves the college data.
    ```json
    {
      "id": "1", 
      "name": "Benjamin Franklin",
      "abbreviation": "BF", 
      "points": 99,
      "matches": []
    }
    ```
  - **400 Bad Request**: Returned if the `college_name` parameter is missing or the query parameters are malformed.
    ```json
    {
      "status": "error",
      "message": "Bad Request: Required parameter 'college_name' is missing from the request."
    }
    ```
  - **404 Not Found**: Returned if no college matches the provided `college_name`.
    ```json
    {
      "status": "error",
      "message": "Not Found: College not found"
    }
    ```
  - **500 Internal Server Error**: 
    ```json
    {
        "status": "error",
        "message": "Internal Service Error"
    }
    ```


### Login
- **URL**: `/login`
- **Method**: `POST`
- **Description**: Authenticates users via CAS.
- **Body**:
  - `ticket` (string): CAS ticket for authentication.
- **Headers**: 
  - `Content-Type`: `application/json`
- **Response**:
  - **200 OK**:
    ```json
    {"username": "johndoe"}
    ```
  - **404 Not Found**: 
    ```json
    {
      "error": "Not Found",
      "message": "User not found"
    }    
    ```
  - **500 Internal Server Error**: 
    ```json
    {"error": "Internal Service Error"}
    ```

### Signup
- **URL**: `/signup`
- **Method**: `POST`
- **Description**: Create account for new user and adds it to the database. 

### Special Users 
- **URL**: `/special-users`
- **Method**: `GET`
- **Description**: Retrieves all users with a special role (ref, sec, president, admin)
- **Parameters**: 
    - `college_name` (string, optional): Name of the college 
    - `role` (string, optional): Name(s) of role
- **Headers**: None
- **Response**:
  - **200 OK**: 
    ```json
    [
        {
        "netid": "awx2",
        "firstname": "Anna",
        "lastname": "Xu",
        "college": "Benjamin Franklin",
        "role": "sec",
        "points": 99,
        "matches": []
        }, // other special roles 
    ]
    ```
  - **500 Internal Server Error**: 
    ```json
    {
        "status": "error",
        "message": "Internal Service Error"
    }
    ```

### Edit User 
- **URL**: `/edit-user`
- **Method**: `PUT`
- **Description**: Updates the signed-in user's information. This endpoint is designed to replace the user's existing details with the new data provided in the request.
- **Parameters**: None
- **Headers**: 
  - `Content-Type`: `application/json`
- **Body**: 
  - `netid` (string, required): The NetID of the user.
  - `firstname` (string, optional): New first name of the user.
  - `lastname` (string, optional): New last name of the user.
  - `college` (string, optional): New college of the user.
  - `role` (string, optional): New role of the user.
  - `points` (int, optional): Updated points of the user.
- **Response**:
  - **200 OK**: Successfully updated the user's information. Returns the updated user data.
    ```json
    {
      "netid": "awx2",
      "firstname": "Anna",
      "lastname": "Xu",
      "college": "Benjamin Franklin",
      "role": "sec",
      "points": 99,
    }
    ```
  - **400 Bad Request**: Returned if required fields are missing or the format is incorrect.
    ```json
    {
        "status": "error",
        "message": "Bad Request: Required field 'netid' missing"
    }
    ```
  - **404 Not Found**: Returned if no user matches the provided NetID.
    ```json
    {
        "status": "error",
        "message": "User not found"
    }
    ```
  - **500 Internal Server Error**: 
    ```json
    {
        "status": "error",
        "message": "Internal Service Error"
    }
    ```

### Add User Points
- **URL**: `/add-user-points`
- **Method**: `POST`
- **Description**: Updates the signed-in user's information. This endpoint is designed to replace the user's existing details with the new data provided in the request.
- **Parameters**: None
- **Headers**: 
  - `Content-Type`: `application/json`
- **Body**: 
  - `netid` (string, required): The NetID of the user.
  - `firstname` (string, optional): New first name of the user.
  - `lastname` (string, optional): New last name of the user.
  - `college` (string, optional): New college of the user.
  - `role` (string, optional): New role of the user.
  - `points` (int, optional): Updated points of the user.
- **Response**:
  - **200 OK**: Successfully updated the user's information. Returns the updated user data.
    ```json
    {
      "netid": "awx2",
      "firstname": "Anna",
      "lastname": "Xu",
      "college": "Benjamin Franklin",
      "role": "sec",
      "points": 99,
    }
    ```
  - **400 Bad Request**: Returned if required fields are missing or the format is incorrect.
    ```json
    {
        "status": "error",
        "message": "Bad Request: Required field 'netid' missing"
    }
    ```
  - **404 Not Found**: Returned if no user matches the provided NetID.
    ```json
    {
        "status": "error",
        "message": "User not found"
    }
    ```
  - **500 Internal Server Error**: 
    ```json
    {
        "status": "error",
        "message": "Internal Service Error"
    }
    ```

### Matches 
- **URL**: `/matches`
- **Method**: `GET`
- **Description**: Retrieves match information based on various optional filtering parameters. Clients can combine filters as needed to narrow down the results.
- **Parameters**: 
    - `college`: String (optional): Filter matches by the associated college.
    - `sport`: String (optional): Filter matches by the sport type.
    - `netid`: String (optional): Filter matches by user involvement (e.g., referee, player).
    - `past`: Boolean (optional): Filter matches that have already occurred.
    - `unscored`: Boolean (optional): Further filter past matches to return only those that have not yet been scored. This parameter should logically be used in conjunction with past.
- **Headers**: None
- **Response**:
  - **200 OK**: 
    ```json
    [
        {
        "id": 1,
        "college1": "Benjamin Franklin",
        "college2": "Berkely",
        "sport": "Basketball",
        "location": "Lanman Center",
        "date": "04/25/2024",
        "start_time": "8:00PM",
        "college1_pts": 0,
        "college2_pts": 0,
        "ref": "",
        }, // other matches 
    ]
    ```
  - **500 Internal Server Error**: 
    ```json
    {"error": "Internal Service Error"}
    ```

### Validate Match
- **URL**: `/validate-match`
- **Method**: `GET`
- **Description**: Validates a proposed match to ensure that there are no scheduling conflicts between the colleges, and the location is available.
- **Parameters**: 
    - `college1`: String (required) - Name of the first college participating.
    - `college2`: String (required) - Name of the second college participating.
    - `date`: String (required) - Date of the match in YYYY-MM-DD format.
    - `start_time`: String (required) - Time of the match in HH:MM format.
    - `location`: String (required) - Venue where the match is to be held.
- **Headers**: None
- **Response**
    - **200 OK**:
    ```json
        {
            "valid": false, 
            "message": "Location is already taken"
        }
    ```
    - **400 Bad Request**:
    ```json
        {
            "error": "Bad Request", 
            "message": "Missing Parameters"
        }
    ```
    - **500 Internal Service Error**:
    ```json
        {
            "error": "Internal Service Error"
        }
    ```

### Add Match
- **URL**: `/add-match`
- **Method**: `POST`
- **Description**: Add a new match while checking that it's a valid match (will throw an error if invalid)
- **Headers**: None
- **Body**: 
    - `college1`: String (required) - Name of the first college participating.
    - `college2`: String (required) - Name of the second college participating.
    - `sport`: String (required) - Sport of Match
    - `date`: String (required) - Date of the match in YYYY-MM-DD format.
    - `start_time`: String (required) - Time of the match in HH:MM format.
    - `location`: String (required) - Venue where the match is to be held.
- **Response**: 
    - **200 OK**
    ```json
    {
        "status": "success",
        "message": "Match added successfully.",
        "match": {
            "id": 123,
            "college1": "Name of the first college",
            "college2": "Name of the second college",
            "sport": "Sport of Match",
            "date": "YYYY-MM-DD",
            "start_time": "HH:MM",
            "location": "Venue where the match is to be held"
        }
    }
    ```
    - **400 Bad Request**
    ```json
    {
        "error": "Bad Request",
        "message": "Validation failed: [specific reason, e.g., 'The location is already booked at the specified time.']"
    }
    ```
    - **500 Internal Service Error**
    ```json
    {
        "error": "Internal Service Error"
    }
    ```


### Update Match
- **URL**: `/update-match`
- **Method**: `POST`
- **Description**: Updates the score of a specific match and recalculates the points for the associated colleges and participants. This endpoint also supports corrections to previously recorded scores.
- **Headers**: 
    - `Content-Type`: `application/json`
- **Body**: 
    - `match_id` (integer, required): Unique identifier of the match to be updated
    - `score1` (integer, required): The outcome of the first college
    - `score2` (integer, required): The outcome of the second college
    - `correction` (boolean, optional): Indicates whether this submission is correcting a previous score. Defaults to `false`. 
    - `netid` (string, required): 
- **Response**:
    - **200 OK**:
    ```json
    {
        "status": "success",
        "message": "Match updated successfully and points recalculated."
    }
    ```
    - **400 Bad Request**
    ```json
    {
    "error": "Bad Request",
    "message": "Invalid input. Please check the match_id and scores provided."
    }
    ```
    -**404 Not Found**
    ```json
    {
    "error": "Not Found",
    "message": "Match not found with provided ID."
    }
    ```
    - **500 Internal Server Error**: 
    ```json
    {"error": "Internal Service Error"}
    ```

### Sign Up For Match 
- **URL**: `/signup-for-match`
- **Method**: `POST`
- **Description**: Allows a user to sign up for a specific match. This endpoint adds the user to the match roster, checking if the match exists and if the user is eligible to participate.
- **Headers**:None
- **Body**:
    - `netid` (String, required): user's netid
    - `matchid` (Integer, required): match id
- **Response**: 
    - **200 OK**
    ```json
    {
        "status": "success",
        "message": "You have successfully signed up for the match."
    }
    ```
    - **400 Bad Request**
    ```json
    {
        "status": "error",
        "message": "Bad Request: Invalid input: Please check the NetID or Match ID."
    }
    ```
    - **404 Not Found**
    ```json
    {
        "status": "error",
        "message": "Not Found: Match not found or user not found."
    }
    ```
    - **500 Internal Service Error**
    ```json
    {
        "status": "error",
        "message": "Internal Service Error"
    }
    ```

### Match Info 
- **URL**: `/match-info`
- **Method**: `GET`
- **Description**: Allows users to get the info of the match
- **Parameters**:
    - `matchid`: (Integer, required): match id
- **Headers**: None
- **Response**: 
    - **200 OK**
    ```json
    {
        "id": 1,
        "college1": "Benjamin Franklin",
        "college2": "Berkely",
        "sport": "Basketball",
        "location": "Lanman Center",
        "date": "04/25/2024",
        "start_time": "8:00PM",
        "college1_pts": 0,
        "college2_pts": 0,
        "ref": "",
    }
    ```
    - **404 Not Found**
    ```json
    {
        "status": "error",
        "message": "Match not found",
    }
    ```
    - **500 Internal Service Error**
    ```json
    {
        "status": "error",
        "message": "Internal Service Error"
    }
    ```





