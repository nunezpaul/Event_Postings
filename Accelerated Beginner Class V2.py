from selenium.webdriver.common.keys import Keys
import tools.facebookEvent as fbE

description = ((Keys.TAB, Keys.ARROW_DOWN,
                "This is a 4 week beginner series in west coast swing. ",
                "This series will start with the very basics and get you dancing! ",
                "This series is perfect for people who are totally new to dancing ",
                "and those who have danced some west coast swing before, ",
                "but are looking to strengthen their social dancing! ",
                "As a reminder, no partner or experience is required and we're open to the public!",
                Keys.ENTER, Keys.ENTER, 
                "Week 1 ~ Intro to WCS (Timing, Structure, Basic 6 Count Patterns)",
                Keys.ENTER, 
                "Week 2 ~ Basic 6 Count Patterns Cont., Connection, Lead/Follow Technique",
                Keys.ENTER, 
                "Week 3 ~ Basic 8 Count Patterns",
                Keys.ENTER,
                "Week 4 ~ 8 Count Pattern Variations",
                Keys.ENTER, Keys.ENTER, 
                "Parking is free on campus after 5:00 PM.",
                Keys.ENTER, 
                "Directions to recommended parking: https://goo.gl/maps/4jyLq3jserC2",
                Keys.ENTER, 
                "Directions to South Catalina Recreation Room: https://goo.gl/maps/UvT8FtHUZj72"))
        
endtime = ['8', '30', 'PM']
starttime = ['7', '30', 'PM']
where = (("South Catalina Recreation Room", Keys.ENTER))
eventname = 'Beginner West Coast Swing Week 4!'
photo = '/Users/p/Desktop/Python/Facebook/Pictures/Beg.jpg'
day = 2#+7*2 #= Monday, 1+7*n = Tuesday, 2+7*n = Wednesday /// +7*2 is two weeks out +7*1 is one week out ///

out = fbE.facebookEvent(photo = photo, day = day, eventname = eventname, 
                        where = where, starttime = starttime, 
                        description = description, endtime = endtime, 
                        submit = True, post2Cal = True)
