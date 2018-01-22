from selenium.webdriver.common.keys import Keys
import tools.facebookEvent as fbE

description = ((Keys.ARROW_DOWN,
        " What's up Caltech Westies!",
        Keys.ENTER, Keys.ENTER, 
        " Caltech West Coast Swing is hosting our usual social dance starting at 8:30pm! ",
        "Our dance finishes either at 11:00 or later depending on how lively y'all are. ",
        "As usual, our social dance is free for all so bring a friend and come dance! ",
        Keys.ENTER, Keys.ENTER, 
        " See y'all then!",
        Keys.ENTER, 
        "___________________________________________________",
        Keys.ENTER, Keys.ENTER, 
        " West Coast Wednesday at Caltech happens every Wednesday night!",
        Keys.ENTER, Keys.ENTER, 
        " Parking is free on campus after 5:00 PM.",
        Keys.ENTER, 
        " Directions to recommended parking: https://goo.gl/maps/4jyLq3jserC2",
        Keys.ENTER, 
        " Directions to South Catalina Recreation Room: https://goo.gl/maps/UvT8FtHUZj72"))

#http://goo.gl/maps/YTSL1 winnet lounge https://goo.gl/maps/gJ4Yvh9Qc982 parking for winnett
        
endtime = ['11', '00', 'PM']
starttime = ['08', '30', 'PM']
where = (("South Catalina Recreation Room", Keys.ENTER))
eventname = 'West Coast Wednesday at Caltech! (South Cat)'
photo = '/Users/p/Desktop/Python/Facebook/Pictures/wcs.png'
day = 2 #0+7*n = Monday, 1+7*n = Tuesday, 2+7*n = Wednesday 

out = fbE.facebookEvent(photo = photo, day = day, eventname = eventname, 
                        where = where, starttime = starttime, 
                        description = description, endtime = endtime, 
                        submit = False, post2Cal = False, driven = True)
