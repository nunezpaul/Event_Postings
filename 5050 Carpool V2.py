from selenium.webdriver.common.keys import Keys
import tools.facebookEvent as fbE

description = ((Keys.TAB, Keys.ARROW_DOWN,
                "What's up Caltech Westies!", 
                Keys.ENTER, Keys.ENTER, 
                "This coming Saturday we have the monthly dance 5050 Swing hosted by the amazing Samantha Buckwalter! ",
                "Time for the Caltech Crew to show up, represent and dance the night away.",
                Keys.ENTER, Keys.ENTER, 
                "The carpool is meeting at 8:30pm at Wilson and San Pasqual before we head over. ",
                "If you are coming RSVP so we know to wait for you or else tough toenails.",
                Keys.ENTER, Keys.ENTER, 
                "The dance costs $10 so don't forget to bring cash or venmo on your phone. ",
                "Times for the carpool are subject to change so remember to check up on any posts within this event!",
                Keys.ENTER, Keys.ENTER, 
                "See y'all then!",
                Keys.ENTER, Keys.ENTER,
                "Directions to meeting place: https://goo.gl/maps/x1n2pjZPgJ52"))
        
endtime = ['11', '55', 'PM']
starttime = ['8', '30', 'PM']
where = (("Northwest corner of Wilson and San Pasqual, Caltech", Keys.TAB))
eventname = 'Caltech Carpool to 5050 Swing!'
photo = '/Users/p/Desktop/Python/Facebook/Pictures/5050.png'
day = 5 #0+7*n = Monday, 1+7*n = Tuesday, 2+7*n = Wednesday

out = fbE.facebookEvent(photo = photo, day = day, eventname = eventname,
                        where = where, starttime = starttime,
                        description = description, endtime = endtime,
                        submit = True, post2Cal = True)
