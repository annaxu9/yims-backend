import sys
sys.path.append('/Users/annaxu/Desktop')

from yims_backend.tables.CollegeDB import CollegeDB
from yims_backend.tables.SportDB import SportDB
from yims_backend.consts import colleges, fall_sports, winter_sports, spring_sports

# Create colleges!
for college in colleges:
    college_info = CollegeDB(name=college, abbreviation=colleges[college])
    college_info.save()

# Create fall sports!
for sport in fall_sports:
    sports = SportDB(name=sport, season="fall", points_for_win=fall_sports[sport][0], icon=fall_sports[sport][1])
    sports.save()

# Create winter sports!
for sport in winter_sports:
    sports = SportDB(name=sport, season="winter", points_for_win=winter_sports[sport][0], icon=winter_sports[sport][1])
    sports.save()

# Create spring sports!
for sport in spring_sports:
    sports = SportDB(name=sport, season="spring", points_for_win=spring_sports[sport][0], icon=spring_sports[sport][1])
    sports.save()

