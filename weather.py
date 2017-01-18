# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\FvdMerwe\.spyder2\.temp.py
"""

import urllib2,datetime,os.path,time

def downloadimg(url,file_name):
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')    
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break    
        f.write(buffer)
    f.close()
    

    
#downloadimg('http://en.sat24.com/image?type=cloud&region=za&timestamp=201511180500','201511180500.jpg')
def fillnull(number,length):
    string = str(number)
    while (len(string) < length):
        string = '0' + string
    return string

def previousmin(time_min):
    i = 0
    if time_min < 0:
        time_min = time_min +60
    if time_min < 15:
        i = 0
    elif time_min < 30:
        i = 15
    elif time_min < 45:
        i = 30
    else:
        i = 45
    return i

def fixhour(hour):
    if hour < 0:
        hour = hour + 24
    return hour
        
print "Downloading the newsest weather images:"        


while 1==1: 
    try:
        now = datetime.datetime.now()   
        a = fillnull(now.year,4) + fillnull(now.month,2) + fillnull(now.day,2) + fillnull(fixhour(now.hour-2),2) + fillnull(previousmin(now.minute),2)
    
        for i in range(2):
            for j in range(24):
                for k in range(0,46,15):
                    b = fillnull(now.year,4) + fillnull(now.month,2) + fillnull(now.day-i,2) + fillnull(fixhour(now.hour-2-j),2) + fillnull(previousmin(now.minute-k),2)
                    if int(b) < int(a):
                        if os.path.isfile('cloud/'+b+'.jpg') == False:
                            print 'Downloading cloud/'+b+'.jpg'
                            downloadimg('http://en.sat24.com/image?type=cloud&region=za&timestamp='+b,'cloud/'+b+'.jpg')
                        if os.path.isfile('rain/'+b+'.jpg') == False:
                            print 'Downloading rain/'+b+'.jpg'
                            downloadimg('http://en.sat24.com/image?type=rain&region=za&timestamp='+b,'rain/'+b+'.jpg')
                        if os.path.isfile('infra/'+b+'.jpg') == False:
                            print 'Downloading infra/'+b+'.jpg'
                            downloadimg('http://en.sat24.com/image?type=infraPolair&region=za&timestamp='+b,'infra/'+b+'.jpg')
        time.sleep(60)
    except:
        print 'error downloading...'
        time.sleep(60)
    
