class College:
    def __init__(self, name, abbreviation, points):
        self._college_name = name
        self._college_abbreviation = abbreviation
        self._points = points
        self._matches = None

    @property
    def name(self):
        return self._college_name
    
    @property
    def abbreviation(self):
        return self._college_abbreviation
    
    @property
    def points(self):
        return self._points