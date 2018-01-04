from selenium.webdriver.common.keys import Keys
import tools.facebookEvent as fbE

name = "Malia San Nicholas"

description = ((Keys.TAB, Keys.ARROW_DOWN,
                "We're extremely excited to be hosting an int/adv class with the amazing " + name + ". ",
                "If you've taken classes with us then you're in a for a special treat! ",
                "If you're looking to take your dancing to the next level, this class is meant for you! ",
                "We don't host int/adv classes very often so definitely make it a point not to miss out! ",
                "As a reminder, you must be comfortable with 6- and 8-count basics, no partner is required and we're open to the public so tell your friends!",
                Keys.ENTER, Keys.ENTER,
                "Costs:", Keys.ENTER,
                "Current Caltech Students: $5", Keys.ENTER,
                "All Others: $10",
                Keys.ENTER, Keys.ENTER,
                "Parking is free on campus after 5:00 PM.",
                Keys.ENTER,
                "Directions to recommended parking: https://goo.gl/maps/4jyLq3jserC2",
                Keys.ENTER,
                "Directions to South Catalina Recreation Room: https://goo.gl/maps/UvT8FtHUZj72"))
        
endtime = ['8', '30', 'PM']
starttime = ['7', '30', 'PM']
where = (("South Catalina Recreation Room, Caltech", Keys.TAB))
eventname = "Int/Adv West Coast Swing w/ "+name+ "! (Week 3!)"
photo = '/Users/p/Desktop/Python/Facebook/Pictures/IntAdv.jpg'
day = 2+5*7 #0+7*n = Monday, 1+7*n = Tuesday, 2+7*n = Wednesday

out = fbE.facebookEvent(photo = photo, day = day, eventname = eventname,
                        where = where, starttime = starttime,
                        description = description, endtime = endtime,
                        submit = True, post2Cal = True)
                        
##out = ('https://www.facebook.com/events/305692859864620/', '2017-06-12')
#path.insert(0, '/Users/p/Desktop/Python/Google Calendar/')
#import InsertEvent
#
#starttime = fbE.milTime(starttime)
#endtime = fbE.milTime(endtime)
#
#if type(out) == str:
#    start = out+'T'+starttime[0]+':'+starttime[1]+':'+'00'
#    end = out+'T'+endtime[0]+':'+endtime[1]+':'+'00'
#    description = list(description[2:-3])
#else:
#    start = out[-1]+'T'+starttime[0]+':'+starttime[1]+':'+'00'
#    end = out[-1]+'T'+endtime[0]+':'+endtime[1]+':'+'00'
#    description = list(description[2:-3])
#    description.append('\n\nLink to Facebook event: ')
#    description.append(out[0])
##start = 2017-05-28T09:00:00
#
#for n,i in enumerate(description):
#    if type(i) == unicode:
#        description[n] = '\n'
#
#
#InsertEvent.insertEvent(title = eventname, location = where[0], 
#                        description = ''.join(description), start = start, end = end)
