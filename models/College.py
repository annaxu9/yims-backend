class College:
    def __init__(self, name, abbreviation, points):
        self._college_name = name
        self._college_abbreviation = abbreviation
        self._points = points
        self._matches = None # finish this (lazy loading)

    @property
    def name(self):
        return self._college_name
    
    @property
    def abbreviation(self):
        return self._college_abbreviation
    
    @property
    def points(self):
        return self._points
    
    def to_dict(self):
        return {
            'name': self._college_name,
            'abbreviation': self._college_abbreviation,
            'points': self._points,
            'matches': self._matches
        }