class User:
    def __init__(self, netid, firstname, lastname, college, role):
        self._netid = netid
        self._firstname = firstname
        self._lastname = lastname
        self._college = college
        self._role = role
        self._points = 0
        self._matches = None