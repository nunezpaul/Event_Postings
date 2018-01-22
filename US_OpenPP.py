from selenium.webdriver.common.keys import Keys
import tools.facebookEvent as fbE

description = ((Keys.ARROW_DOWN, 
        " What's up Caltech Westies!",
        Keys.ENTER, Keys.ENTER, 
        " Instead of hosting our weekly, we're hosting a carpool to the US Open Pre-Party! ",
        "It's somewhat of a tradition as this will be the third year in a row. ",
        "The time we leave is somewhat flexible and subject to change. ",
        "The dance is $10 and goes till an ungodly hour most likely so be prepared! ",
        Keys.ENTER,
        " See you there!",
        Keys.ENTER, Keys.ENTER,
        " Link to the event:",
        Keys.ENTER,
        " https://www.facebook.com/events/1986737624880114/"))

#http://goo.gl/maps/YTSL1 winnet lounge https://goo.gl/maps/gJ4Yvh9Qc982 parking for winnett
        
endtime = ['11', '59', 'PM']
starttime = ['08', '30', 'PM']
where = (("Corner of Wilson and San Pasqual", Keys.ENTER))
eventname = "Caltech Carpool to US Open Pre-Party!"
photo = "/Users/p/Desktop/Python/Facebook/Pictures/USOpenPP.jpg"
day = 2 #0+7*n = Monday, 1+7*n = Tuesday, 2+7*n = Wednesday 

out = fbE.facebookEvent(photo = photo, day = day, eventname = eventname, 
                        where = where, starttime = starttime, 
                        description = description, endtime = endtime, 
                        submit = True, post2Cal = True)
