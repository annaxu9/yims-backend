from sys import path
path.append('/Users/annaxu/Desktop')

from yims_backend.data_access_layer.CollegeDataAccess import CollegeDAO

collegedao = CollegeDAO()

collegedao.add_points_to_college('Pierson', 20)

colleges = collegedao.get_all_colleges_by_points()
for college in colleges:
    print(college.name, college.abbreviation, college.points)



