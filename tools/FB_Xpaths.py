#create event button
eventXpath = "(.//*[@class='_42ft _4jy0 _3-9a _4jy3 _4jy1 selected _51sy'])"

#all the different sections to be filled in for an event on FB
eventNameXpath = "(.//*[@class='_58al'])[3]"
locationXpath = "(.//*[@class='_58al'])[4]"
dateXpath = "(.//*[@class='_3smp'])[1]"
timeHourXpath = "(.//*[@class='_4nx5'])[1]"
timeMinuteXpath = "(.//*[@class='_4nx5'])[2]"
timeAMPMXpath = "(.//*[@class = '_4nx5'])[3]"
moreInfoXpath = "(.//*[@class ='notranslate _5rpu'])"
addPhotoXpath = ".//*[@class='_n _5f0v']"

#end time used to be optional
endDateXpath = "(.//*[@class='_3smp'])[2]"
endHourXpath = "(.//*[@class='_4nx5'])[4]"
endMinuteXpath = "(.//*[@class='_4nx5'])[5]"
endAMPMXpath = "(.//*[@class='_4nx5'])[6]"

#submit button
submitClickXpath = ".//*[@class = '_42ft _4jy0 layerConfirm uiOverlayButton _4jy3 _4jy1 selected _51sy']"
