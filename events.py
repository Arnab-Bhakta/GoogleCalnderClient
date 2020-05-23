
event_template = {
  'summary': 'Google I/O 2015',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2015-05-28T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2015-05-28T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

class events():
    event = {}
    def __init__(self, name, stime, etime, reminder, color):
        #self.event = event_template
        self.event['summary'] = name
        self.event[ 'start' ] = {
                                    'dateTime': stime,
                                    'timeZone': 'Asia/Kolkata',
                                },
        self.event[ 'end' ] = {
                                    'dateTime': etime,
                                    'timeZone': 'Asia/Kolkata',
                                }
        self.event[ 'reminders' ] = {
                                        'useDefault': False,
                                        'overrides': [
                                        {'method': 'email', 'minutes': 60},
                                        {'method': 'popup', 'minutes': 15},
                                        ],
                                    }
        self.event[ 'colorId' ] = "11"


   
