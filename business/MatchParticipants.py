class MatchParticipant:
    def __init__(self, match, user):
        self._match = match
        self._user = user

    @property
    def match(self):
        return self._match
    
    @property
    def user(self):
        return self._user
    
    def to_dict(self):
        return {
            'match': self._match.to_dict(),
            'user': self._user.to_dict()
        }
