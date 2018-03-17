import datetime

#weekday: 0=Monday, 1=Tuesday, 2=Wednesday...-1=Sunday, -2=Saturday, -3=Friay
#weeks_ahead: 0 is default for next week, 1 is the week after next...
#facebook_format: True gives date in the american format for FB events else y/m/d
def next_day(weekday, weeks_ahead = 0, facebook_format = True):
    today = datetime.date.today()
    days_ahead = weekday - today.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += (7)
    out = str(today + datetime.timedelta(days_ahead + weeks_ahead*7))
    year, month, day = out.split('-')
    if facebook_format == True:
        return month + '/' + day + '/' + year
    else:
        return year, month, day

if __name__ == '__main__':
    next_day(weekday=2 + 4*7) #next monday
    next_day(weekday=0, weeks_ahead=1) #second monday from now
    next_day(weekday=0, weeks_ahead=2, facebook_format=False) #third monday from now and y/m/d format
