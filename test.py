from sys import path
path.append('/Users/annaxu/Desktop')

from flask import jsonify

from yims_backend.data_access_layer.CollegeDataAccess import CollegeDAO

collegedao = CollegeDAO()

print(collegedao.get_leaderboard())



