import sys
sys.path.append('/Users/annaxu/Desktop')

from yims_backend.database.session import session
from yims_backend.tables.CollegeDB import CollegeDB
from yims_backend.models.College import College

class CollegeDAO:
    def get_all_colleges_alphabetical(self):
        colleges = session.query(CollegeDB).all()
        return [College(college.name, college.abbreviation, college.points) for college in colleges]
    def get_leaderboard(self):
        colleges = session.query(CollegeDB).order_by(CollegeDB.points.desc()).all()
        return [College(college.name, college.abbreviation, college.points).to_dict() for college in colleges]
    def get_college_by_name(self, college_name):
        college = session.query(CollegeDB).filter_by(name=college_name).first()
        if college:
            return College(college.name, college.abbreviation, college.points)
        return None
    def add_points_to_college(self, college_name, additional_points):
        college = session.query(CollegeDB).filter_by(name=college_name).first()
        if college:
            college.points += additional_points
            session.commit()