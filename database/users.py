import sys
sys.path.append('/Users/annaxu/Desktop')

from yims_backend.tables.UserDB import UserDB
from yims_backend.data_acess_layer.UsersDataAccess import UsersDAO

colleges = {
    "Benjamin Franklin" : 'BF', 
    "Berkeley": 'BK', 
    "Branford": 'BR',
    "Davenport": 'DC',
    "Ezra Stiles": 'ES',
    "Grace Hopper": 'GH',
    "Jonathan Edwards": 'JE',
    "Morse": 'MC',
    "Pauli Murray": "MY",
    "Pierson": 'PC',
    "Saybrook": 'SY',
    "Silliman": 'SM',
    "Timothy Dwight": 'TD',
    "Trumbull": 'TC'
    }

fake_people = [
    {"netid": "jdoe1", "firstname": "John", "lastname": "Doe", "college": "Berkeley", "role": "player"},
    {"netid": "asmith2", "firstname": "Alice", "lastname": "Smith", "college": "Silliman", "role": "admin"},
    {"netid": "mjohnson3", "firstname": "Michael", "lastname": "Johnson", "college": "Jonathan Edwards", "role": "ref"},
    {"netid": "lwilliams4", "firstname": "Linda", "lastname": "Williams", "college": "Trumbull", "role": "player"},
    {"netid": "bwhite5", "firstname": "Betty", "lastname": "White", "college": "Grace Hopper", "role": "admin"},
    {"netid": "tgreen6", "firstname": "Tom", "lastname": "Green", "college": "Davenport", "role": "ref"},
    {"netid": "slee7", "firstname": "Sarah", "lastname": "Lee", "college": "Ezra Stiles", "role": "player"},
    {"netid": "cwalker8", "firstname": "Charles", "lastname": "Walker", "college": "Pierson", "role": "admin"},
    {"netid": "kthomas9", "firstname": "Karen", "lastname": "Thomas", "college": "Saybrook", "role": "ref"},
    {"netid": "dmoore10", "firstname": "David", "lastname": "Moore", "college": "Pauli Murray", "role": "player"}
]

# Assuming you have a function to get the college_id based on the college name
def get_college_id(college_name):
    return list(colleges).index(college_name) + 1

# Loop to iterate over the list of fake people and add them to the database
for person in fake_people:
    college_id = get_college_id(person["college"])
    user = UserDB(netid=person["netid"], firstname=person["firstname"], lastname=person["lastname"], college_id=college_id, role=person["role"])
    user.save()


pr


