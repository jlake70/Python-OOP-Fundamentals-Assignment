from event import Event

class ParticipantEvent(Event):
    def __init__(self, name, date):
        super().__init__(name, date)
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count