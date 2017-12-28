# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/google-apps/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.


from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from credentials import get_credentials
import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'
    
def insertEvent(title, location, description, start, end):
    """Shows basic usage of the Google Calendar API.
        
        Creates a Google Calendar API service object and outputs a list of the next
        10 events on the user's calendar.
        """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    event = {
      'summary': title,
      'location': location,
      'description': description,
      'start': {
        'dateTime': start, #+ '-07:00', #-7:00 refers to GMT time
        'timeZone': 'America/Los_Angeles',
      },
      'end': {
        'dateTime': end, #+ '-07:00',
        'timeZone': 'America/Los_Angeles',
      },
#      'attendees': [
#        {'email': 'pnunez@caltech.edu'},
#      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'popup', 'minutes': 59},         
        ],
      },
    }
    
    event = service.events().insert(calendarId='m1mms29e3dndra26c4g8mqu7e4@group.calendar.google.com', body=event).execute()
    print ('Event created: %s' % (event.get('htmlLink')))



if __name__ == '__main__':
    title = 'test event'
    location = 'South Catalina Recreation Room'
    description = "stuff that goes here \n lets add a new line"
    start = '2017-07-15T09:00:00'
    end = '2017-07-15T16:00:00'
    insertEvent(title = title, location = location, description=description,
         start = start, end = end)
         
