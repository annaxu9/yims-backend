class College:
    def __init__(self, name, abbreviation, points, dao=None, matches=None):
        self._college_name = name
        self._college_abbreviation = abbreviation
        self._points = points
        self._dao = dao
        self._matches = matches

    @property
    def name(self):
        return self._college_name

    @property
    def abbreviation(self):
        return self._college_abbreviation

    @property
    def points(self):
        return self._points

    @property
    def matches(self):
        if self._matches is None and self._dao:
            self._matches = self._dao.get_matches_by_college(self._college_name)
        return self._matches

    def to_dict(self):
        return {
            'name': self._college_name,
            'abbreviation': self._college_abbreviation,
            'points': self._points,
            'matches': [match.to_dict() for match in self.matches] if self.matches else []
        }
    
    def get_college_id(self):
        return self._dao.get_college_id(self._college_name)

    @classmethod
    def get_all_colleges(cls, dao):
        return dao.get_all_colleges_alphabetical()

    @classmethod
    def get_leaderboard(cls, dao):
        return dao.get_leaderboard()

    @classmethod
    def get_college_by_name(cls, college_name, dao):
        return dao.get_college_by_name(college_name)

    @classmethod
    def add_points_to_college(cls, college_name, additional_points, dao):
        return dao.add_points_to_college(college_name, additional_points)
