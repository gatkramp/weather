# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:38:32 2015

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

error_cnt = 0    
while 1==1:
    try:

        now = datetime.datetime.now()
        
        a = fillnull(now.year,4) + fillnull(now.month,2) + fillnull(now.day,2) + fillnull(fixhour(now.hour-2),2) + fillnull(previousmin(now.minute),2)
        im_files = []
        rm_files = []
        
        for i in range(1):
                for j in range(24):
                    for k in range(0,46,15):
                        b = fillnull(now.year,4) + fillnull(now.month,2) + fillnull(now.day-i,2) + fillnull(fixhour(now.hour-2-j),2) + fillnull(previousmin(now.minute-k),2)
                        if int(b) <= int(a):
                            if os.path.isfile('cloud/'+b+'.jpg') == True:
                                if os.path.getsize('cloud/'+b+'.jpg') > 500:
                                    print "Black found"
                                    im_files.append('infra/'+b+'.jpg')
                                    rm_files.append('rain/'+b+'.jpg')
                                else:
                                    print "non found"
                                    im_files.append('infra/'+b+'.jpg')
                                    rm_files.append('rain/'+b+'.jpg')
    
                                    
        #im_files = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
        
#        im_files.sort()
        im_files.sort(key=lambda x: x.split("/", 2)[-1])
        
        rm_files.sort()
        newx = 600
        newy = 437
        for f in range(len(im_files)):
    
            img1 = cv.imread(im_files[f], 1)
            img2 = cv.imread(rm_files[f], 1)
            
            rows,cols,channels = img2.shape
            roi = img1[0:rows, 0:cols ]
            
            img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
    
            ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
            mask_inv = cv.bitwise_not(mask)
            
            img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
       
               # Take only region of logo from logo image.
            img2_fg = cv.bitwise_and(img2,img2,mask = mask)
               
            # Put logo in ROI and modify the main image
            dst = cv.add(img1_bg,img2_fg)
            img1[0:rows, 0:cols ] = dst
            
            cv.circle(img1,(495,265), 2, (0,0,255), -1)
    #        im = cv.resize(im,(newx,newy))
            cv.imshow('display', img1)
            cv.waitKey(20)
        cv.waitKey(1500)
    except:
        error_cnt += 1
        print str(error_cnt)+": Error occured"

cv.destroyAllWindows()

