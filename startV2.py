# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 00:57:31 2020

@author: user
"""

import numpy as np

subjects=np.array([['Maths','English','Kiswahili'],['pyshics','Biology','Chemistry'],['Geography','History','CRE'],['Agriculture','Business','Computer']])
subjectsNaNcategory=np.array(['Maths','English','Kiswahili','pyshics','Biology','Chemistry','Geography','History','CRE','Technicals'])
c=np.copy(subjects[0:1])
s=np.copy(subjects[1:2])
h=np.copy(subjects[2:3])
t=np.copy(subjects[3:4])

startTime=8
endTime=16
totalBreaks=80
timePerLesson=40
noOfPeriods=(((endTime-startTime)*60)-totalBreaks)/timePerLesson

timetable=np.empty([int(noOfPeriods),5], dtype=object)

doubleLessonsTaught=[]
LessonsDouble=[]
subjectTaken=[]

pickNo=int(2)
exhaustedCategory=10
m=0.3
n=0.3
o=0.2
p=0.2
while(True):
    if(pickNo==0):pickNo=2
    if(exhaustedCategory == 0):
        m=0
        n=0.4
        o=0.3
        p=0.3
    elif(exhaustedCategory==1):
        m=0.4
        n=0
        o=0.3
        p=0.3
    elif(exhaustedCategory==2):
        m=0.3
        n=0.4
        o=0
        p=0.3
    elif(exhaustedCategory==3):
        m=0.3
        n=0.4
        o=0.3
        p=0
        
    doublesCategory=np.array([0,1,2,3])
    doubleLessons=np.random.choice(doublesCategory,pickNo,replace=False, p=[m,n,o,p])
    
    for i in doubleLessons:
        if(i==3):
            LessonsDouble.append('Technicals')
        else:
            dlP=subjects[i][0]
            if(dlP not in subjectsNaNcategory):
                dlP=subjects[i][1]
                if(dlP not in subjectsNaNcategory):
                    dlP=subjects[i][2]
                    if(dlP not in subjectsNaNcategory):
                        pickNo=pickNo-1
                        exhaustedCategory=[i]
                    else:
                        LessonsDouble.append(dlP)
                else:
                    LessonsDouble.append(dlP)
            else:
                LessonsDouble.append(dlP)
    
    if(len(LessonsDouble)==2):
        break
print(LessonsDouble)   
#delete double lessons already taught from list
sciPick=2
humPick=2
for i in LessonsDouble:
    subjectsNaNcategory=np.delete(subjectsNaNcategory,np.where(subjectsNaNcategory==i), axis=0)
    #check if subject is a science or humanity
    if i in s:sciPick=sciPick-1
    if i in h:humPick=humPick-1
print(len(subjectsNaNcategory))    
    
#create a list of subject to be taught
#8 subjects daily
#3 compasary, 2 sciences, 2 humanities, 1 technical
#pick 2 sciences
q=0
r=0
b=0
alrPick=''
RandomSciences=[]
while(True):
    if(np.where(s==alrPick)==0):
        q=0
        r=0.5
        b=0.5
    elif(np.where(s==alrPick)==1):
        q=0.5
        r=0
        b=0.5
    elif(np.where(s==alrPick)==2):
        q=0.5
        r=0.5
        b=0
    #get a random subject and check if it does not exist in the double lesson or it has not been picked before
    looper=0
    if(q==0 and r==0 and b==0):
       while(looper<sciPick):
           if(looper==0):
               for i in (np.random.choice(subjects[1],1,replace="False")):
                   if(i not in LessonsDouble):
                       RandomSciences.append(i)
                       looper=looper+1
               
           else:
               for i in (np.random.choice(subjects[1],1,replace="False")):
                   if((i not in LessonsDouble) and (i not in RandomSciences)):
                       RandomSciences.append(i)
                       looper=looper+1

    else:
       while(looper<sciPick):
           if(looper==0):
               for i in (np.random.choice(subjects[1],1,replace="False",p=[q,r,b])):
                   if(i not in LessonsDouble):
                       RandomSciences.append(i)
                       looper=looper+1
               
           else:
               for i in (np.random.choice(subjects[1],1,replace="False",p=[q,r,b])):
                   if((i not in LessonsDouble) and (i not in RandomSciences)):
                       RandomSciences.append(i)
                       looper=looper+1
    if(sciPick==1):
        for i in LessonsDouble:
            if i in s:
                RandomSciences.append(i)
    alrPick=np.random.choice(np.array(RandomSciences).shape[0],1)
    
    break
print(RandomSciences)
#pick 2 Random humanities
c=0
u=0
v=0
halrPick=''
RandomHumanities=[]
while(True):
    if(np.where(s==alrPick)==0):
        c=0
        u=0.5
        v=0.5
    elif(np.where(s==alrPick)==1):
        c=0.5
        u=0
        v=0.5
    elif(np.where(s==alrPick)==2):
        c=0.5
        u=0.5
        v=0
    
    #get a random subject and check if it does not exist in the double lesson or it has not been picked before
    looper2=0
    if(c==0 and u==0 and v==0):
        while(looper2<humPick):
            if(looper==0):
                for i in (np.random.choice(subjects[2],1,replace="False")):
                    RandomHumanities.append(i)
                    looper2=looper2+1
            else:
                for i in (np.random.choice(subjects[2],1,replace="False")):
                    if((i not in LessonsDouble) and (i not in RandomHumanities)):
                        RandomHumanities.append(i)
                        looper2=looper2+1
    else:
        while(looper2<humPick):
            if(looper==0):
                for i in (np.random.choice(subjects[2],humPick,replace="False",p=[c,u,v])):
                    RandomHumanities.append(i)
                    looper2=looper2+1
            else:
                for i in (np.random.choice(subjects[2],humPick,replace="False",p=[c,u,v])):
                    if(i not in LessonsDouble and i not in RandomHumanities):
                        RandomHumanities.append(i)
                        looper2=looper2+1
    if(humPick==1):
        for i in LessonsDouble:
            if i in h:
                RandomHumanities.append(i)
    halrPick=np.random.choice(np.array(RandomSciences).shape[0],1)
    
    break
print(RandomHumanities)
subjectsDone=[]
p1_c_count=0
p1_c=np.array(['Maths']+RandomSciences)
cToday=np.array(['Maths','English','Kiswahili'])
sToday=np.array(RandomSciences)
hToday=np.array(RandomHumanities)
tToday=np.array(['Technicals'])
p1_c_done=[]
dayCount=0
periodCount=0
doubleJump=[]
print(p1_c)
while(periodCount<5):
    if(periodCount==0):
        #period 1
        subjectToday=np.array(cToday.tolist()+sToday.tolist())
        subjectTpick=np.random.choice(subjectToday,1)
        for i in subjectTpick:
            subjectTpick=i
        if(subjectTpick in LessonsDouble):
            timetable[periodCount][dayCount]=subjectTpick
            timetable[periodCount+1][dayCount]=subjectTpick
            subjectsDone.append(subjectTpick)
            periodCount=periodCount+2
            print(subjectTpick)
            print("line 229")
            if(subjectTpick in p1_c):
                p1_c_count=p1_c_count+1
                p1_c_done.append(subjectTpick)
        else:
            timetable[periodCount][dayCount]=subjectTpick
            subjectsDone.append(subjectTpick)
            periodCount=periodCount+1
            print(subjectTpick)
            print("line 238")
            if(subjectTpick in p1_c):
                p1_c_count=p1_c_count+1
                p1_c_done.append(subjectTpick)
    elif(periodCount==1):
        #period 2
        subjectToday=np.array(cToday.tolist()+sToday.tolist())
        for i in subjectsDone:
            subjectToday=np.delete(subjectToday,np.where(subjectToday==i), axis=0)
            
        subjectTpick=np.random.choice(subjectToday,1)
        for i in subjectTpick:
            subjectTpick=i
        while(True):
            if(subjectTpick in LessonsDouble):
                doubleJump.append(subjectTpick)
                subjectTpick=np.random.choice(subjectToday,1)
                for i in subjectTpick:
                    subjectTpick=i
                subjectsDone.append(subjectTpick)
            else:
                timetable[periodCount][dayCount]=subjectTpick
                subjectsDone.append(subjectTpick)
                periodCount=periodCount+1
                if(subjectTpick in p1_c):
                    p1_c_count=p1_c_count+1
                    p1_c_done.append(subjectTpick)
                break
    elif(periodCount==2):
        #period 3
        
        if(len(doubleJump)>0):
            subjectTpick=doubleJump.pop(0)
            timetable[periodCount][dayCount]=subjectTpick
            timetable[periodCount+1][dayCount]=subjectTpick
            periodCount=periodCount+2
            if(subjectTpick in p1_c):
                p1_c_count=p1_c_count+1
                p1_c_done.append(subjectTpick)
        else:
            subjectToday=np.array(cToday.tolist()+sToday.tolist())
            for i in subjectsDone:
                subjectToday=np.delete(subjectToday,np.where(subjectToday==i), axis=0)
            
            subjectTpick=np.random.choice(subjectToday,1)
            for i in subjectTpick:
                subjectTpick=i
            
            if(subjectTpick in LessonsDouble):
                timetable[periodCount][dayCount]=subjectTpick
                timetable[periodCount+1][dayCount]=subjectTpick
                subjectsDone.append(subjectTpick)
                periodCount=periodCount+2
                if(subjectTpick in p1_c):
                    p1_c_count=p1_c_count+1
                    p1_c_done.append(subjectTpick)
            else:
                timetable[periodCount][dayCount]=subjectTpick
                subjectsDone.append(subjectTpick)
                periodCount=periodCount+1
                if(subjectTpick in p1_c):
                    p1_c_count=p1_c_count+1
                    p1_c_done.append(subjectTpick)
    elif(periodCount==3):
        #period 4
        subjectToday=np.array(cToday.tolist()+sToday.tolist()+hToday.tolist())
        for i in subjectsDone:
            subjectToday=np.delete(subjectToday, np.where(subjectToday==i), axis=0)
        if(p1_c_count==1):
            subjectTpick=np.random.choice(np.delete(p1_c,np.where(p1_c==p1_c_done[0]),axis=0),1)
            for i in subjectTpick:
                subjectTpick=i
            countSet=0    
            while(True):
                if(subjectTpick in LessonsDouble):
                    doubleJump.append(subjectTpick)
                    subjectsDone.append(subjectTpick)
                    countSet=countSet+1
                    if(countSet<2):
                        subjectTpick=np.random.choice(np.setdiff1d(np.delete(p1_c,np.where(p1_c==subjectTpick),axis=0),np.delete(p1_c,np.where(p1_c==p1_c_done[0]),axis=0)),1)
                        for i in subjectTpick:
                            subjectTpick=i
                    else:
                        subjectTpick=np.random.choice(subjectToday,1)
                        for i in subjectTpick:
                            subjectTpick=i
                else:
                    timetable[periodCount][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+1
                    if(subjectTpick in p1_c):
                        p1_c_count=p1_c_count+1
                        p1_c_done.append(subjectTpick)
                    break
        elif(p1_c_count==2):
            subjectToday=np.array(cToday.tolist()+sToday.tolist()+hToday.tolist())
            for i in subjectsDone:
                subjectToday=np.delete(subjectToday, np.where(subjectToday==i), axis=0)
            for i in p1_c_done:
                subjectTpick=np.delete(p1_c,np.where(p1_c==i),axis=0)
                
            for i in p1_c:
                subjectTpick=i
            while(True):
                if(subjectTpick in LessonsDouble):
                    doubleJump.append(subjectTpick)
                    subjectsDone.append(subjectTpick)
                    subjectTpick=np.random.choice(subjectToday,1)
                    for i in subjectTpick:
                        subjectTpick=i
                else:
                    timetable[periodCount][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+1
                    if(subjectTpick in p1_c):
                        p1_c_count=p1_c_count+1
                        p1_c_done.append(subjectTpick)
                    break
        else:
            subjectToday=np.array(cToday.tolist()+sToday.tolist()+hToday.tolist())
            for i in subjectsDone:
                subjectToday=np.delete(subjectToday, np.where(subjectToday==i), axis=0)
                
            subjectTpick=np.random.choice(subjectToday,1)
            for i in subjectTpick:
                subjectTpick=i
            while(True):
                if(subjectTpick in LessonsDouble):
                    doubleJump.append(subjectTpick)
                    subjectsDone.append(subjectTpick)
                    subjectTpick=np.random.choice(subjectToday,1)
                    for i in subjectTpick:
                        subjectTpick=i
                else:
                    timetable[periodCount][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+1
                    break
    elif(periodCount==4):
        #period 5
        subjectToday=np.array(cToday.tolist()+sToday.tolist()+hToday.tolist())
        for i in subjectsDone:
            subjectToday=np.delete(subjectToday, np.where(subjectToday==i), axis=0)
        if(p1_c_count==1):
            subjectTpick=np.random.choice(np.delete(p1_c,np.where(p1_c==p1_c_done[0]),axis=0),1)
            for i in subjectTpick:
                subjectTpick=i
            countSet=0    
            while(True):
                if(subjectTpick in LessonsDouble):
                    doubleJump.append(subjectTpick)
                    subjectsDone.append(subjectTpick)
                    countSet=countSet+1
                    if(countSet<2):
                        subjectTpick=np.random.choice(np.setdiff1d(np.delete(p1_c,np.where(p1_c==subjectTpick),axis=0),np.delete(p1_c,np.where(p1_c==p1_c_done[0]),axis=0)),1)
                        for i in subjectTpick:
                            subjectTpick=i
                    else:
                        subjectTpick=np.random.choice(subjectToday,1)
                        for i in subjectTpick:
                            subjectTpick=i
                else:
                    timetable[periodCount][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+1
                    if(subjectTpick in p1_c):
                        p1_c_count=p1_c_count+1
                        p1_c_done.append(subjectTpick)
                    break
        elif(p1_c_count==2):
            for i in p1_c_done:
                subjectTpick=np.delete(p1_c,np.where(p1_c==i),axis=0)
                
            for i in p1_c:
                subjectTpick=i
            while(True):
                if(subjectTpick in LessonsDouble):
                    doubleJump.append(subjectTpick)
                    subjectsDone.append(subjectTpick)
                    subjectTpick=np.random.choice(subjectToday,1)
                    for i in subjectTpick:
                        subjectTpick=i
                else:
                    timetable[periodCount][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+1
                    if(subjectTpick in p1_c):
                        p1_c_count=p1_c_count+1
                        p1_c_done.append(subjectTpick)
                    break
        else:
            if(len(doubleJump)>0):
                subjectTpick=doubleJump.pop(0)
                timetable[periodCount][dayCount]=subjectTpick
                timetable[periodCount+1][dayCount]=subjectTpick
                periodCount=periodCount+2
            else:
                subjectToday=np.array(cToday.tolist()+sToday.tolist()+hToday.tolist())
                for i in subjectsDone:
                    subjectToday=np.delete(subjectToday, np.where(subjectToday==i), axis=0)
                
                subjectTpick=np.random.choice(subjectToday,1)
                for i in subjectTpick:
                    subjectTpick=i
                    
                if(subjectTpick in LessonsDouble):
                    timetable[periodCount][dayCount]=subjectTpick
                    timetable[periodCount+1][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+2
                else:
                    timetable[periodCount][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+1
print(timetable)
print(subjectsDone)
print(p1_c_done)
print(p1_c_count)
print(doubleJump)
   elif(periodCount==5):
        #period 6
        subjectToday=np.array(cToday.tolist()+sToday.tolist()+hToday.tolist()+tToday.tolist())
        for i in subjectsDone:
            subjectToday=np.delete(subjectToday, np.where(subjectToday==i), axis=0)
        if(p1_c_count==2):
            for i in p1_c_done:
                subjectTpick=np.delete(p1_c,np.where(p1_c==i),axis=0)
                
            for i in p1_c:
                subjectTpick=i
            while(True):
                if(subjectTpick in LessonsDouble):
                    doubleJump.append(subjectTpick)
                    subjectsDone.append(subjectTpick)
                    subjectTpick=np.random.choice(subjectToday,1)
                    for i in subjectTpick:
                        subjectTpick=i
                else:
                    timetable[periodCount][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+1
                    if(subjectTpick in p1_c):
                        p1_c_count=p1_c_count+1
                        p1_c_done.append(subjectTpick)
                    break
        else:
            if(len(doubleJump)>0):
                subjectTpick=doubleJump.pop(0)
                timetable[periodCount][dayCount]=subjectTpick
                timetable[periodCount+1][dayCount]=subjectTpick
                periodCount=periodCount+2
            else:
                subjectToday=np.array(cToday.tolist()+sToday.tolist()+hToday.tolist()+tToday.tolist())
                for i in subjectsDone:
                    subjectToday=np.delete(subjectToday, np.where(subjectToday==i), axis=0)
                
                subjectTpick=np.random.choice(subjectToday,1)
                for i in subjectTpick:
                    subjectTpick=i
                
                if(subjectTpick in LessonsDouble):
                    timetable[periodCount][dayCount]=subjectTpick
                    timetable[periodCount+1][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+2
                else:
                    timetable[periodCount][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+1
    elif(periodCount==6):
        #period 7
        subjectToday=np.array(hToday.tolist()+tToday.tolist())
        for i in subjectsDone:
            subjectToday=np.delete(subjectToday, np.where(subjectToday==i), axis=0)
            
        subjectTpick=np.random.choice(subjectToday,1)
        for i in subjectTpick:
            subjectTpick=i
            
        while(True):
            if(subjectTpick in LessonsDouble):
                doubleJump.append(subjectTpick)
                subjectsDone.append(subjectTpick)
                subjectTpick=np.random.choice(subjectToday,1)
            else:
                timetable[periodCount][dayCount]=subjectTpick
                subjectsDone.append(subjectTpick)
                periodCount=periodCount+1
                break
    elif(periodCount==7):
        #period 8
        if(len(doubleJump)>0):
            subjectTpick=doubleJump.pop(0)
            timetable[periodCount][dayCount]=subjectTpick
            timetable[periodCount+1][dayCount]=subjectTpick
            periodCount=periodCount+2
        else:
            subjectToday=np.array(hToday.tolist()+tToday.tolist())
            for i in subjectsDone:
                subjectToday=np.delete(subjectToday, np.where(subjectToday==i), axis=0)
            if(subjectToday.size !=0):
                subjectTpick=np.random.choice(subjectToday,1)
                for i in subjectTpick:
                    subjectTpick=i
                
                if(subjectTpick in LessonsDouble):
                    timetable[periodCount][dayCount]=subjectTpick
                    timetable[periodCount+1][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+2
                else:
                    timetable[periodCount][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+1
            else:
               periodCount=periodCount+1 
    elif(periodCount==8):
        #period 9
        if(len(doubleJump)>0):
            subjectTpick=doubleJump.pop(0)
            timetable[periodCount][dayCount]=subjectTpick
            timetable[periodCount+1][dayCount]=subjectTpick
            periodCount=periodCount+2
        else:
            subjectToday=np.array(hToday.tolist()+tToday.tolist())
            for i in subjectsDone:
                subjectToday=np.delete(subjectToday, np.where(subjectToday==i), axis=0)
            if(subjectToday.size !=0):
                subjectTpick=np.random.choice(subjectToday,1)
                for i in subjectTpick:
                    subjectTpick=i
                
                if(subjectTpick in LessonsDouble):
                    timetable[periodCount][dayCount]=subjectTpick
                    timetable[periodCount+1][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+2
                else:
                    timetable[periodCount][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+1
            else:
                periodCount=periodCount+2
    elif(periodCount==9):
        #period 10
        subjectToday=np.array(hToday.tolist()+tToday.tolist())
        for i in subjectsDone:
            subjectToday=np.delete(subjectToday, np.where(subjectToday==i), axis=0)
        if(subjectToday.size !=0):    
            subjectTpick=np.random.choice(subjectToday,1)
            for i in subjectTpick:
                subjectTpick=i
            while(True):
                if(subjectTpick in LessonsDouble):
                    doubleJump.append(subjectTpick)
                    subjectsDone.append(subjectTpick)
                    subjectTpick=np.random.choice(subjectToday,1)
                    for i in subjectTpick:
                        subjectTpick=i
                else:
                    timetable[periodCount][dayCount]=subjectTpick
                    subjectsDone.append(subjectTpick)
                    periodCount=periodCount+1
                    break
        else:
            periodCount=periodCount+1
print(timetable)      
