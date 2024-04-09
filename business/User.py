class User:
    def __init__(self, netid, firstname, lastname, college, role, dao=None, points=0, matches=None):
        self._netid = netid
        self._firstname = firstname
        self._lastname = lastname
        self._college = college
        self._role = role
        self._points = points
        self._matches = matches
        self._dao = dao

    @property
    def netid(self):
        return self._netid

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def college(self):
        return self._college

    @property
    def role(self):
        return self._role

    @property
    def points(self):
        return self._points

    @property
    def matches(self):
        if self._matches is None and self._dao:
            self._matches = self._dao.get_matches_by_user(self._netid)
        return self._matches

    def to_dict(self):
        return {
            'netid': self._netid,
            'firstname': self._firstname,
            'lastname': self._lastname,
            'college': self._college,
            'role': self._role,
            'points': self._points,
            'matches': [match.to_dict() for match in self.matches]
        }
    
    @classmethod
    def get_user(cls, netid, user_dao):
        user_db = user_dao.get_user(netid)
        if user_db:
            return cls(
                netid=user_db.netid,
                firstname=user_db.firstname,
                lastname=user_db.lastname,
                college=user_db.college,
                role=user_db.role,
                points=user_db.points,
                dao=user_dao
            )
        return None
