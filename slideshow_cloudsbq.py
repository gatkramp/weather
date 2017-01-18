# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:29:36 2015

@author: FvdMerwe
"""


import time,datetime
import numpy as np

import cv2 as cv
import os

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
        i = 45
    elif time_min < 30:
        i = 00
    elif time_min < 45:
        i = 15
    else:
        i = 30
    return i

def fixhour(hour):
    if hour < 0:
        hour = hour + 24
    return hour
    
while 1==1:

    now = datetime.datetime.now()
    
    a = fillnull(now.year,4) + fillnull(now.month,2) + fillnull(now.day,2) + fillnull(fixhour(now.hour-2),2) + fillnull(previousmin(now.minute),2)
    im_files = []
    
    for i in range(1):
            for j in range(6):
                for k in range(0,46,15):
                    b = fillnull(now.year,4) + fillnull(now.month,2) + fillnull(now.day-i,2) + fillnull(fixhour(now.hour-2-j),2) + fillnull(previousmin(now.minute-k),2)
                    if int(b) <= int(a):
                        if os.path.isfile('cloud/'+b+'.jpg') == True:
                            if os.path.getsize('cloud/'+b+'.jpg') > 500: 
    #                            print b,os.path.getsize('cloud/'+b+'.jpg')
                                im_files.append('cloud/'+b+'.jpg')
    #im_files = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
    
    im_files.sort()
    
    newx = 600
    newy = 437
    for f in im_files:

        im = cv.imread(f, 1) #read image in greyscale
        cv.circle(im,(495,265), 2, (0,0,255), -1)
#        im = cv.resize(im,(newx,newy))
        cv.imshow('display', im)
        cv.waitKey(50)
    cv.waitKey(1500)

cv.destroyAllWindows()