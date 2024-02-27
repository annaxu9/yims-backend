class Sport:
    def __init__(self, name, points_for_win, season, icon):
        self._name = name
        self._points_for_win = points_for_win
        self._season = season
        self._icon = icon
    
    @property
    def get_name(self):
        return self._name
    
    @property
    def get_points_for_win(self):
        return self._points_for_win
    
    @property
    def get_season(self):
        return self._season
    
    @property
    def get_icon(self):
        return self._icon