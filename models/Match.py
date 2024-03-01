class Match:
    def __init__(self, college1, college2, sport, location, date, start_time):
        self._college1_name = college1
        self._college2_name = college2
        self._sport_name = sport
        self._location = location
        self._date = date
        self._start_time = start_time
        self._college1_pts = -1
        self._college2_pts = -1

    @property
    def get_colleges(self):
        return (self._college1_name, self._college2_name)
    
    @property
    def get_sport(self):
        return self._sport_name
    
    @property
    def get_location(self):
        return self._location
    
    @property
    def get_date(self):
        return self._date
    
