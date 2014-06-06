from community_share import store, mail_actions
from community_share.models.share import EventReminder

ONEDAY_EVENT_REMINDER_TEMPLATE = '''You have an share coming up with {{otheruser.name}}
'''

def send_reminders():
    events = EventReminder.get_oneday_reminder_events()
    event_reminders = [EventReminder(event_id=event.id, typ='oneday_before')
                       for event in events]
    for reminder in event_reminders:
        store.session.add(reminder)
    store.session.commit()
    for event in events:
        mail_actions.send_event_reminder_message(event)
    