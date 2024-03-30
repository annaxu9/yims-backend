class User:
    def __init__(self, netid, firstname, lastname, college, role):
        self._netid = netid
        self._firstname = firstname
        self._lastname = lastname
        self._college = college
        self._role = role
        self._points = 0
        self._matches = None

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
    
    def to_dict(self):
        return {
            'netid': self._netid,
            'firstname': self._firstname,
            'lastname': self._lastname,
            'college': self._college,
            'role': self._role,
            'points': self._points,
            'matches': self._matches
        }