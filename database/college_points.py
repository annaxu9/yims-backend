import sys
sys.path.append('/Users/annaxu/Desktop')

from yims_backend.models.CollegeDB import CollegeDB
from yims_backend.consts import colleges
import session


points = [15, 22, 95, 33, 45, 30, 10, 64, 34, 55, 32, 13, 35, 67, 43, 54, 22]



# Create colleges!
for i, college in enumerate(colleges):
    college_info = CollegeDB(name=college, abbreviation=colleges[college], points=points[i])
    college_info.save()