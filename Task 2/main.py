from participant_event import ParticipantEvent

event = ParticipantEvent("Python Workshop", "2023-09-15")


event.add_participant()
event.add_participant()
event.add_participant()


print(f"Current participant count: {event.get_participant_count()}")
