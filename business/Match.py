class Match:
    def __init__(self, college1, college2, sport, location, date, start_time, college1_pts=-1, college2_pts=-1, ref=None, college_dao=None, sport_dao=None, user_dao=None):
        self._college1 = college1
        self._college2 = college2
        self._sport = sport
        self._location = location
        self._date = date
        self._start_time = start_time
        self._college1_pts = college1_pts
        self._college2_pts = college2_pts
        self._ref = ref
        self._college_dao = college_dao
        self._sport_dao = sport_dao
        self._user_dao = user_dao

    @property
    def colleges(self):
        return (self._college1, self._college2)

    @property
    def sport(self):
        return self._sport

    @property
    def location(self):
        return self._location

    @property
    def date(self):
        return self._date

    @property
    def start_time(self):
        return self._start_time

    @property
    def ref(self):
        return self._ref

    def to_dict(self):
        return {
            'college1': self._college1.name,
            'college2': self._college2.name,
            'sport': self._sport.name,
            'location': self._location,
            'date': self._date,
            'startTime': self._start_time,
            'college1Points': self._college1_pts,
            'college2Points': self._college2_pts,
            'ref': self._ref.netid if self._ref else None
        }

    @classmethod
    def get_filtered_matches(cls, dao, college=None, sport=None):
        return dao.get_filtered_matches(college=college, sport=sport)

    @classmethod
    def add_match(cls, dao, college1, college2, sport, location, date, start_time):
        return dao.add_match(college1, college2, sport, location, date, start_time)

    @classmethod
    def delete_match(cls, dao, match_id):
        return dao.delete_match(match_id)

    @classmethod
    def get_past_unscored_matches(cls, dao):
        return dao.get_past_unscored_matches()
    
    @classmethod
    def from_db(cls, match_db, college_dao, sport_dao, user_dao):
        college1 = college_dao.get_college_by_id(match_db.college_id1)
        college2 = college_dao.get_college_by_id(match_db.college_id2)
        sport = sport_dao.get_sport_by_id(match_db.sport_id)
        ref = user_dao.get_user_by_net_id(match_db.ref_id)
        return cls(college1=college1, college2=college2, sport=sport, location=match_db.location, date=match_db.date, start_time=match_db.start_time, college1_pts=match_db.college_pts1, college2_pts=match_db.college_pts2, ref=ref, college_dao=college_dao, sport_dao=sport_dao, user_dao=user_dao)