from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from loginFB import login
from next_date import next_day
import time
from FB_Xpaths import *

#3.4.1 selenium
#54.0.1 firefox

#test = ['11', '00', 'PM']
def milTime(time):
    if time[2] == 'PM':  
        return str(int(time[0])+12), time[1]
    else:
        return time

def find_element_by_xpath_robust(driver, Xpath):
    return WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(Xpath))

def facebookEvent(photo, day, eventname, where, starttime, 
                  description, endtime = False, submit = True, post2Cal = False, driven = True):
    #logging in
    if driven:
        driver = login()
    
        try:
            facebookLogo = find_element_by_xpath_robust(driver, facebookLogoXpath)
            print('Found facebook logo!')
        except:
            print('Unable to find facebook logo :(')
        
        driver.get("https://www.facebook.com/groups/caltechwcs/events")
        
        #select create event
        event = find_element_by_xpath_robust(driver, eventXpath)
        event.click()
        
        #to do: make the put in a for loop within the try to shorten the eventName through moreInfo into 3 lines.
        #should be put into a dictionary such that I can keep track of it
        #find event info location
        i = 0
        while True:
            try:
                eventName =  find_element_by_xpath_robust(driver, eventNameXpath)
                location =  find_element_by_xpath_robust(driver, locationXpath)
                date =  find_element_by_xpath_robust(driver, dateXpath)
                timeHour = find_element_by_xpath_robust(driver, timeHourXpath)
                timeMinute = find_element_by_xpath_robust(driver, timeMinuteXpath)
                timeAMPM = find_element_by_xpath_robust(driver, timeAMPMXpath)
                submitClick = find_element_by_xpath_robust(driver, submitClickXpath)
                addPhoto = find_element_by_xpath_robust(driver, addPhotoXpath)
                moreInfo = find_element_by_xpath_robust(driver, moreInfoXpath)
                
                    #if endtime is not False:
                    #endTimeClick = driver.find_element_by_xpath(endTimeClickXpath)
                    #open endTime
                    #endTimeClick.click()
                break
            except Exception as E:
                print('attempting to find event pop-up...')
                i+=1
                if i > 10:
                    print('early stopping because: ')
                    print(E)
                    driver.close()
                    exit()
                        
        
        #add Photo
        addPhoto.send_keys(photo)
        
        #Next Day python 2 import
        next_occurence = next_day(day, 0, False)

        date.clear()
        date.send_keys(next_day(day)) #7/13/2016
        
        #send event info
        eventName.clear()
        eventName.send_keys(eventname + ' (' + str(next_occurence[1]) + '/' + str(next_occurence[2]) + ')')
        location.send_keys(where)
        
        #set the time
        timeHour.clear()
        timeHour.send_keys(starttime[0])
        timeMinute.clear()
        timeMinute.send_keys(starttime[1])
        timeAMPM.clear()
        timeAMPM.send_keys(starttime[2])
        
        #Add ending time
        while endtime is not False:
            try:
                endDate = find_element_by_xpath_robust(driver, endDateXpath)
                endHour = find_element_by_xpath_robust(driver, endHourXpath)
                endMinute = find_element_by_xpath_robust(driver, endMinuteXpath)
                endAMPM = find_element_by_xpath_robust(driver, endAMPMXpath)
                break
            except:
                print('searching for ending time and date...')

        if endtime is not False:
            endDate.clear()
            endDate.send_keys(next_day(day))
            
            #ending time
            endHour.clear()
            endHour.send_keys(endtime[0])
            endMinute.clear()
            endMinute.send_keys(endtime[1])
            endAMPM.clear()
            endAMPM.send_keys(endtime[2])
            
            #enter the details to the event
            moreInfo.clear()
            moreInfo.send_keys(description)

        else:
            moreInfo.clear()
            moreInfo.send_keys(description)


        if submit is True:
            time.sleep(5)
            submitClick.click()
            time.sleep(10)
            
            while True:
                try:
                    facebookLogo = find_element_by_xpath_robust(driver, facebookLogoXpath)
                    break
                except:
                    print('waiting for page to load')

            FBlink = str(driver.current_url)
            print(FBlink.split('?')[0])
            driver.close()
            out = FBlink.split('?')[0], next_occurence[0]+'-'+ next_occurence[1]+'-'+next_occurence[2]
        else:
            out = next_occurence[0]+'-'+ next_occurence[1]+'-'+next_occurence[2]
    else:
        next_occurence = next_day(day, 0, False)
        out = next_occurence[0]+'-'+ next_occurence[1]+'-'+next_occurence[2]
        
    if post2Cal is True:
        from sys import path
        path.insert(0, '/Users/p/Desktop/Python/Google Calendar/')
        import InsertEvent

        starttime = milTime(starttime)
        endtime = milTime(endtime)

        if type(out) == str:
            start = out+'T'+starttime[0]+':'+starttime[1]+':'+'00'
            end = out+'T'+endtime[0]+':'+endtime[1]+':'+'00'
        else:
            start = out[-1]+'T'+starttime[0]+':'+starttime[1]+':'+'00'
            end = out[-1]+'T'+endtime[0]+':'+endtime[1]+':'+'00'    
        #start = 2017-05-28T09:00:00
        
        if 'FBlink' in locals():
            description = list( description[2:] + tuple((Keys.ENTER, Keys.ENTER,
                                'Time: ', starttime[0]+':'+starttime[1],
                                ' - ', endtime[0]+':'+endtime[1],Keys.ENTER,Keys.ENTER,
                                'Link to Facebook event: ',FBlink.split('?')[0])) )
        else:
            description = list(description[2:]+ tuple((Keys.ENTER, Keys.ENTER,
                                            'Time: ', starttime[0]+':'+starttime[1],
                                            ' - ', endtime[0]+':'+endtime[1])) )
        
        for n,i in enumerate(description):
            if type(i) == unicode:
                description[n] = '\n'
        
        InsertEvent.insertEvent(title = eventname, location = where[0], 
                                description = ''.join(description), start = start, end = end)
        return out

#sample of link collected: 'https://www.facebook.com/events/305692859864620/?context=create&previousaction=create&ref=4&sid_create=866238603&action_history=%5B%7B%22surface%22%3A%22create_dialog%22%2C%22mechanism%22%3A%22group_create_dialog%22%2C%22extra_data%22%3A%5B%5D%7D%5D&has_source=1'

#sample of link returned: 'https://www.facebook.com/events/305692859864620/'
#sample of date time out '2017-05-28

