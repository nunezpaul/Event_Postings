from selenium.webdriver.common.keys import Keys
import facebookEvent as fbE

description = ((Keys.TAB, Keys.ARROW_DOWN,
                "This week we're having a special beginner/intermediate west coast swing workshop! ",
                "If you've taken the beginner class from us then this class will be great for you! ",
                "We're looking to expand upon your basics and further develop your options, technique and solidify your social dancing. "
                "As a reminder, no partner or experience is required and we're open to the public!",
                Keys.ENTER, Keys.ENTER,
                "Cost:",
                Keys.ENTER,
                "Current Caltech students: Free",
                Keys.ENTER,
                "All others: suggested donation of $3-5",
                Keys.ENTER, Keys.ENTER,
                "Parking is free on campus after 5:00 PM.",
                Keys.ENTER,
                "Directions to recommended parking: https://goo.gl/maps/4jyLq3jserC2",
                Keys.ENTER,
                "Directions to South Catalina Recreation Room: https://goo.gl/maps/UvT8FtHUZj72"))
        
endtime = ['8', '30', 'PM']
starttime = ['7', '30', 'PM']
where = (("South Catalina Recreation Room", Keys.TAB))
eventname = 'Beg/Int West Coast Swing Workshop! (South Cat)'
photo = '/Users/p/Desktop/Python/Facebook/Pictures/Beg.jpg'
day = 2 #0+7*n = Monday, 1+7*n = Tuesday, 2+7*n = Wednesday  

out = fbE.facebookEvent(photo = photo, day = day, eventname = eventname,
                        where = where, starttime = starttime,
                        description = description, endtime = endtime,
                        submit = False, post2Cal = False)
