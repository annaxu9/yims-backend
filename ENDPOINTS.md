# YIMS Endpoints 

This document outlines the details of the API endpoints provided by the YIMS API.

## Table of Contents
- [Leaderboard](#leaderboard)
- [College](#college)
- [Login](#login)
- [Signup](#signup)
- [IM President](#im-president)
- [IM Secretaries](#im-secretaries)
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
    {"error": "Internal Service Error"}
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
      "error": "Bad Request",
      "message": "Required parameter 'college_name' is missing from the request."
    }
    ```
  - **404 Not Found**: Returned if no college matches the provided `college_name`.
    ```json
    {
      "error": "Not Found",
      "message": "College not found"
    }
    ```
  - **500 Internal Server Error**: 
    ```json
    {"error": "Internal Service Error"}
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

### IM President 
- **URL**: `/im-president`
- **Method**: `GET`
- **Description**: Retrieves the IM President
- **Parameters**: None 
- **Headers**: None
- **Response**:
  - **200 OK**: 
    ```json
    {
    "netid": "awx2",
    "firstname": "Anna",
    "lastname": "Xu",
    "college": "Benjamin Franklin",
    "role": "president",
    "points": 99,
    } 
    ```
  - **500 Internal Server Error**: 
    ```json
    {"error": "Internal Service Error"}
    ```

### IM Secretaries 
- **URL**: `/im-secretaries`
- **Method**: `GET`
- **Description**: Retrieves all IM Secretaries
- **Parameters**: 
    - `college_name` (string, optional): Name of the college 
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
        }, // other im secretaries 
    ]
    ```
  - **500 Internal Server Error**: 
    ```json
    {"error": "Internal Service Error"}
    ```

### Special Users 
- **URL**: `/all-special-users`
- **Method**: `GET`
- **Description**: Retrieves all users with a special role (ref, sec, president, admin)
- **Parameters**: 
    - `college_name` (string, optional): Name of the college 
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
    {"error": "Internal Service Error"}
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
    {"error": "Bad Request: Required field 'netid' missing"}
    ```
  - **404 Not Found**: Returned if no user matches the provided NetID.
    ```json
    {"error": "User not found"}
    ```
  - **500 Internal Server Error**: 
    ```json
    {"error": "Internal Service Error"}
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
    {"error": "Bad Request: Required field 'netid' missing"}
    ```
  - **404 Not Found**: Returned if no user matches the provided NetID.
    ```json
    {"error": "User not found"}
    ```
  - **500 Internal Server Error**: 
    ```json
    {"error": "Internal Service Error"}
    ```

### Matches 
- **URL**: `/matches`
- **Method**: `GET`
- **Description**: Retrieves match information based on various optional filtering parameters. Clients can combine filters as needed to narrow down the results.
- **Parameters**: 
    - `college`: String (optional) - Filter matches by the associated college.
    - `sport`: String (optional) - Filter matches by the sport type.
    - `netid`: String (optional) - Filter matches by user involvement (e.g., referee, player).
    - `past`: Boolean (optional) - Filter matches that have already occurred.
    - `unscored`: Boolean (optional) - Further filter past matches to return only those that have not yet been scored. This parameter should logically be used in conjunction with past.
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
- **Description**: Validate the match to make sure that the colleges don't have conflicting matches and the location is open as well. 
- **Parameter


### Add Match

### Update Match
- **URL**: `/update-match`
- **Method**: `POST`
- **Description**: Updates the score of a specific match and recalculates the points for the associated colleges and participants. This endpoint also supports corrections to previously recorded scores.
- **Headers**: None
    - `Content-Type`: `application/json`
- **Body**: 
    - `match_id` (integer, required): Unique identifier of the match to be updated
    - `score1` (integer, required): The outcome of the first college
    - `score2` (integer, required): The outcome of the second college
    - `correction` (boolean, optional): Indicates whether this submission is correcting a previous score. Defaults to `false`. 
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

### Match Info 




