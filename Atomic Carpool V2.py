from selenium.webdriver.common.keys import Keys
import tools.facebookEvent as fbE

description = ((Keys.TAB, Keys.ARROW_DOWN,
                "What's up Caltech Westies! ",
                "This Thursday the Ben Morris is hosting an college night at Atomic! ",
                "The Caltech Crew is planning to make an appearance and represent. ",
                "No car? No problem! We're carpooling from campus to Atomic in Irvine. ",
                "We'll be meeting at Wilson and San Pasqual. Make sure to indicate that ",
                "you're coming or we might leave without you. ",
                "The dance is $8 or $6 with a student ID.",
                Keys.ENTER, Keys.ENTER, 
                "Directions to meeting place: https://goo.gl/maps/x1n2pjZPgJ52",
                Keys.ENTER,
                "Link to event: https://www.facebook.com/events/132157340776232/"))
        
endtime = ['11', '59', 'PM']
starttime = ['9', '00', 'PM']
where = (("Northwest corner of Wilson and San Pasqual, Caltech", Keys.TAB))
eventname = 'Caltech Carpool to Atomic!'
photo = '/Users/p/Desktop/Python/Facebook/Pictures/StB.png'
day = 3 #0+7*n = Monday, 1+7*n = Tuesday, 2+7*n = Wednesday  

out = fbE.facebookEvent(photo = photo, day = day, eventname = eventname,
                        where = where, starttime = starttime,
                        description = description, endtime = endtime,
                        submit = True, post2Cal = True)
