from selenium.webdriver.common.keys import Keys
import tools.facebookEvent as fbE

description = ((Keys.TAB, Keys.ARROW_DOWN,
                "What's up Caltech Westies!", 
                Keys.ENTER, Keys.ENTER, 
                "This Friday is another installment of Blackout Friday hosted by the Demetre Souliotes! ",
                "Time for the Caltech Crew to show up and represent.", 
                Keys.ENTER, Keys.ENTER, 
                "The carpool is meeting at 7:30pm at Wilson and San Pasqual before we head over. ",
                "If you are coming facebook RSVP so we know to wait for you or else tough toenails.",
                Keys.ENTER, Keys.ENTER, 
                "As a reminder, students get into the dance for $5 with your student ID. ",
                "The beginner classes are free, the Int/Adv classes are $5 and they are definitely worth it!",
                Keys.ENTER, Keys.ENTER, 
                "See y'all then!",
                Keys.ENTER, Keys.ENTER,
                "Directions to meeting place: https://goo.gl/maps/x1n2pjZPgJ52"))
        
endtime = ['11', '59', 'PM']
starttime = ['7', '30', 'PM']
where = (("Northwest corner of Wilson and San Pasqual, Caltech", Keys.TAB))
eventname = 'Caltech Carpool to Blackout Friday!'
photo = '/Users/p/Desktop/Python/Facebook/Pictures/bof.png'
day = 4+0*7 #0+7*n = Monday, 1+7*n = Tuesday, 2+7*n = Wednesday

out = fbE.facebookEvent(photo = photo, day = day, eventname = eventname, 
                        where = where, starttime = starttime, 
                        description = description, endtime = endtime, 
                        submit = True, post2Cal = True, driven = False)
