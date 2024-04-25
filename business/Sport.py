class Sport:
    def __init__(self, id, name, points_for_win, season, icon, dao=None, matches=None):
        self._id = id
        self._name = name
        self._points_for_win = points_for_win
        self._season = season
        self._icon = icon
        self._dao = dao
        self._matches = matches

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def points_for_win(self):
        return self._points_for_win

    @property
    def season(self):
        return self._season

    @property
    def icon(self):
        return self._icon

    @property
    def matches(self):
        if self._matches is None and self._dao:
            self._matches = self._dao.get_matches_by_sport(self._name)
        return self._matches

    def to_dict(self):
        return {
            'id': self._id,
            'name': self._name,
            'points_for_win': self._points_for_win,
            'season': self._season,
            'icon': self._icon,
            'matches': [match.to_dict() for match in self.matches]
        }

    @classmethod
    def get_all_sports(cls, dao):
        return dao.get_all_sports()
    
    @classmethod
    def get_sport_by_name(cls, sport_name, dao):
        return dao.get_sport_by_name(sport_name)
