#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.02), January 19, 2015, at 23:58
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import csv

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Self_Other'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
#setup files for saving
#if not os.path.isdir('behav_data'+os.path.sep+'pylog'):
#    os.makedirs('behav_data'+os.path.sep+'pylog') #if this fails (e.g. permissions) we will get error
#filename='behav_data'+os.path.sep+'pylog' + os.path.sep + '%s_%s_run%s_%s' %(expInfo['expName'],expInfo['participant'],expInfo['Run'], expInfo['date'])
#logFile=logging.LogFile(filename+'.log', level=logging.DEBUG)
#logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1024, 760), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess
    

#stim file names
stimFiles=np.loadtxt('stim_files/%s_block_list%s.txt'%(expInfo['participant'],expInfo['session']),dtype='str',delimiter='\t') 


# Initialize components for Routine "instruction"
instructionClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'Listen to the sentences and answer the question regarding the last sentence you hear in each block. \n\nIn the silent blocks, you will be asked a real-world question. \n\nTo answer, respond YES with your point finger or NO with your middle finger. ',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trigger"
triggerClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'Waiting for the scanner...',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "blockS1"
blockS1Clock = core.Clock()
sound_6 = sound.Sound(stimFiles[0,0], secs=stimFiles[0,1])   ###########create text file for all stims and change the numbers in the  [  ]
sound_6.setVolume(1)
ISI_6 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_6')
sound_7 = sound.Sound(stimFiles[1,0], secs=stimFiles[1,1])
sound_7.setVolume(1)
ISI_7 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_7')
sound_8 = sound.Sound(stimFiles[2,0], secs=stimFiles[2,1])
sound_8.setVolume(1)
ISI_8 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_8')
sound_9 = sound.Sound(stimFiles[3,0], secs=stimFiles[3,1])
sound_9.setVolume(1)
ISI_9 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_9')
sound_10 = sound.Sound(stimFiles[4,0], secs=stimFiles[4,1])
sound_10.setVolume(1)
ISI_10 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_10')
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "compQ1"
compQ1Clock = core.Clock()
image_2 = visual.ImageStim(win=win, name='image_2',
    image=stimFiles[0,3], mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blockS2"
blockS2Clock = core.Clock()
sound_11 = sound.Sound(stimFiles[5,0], secs=stimFiles[5,1])
sound_11.setVolume(1)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
sound_12 = sound.Sound(stimFiles[6,0], secs=stimFiles[6,1])
sound_12.setVolume(1)
ISI_11 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_11')
sound_13 = sound.Sound(stimFiles[7,0], secs=stimFiles[7,1])
ISI_12 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_12')
sound_14 = sound.Sound(stimFiles[8,0], secs=stimFiles[8,1])
sound_14.setVolume(1)
ISI_13 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_13')
sound_15 = sound.Sound(stimFiles[9,0], secs=stimFiles[9,1])
sound_15.setVolume(1)
ISI_14 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_14')
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "compQ2"
compQ2Clock = core.Clock()
image_3 = visual.ImageStim(win=win, name='image_3',
    image=stimFiles[1,3], mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "compQS1"
compQS1Clock = core.Clock()
image_8 = visual.ImageStim(win=win, name='image_8',
    image=stimFiles[2,3], mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blockO1"
blockO1Clock = core.Clock()
sound_26 = sound.Sound(stimFiles[10,0], secs=stimFiles[10,1])
sound_26.setVolume(1)
ISI_23 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_23')
sound_27 = sound.Sound(stimFiles[11,0], secs=stimFiles[11,1])
sound_27.setVolume(1)
ISI_24 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_24')
sound_28 = sound.Sound(stimFiles[12,0], secs=stimFiles[12,1])
sound_28.setVolume(1)
ISI_25 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_25')
sound_29 = sound.Sound(stimFiles[13,0], secs=stimFiles[13,1])
sound_29.setVolume(1)
ISI_26 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_26')
sound_30 = sound.Sound(stimFiles[14,0], secs=stimFiles[14,1])
sound_30.setVolume(1)
ISI_27 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_27')
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "compQ3"
compQ3Clock = core.Clock()
image_4 = visual.ImageStim(win=win, name='image_4',
    image=stimFiles[3,3], mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blockO2"
blockO2Clock = core.Clock()
sound_31 = sound.Sound(stimFiles[15,0], secs=stimFiles[15,1])
sound_31.setVolume(1)
ISI_28 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_28')
sound_32 = sound.Sound(stimFiles[16,0], secs=stimFiles[16,1])
sound_32.setVolume(1)
ISI_29 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_29')
sound_33 = sound.Sound(stimFiles[17,0], secs=stimFiles[17,1])
sound_33.setVolume(1)
ISI_30 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_30')
sound_34 = sound.Sound(stimFiles[18,0], secs=stimFiles[18,1])
sound_34.setVolume(1)
ISI_31 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_31')
sound_35 = sound.Sound(stimFiles[19,0], secs=stimFiles[19,1])
sound_35.setVolume(1)
ISI_32 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_32')
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "compQ4"
compQ4Clock = core.Clock()
image_5 = visual.ImageStim(win=win, name='image_5',
    image=stimFiles[4,3], mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "compQS2"
compQS2Clock = core.Clock()
image_9 = visual.ImageStim(win=win, name='image_9',
    image=stimFiles[5,3], mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blockS3"
blockS3Clock = core.Clock()
sound_16 = sound.Sound(stimFiles[20,0], secs=stimFiles[20,1])
sound_16.setVolume(1)
ISI_2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')
sound_17 = sound.Sound(stimFiles[21,0], secs=stimFiles[21,1])
sound_17.setVolume(1)
ISI_15 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_15')
sound_18 = sound.Sound(stimFiles[22,0], secs=stimFiles[22,1])
sound_18.setVolume(1)
ISI_16 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_16')
sound_19 = sound.Sound(stimFiles[23,0], secs=stimFiles[23,1])
sound_19.setVolume(1)
ISI_17 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_17')
sound_20 = sound.Sound(stimFiles[24,0], secs=stimFiles[24,1])
sound_20.setVolume(1)
ISI_18 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_18')
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "compQ5"
compQ5Clock = core.Clock()
image_6 = visual.ImageStim(win=win, name='image_6',
    image=stimFiles[6,3], mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "compQS3"
compQS3Clock = core.Clock()
image_10 = visual.ImageStim(win=win, name='image_10',
    image=stimFiles[7,3], mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blockS4"
blockS4Clock = core.Clock()
sound_21 = sound.Sound(stimFiles[25,0], secs=stimFiles[25,1])
sound_21.setVolume(1)
ISI_3 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_3')
sound_22 = sound.Sound(stimFiles[26,0], secs=stimFiles[26,1])
sound_22.setVolume(1)
ISI_19 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_19')
sound_23 = sound.Sound(stimFiles[27,0], secs=stimFiles[27,1])
sound_23.setVolume(1)
ISI_20 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_20')
sound_24 = sound.Sound(stimFiles[28,0], secs=stimFiles[28,1])
sound_24.setVolume(1)
ISI_21 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_21')
sound_25 = sound.Sound(stimFiles[29,0], secs=stimFiles[29,1])
sound_25.setVolume(1)
ISI_22 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_22')
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "compQ6"
compQ6Clock = core.Clock()
image_7 = visual.ImageStim(win=win, name='image_7',
    image=stimFiles[8,3], mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blockO3"
blockO3Clock = core.Clock()
sound_36 = sound.Sound(stimFiles[30,0], secs=stimFiles[30,1])
sound_36.setVolume(1)
ISI_33 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_33')
sound_37 = sound.Sound(stimFiles[31,0], secs=stimFiles[31,1])
sound_37.setVolume(1)
ISI_34 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_34')
sound_38 = sound.Sound(stimFiles[32,0], secs=stimFiles[32,1])
sound_38.setVolume(1)
ISI_35 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_35')
sound_39 = sound.Sound(stimFiles[33,0], secs=stimFiles[33,1])
sound_39.setVolume(1)
ISI_36 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_36')
sound_40 = sound.Sound(stimFiles[34,0], secs=stimFiles[34,1])
sound_40.setVolume(1)
ISI_37 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_37')
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "compQ7"
compQ7Clock = core.Clock()
image_12 = visual.ImageStim(win=win, name='image_12',
    image=stimFiles[9,3], mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blockO4"
blockO4Clock = core.Clock()
sound_41 = sound.Sound(stimFiles[35,0], secs=stimFiles[35,1])
sound_41.setVolume(1)
ISI_38 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_38')
sound_42 = sound.Sound(stimFiles[36,0], secs=stimFiles[36,1])
sound_42.setVolume(1)
ISI_39 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_39')
sound_43 = sound.Sound(stimFiles[37,0], secs=stimFiles[37,1])
sound_43.setVolume(1)
ISI_40 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_40')
sound_44 = sound.Sound(stimFiles[38,0], secs=stimFiles[38,1])
sound_44.setVolume(1)
ISI_41 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_41')
sound_45 = sound.Sound(stimFiles[39,0], secs=stimFiles[39,1])
sound_45.setVolume(1)
ISI_42 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_42')
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Initialize components for Routine "compQ8"
compQ8Clock = core.Clock()
image_13 = visual.ImageStim(win=win, name='image_13',
    image=stimFiles[10,3], mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "compQS4"
compQS4Clock = core.Clock()
image_11 = visual.ImageStim(win=win, name='image_11',
    image=stimFiles[10,3], mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instructionComponents = []
instructionComponents.append(text)
instructionComponents.append(key_resp_2)
for thisComponent in instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instruction"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()

#------Prepare to start Routine "trigger"-------
t = 0
triggerClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
triggerComponents = []
triggerComponents.append(text_2)
triggerComponents.append(key_resp_3)
for thisComponent in triggerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "trigger"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = triggerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['+', 'num_add','t'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "trigger"-------
for thisComponent in triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
   key_resp_3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()

#------Prepare to start Routine "blockS1"-------
t = 0
blockS1Clock.reset()  # clock 
frameN = -1
routineTimer.add(16.000000)
# update component parameters for each repeat
# keep track of which components have finished
blockS1Components = []
blockS1Components.append(sound_6)
blockS1Components.append(ISI_6)
blockS1Components.append(sound_7)
blockS1Components.append(ISI_7)
blockS1Components.append(sound_8)
blockS1Components.append(ISI_8)
blockS1Components.append(sound_9)
blockS1Components.append(ISI_9)
blockS1Components.append(sound_10)
blockS1Components.append(ISI_10)
blockS1Components.append(text_4)
for thisComponent in blockS1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "blockS1"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blockS1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_6
    if t >= 0.0 and sound_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_6.tStart = t  # underestimates by a little under one frame
        sound_6.frameNStart = frameN  # exact frame index
        sound_6.play()  # start the sound (it finishes automatically)
    elif sound_6.status == STARTED and t >= (0.0 + (float(stimFiles[0,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_6.stop()  # stop the sound (if longer than duration)
    # start/stop sound_7
    if t >= (float(stimFiles[0,1])+float(stimFiles[0,2])) and sound_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_7.tStart = t  # underestimates by a little under one frame
        sound_7.frameNStart = frameN  # exact frame index
        sound_7.play()  # start the sound (it finishes automatically)
    elif sound_7.status == STARTED and t >= ((float(stimFiles[0,1])+float(stimFiles[0,2]))+ (float(stimFiles[1,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_7.stop()  # stop the sound (if longer than duration)
    # start/stop sound_8
    if t >= (float(stimFiles[0,1])+float(stimFiles[0,2])+float(stimFiles[1,1])+float(stimFiles[1,2])) and sound_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_8.tStart = t  # underestimates by a little under one frame
        sound_8.frameNStart = frameN  # exact frame index
        sound_8.play()  # start the sound (it finishes automatically)
    elif sound_8.status == STARTED and t >= ((float(stimFiles[0,1])+float(stimFiles[0,2])+float(stimFiles[1,1])+float(stimFiles[1,2])) + (float(stimFiles[2,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_8.stop()  # stop the sound (if longer than duration)
    # start/stop sound_9
    if t >= (float(stimFiles[0,1])+float(stimFiles[0,2])+float(stimFiles[1,1])+float(stimFiles[1,2])+float(stimFiles[2,1])+float(stimFiles[2,2])) and sound_9.status == NOT_STARTED:
        # keep track of start time/frame for later 
        sound_9.tStart = t  # underestimates by a little under one frame
        sound_9.frameNStart = frameN  # exact frame index
        sound_9.play()  # start the sound (it finishes automatically)
    elif sound_9.status == STARTED and t >= ((float(stimFiles[0,1])+float(stimFiles[0,2])+float(stimFiles[1,1])+float(stimFiles[1,2])+float(stimFiles[2,1])+float(stimFiles[2,2])) + (float(stimFiles[3,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_9.stop()  # stop the sound (if longer than duration)
    # start/stop sound_10
    if t >= (float(stimFiles[0,1])+float(stimFiles[0,2])+float(stimFiles[1,1])+float(stimFiles[1,2])+float(stimFiles[2,1])+float(stimFiles[2,2])+float(stimFiles[3,1])+float(stimFiles[3,2])) and sound_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_10.tStart = t  # underestimates by a little under one frame
        sound_10.frameNStart = frameN  # exact frame index
        sound_10.play()  # start the sound (it finishes automatically)
    elif sound_10.status == STARTED and t >= ((float(stimFiles[0,1])+float(stimFiles[0,2])+float(stimFiles[1,1])+float(stimFiles[1,2])+float(stimFiles[2,1])+float(stimFiles[2,2])+float(stimFiles[3,1])+float(stimFiles[3,2])) + (float(stimFiles[4,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_10.stop()  # stop the sound (if longer than duration)
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    elif text_4.status == STARTED and t >= (0.0 + (16-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_4.setAutoDraw(False)
    # *ISI_6* period
    if t >= float(stimFiles[0,1]) and ISI_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_6.tStart = t  # underestimates by a little under one frame
        ISI_6.frameNStart = frameN  # exact frame index
        ISI_6.start(float(stimFiles[0,2]))
    elif ISI_6.status == STARTED: #one frame should pass before updating params and completing
        ISI_6.complete() #finish the static period
    # *ISI_7* period
    if t >= (float(stimFiles[0,1])+float(stimFiles[0,2])+float(stimFiles[1,1])) and ISI_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_7.tStart = t  # underestimates by a little under one frame
        ISI_7.frameNStart = frameN  # exact frame index
        ISI_7.start(float(stimFiles[1,2]))
    elif ISI_7.status == STARTED: #one frame should pass before updating params and completing
        ISI_7.complete() #finish the static period
    # *ISI_8* period
    if t >= (float(stimFiles[0,1])+float(stimFiles[0,2])+float(stimFiles[1,1])+float(stimFiles[1,2])+float(stimFiles[2,1])) and ISI_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_8.tStart = t  # underestimates by a little under one frame
        ISI_8.frameNStart = frameN  # exact frame index
        ISI_8.start(float(stimFiles[2,2]))
    elif ISI_8.status == STARTED: #one frame should pass before updating params and completing
        ISI_8.complete() #finish the static period
    # *ISI_9* period
    if t >= (float(stimFiles[0,1])+float(stimFiles[0,2])+float(stimFiles[1,1])+float(stimFiles[1,2])+float(stimFiles[2,1])+float(stimFiles[2,2])+float(stimFiles[3,1])) and ISI_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_9.tStart = t  # underestimates by a little under one frame
        ISI_9.frameNStart = frameN  # exact frame index
        ISI_9.start(float(stimFiles[3,2]))
    elif ISI_9.status == STARTED: #one frame should pass before updating params and completing
        ISI_9.complete() #finish the static period
    # *ISI_10* period
    if t >= (float(stimFiles[0,1])+float(stimFiles[0,2])+float(stimFiles[1,1])+float(stimFiles[1,2])+float(stimFiles[2,1])+float(stimFiles[2,2])+float(stimFiles[3,1])+float(stimFiles[3,2])+float(stimFiles[4,1])) and ISI_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_10.tStart = t  # underestimates by a little under one frame
        ISI_10.frameNStart = frameN  # exact frame index
        ISI_10.start(float(stimFiles[4,2]))
    elif ISI_10.status == STARTED: #one frame should pass before updating params and completing
        ISI_10.complete() #finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockS1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "blockS1"-------
for thisComponent in blockS1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "compQ1"-------
t = 0
compQ1Clock.reset()  # clock 
frameN = -1
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
compQ1Components = []
compQ1Components.append(image_2)
for thisComponent in compQ1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "compQ1"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = compQ1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if t >= 0.0 and image_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_2.tStart = t  # underestimates by a little under one frame
        image_2.frameNStart = frameN  # exact frame index
        image_2.setAutoDraw(True)
    elif image_2.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in compQ1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "compQ1"-------
for thisComponent in compQ1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "blockS2"-------
t = 0
blockS2Clock.reset()  # clock 
frameN = -1
routineTimer.add(16.000000)
# update component parameters for each repeat
# keep track of which components have finished
blockS2Components = []
blockS2Components.append(sound_11)
blockS2Components.append(ISI)
blockS2Components.append(sound_12)
blockS2Components.append(ISI_11)
blockS2Components.append(sound_13)
blockS2Components.append(ISI_12)
blockS2Components.append(sound_14)
blockS2Components.append(ISI_13)
blockS2Components.append(sound_15)
blockS2Components.append(ISI_14)
blockS2Components.append(text_5)
for thisComponent in blockS2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "blockS2"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blockS2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_11
    if t >= 0.0 and sound_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_11.tStart = t  # underestimates by a little under one frame
        sound_11.frameNStart = frameN  # exact frame index
        sound_11.play()  # start the sound (it finishes automatically)
    elif sound_11.status == STARTED and t >= (0.0 + (float(stimFiles[5,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_11.stop()  # stop the sound (if longer than duration)
    # start/stop sound_12
    if t >= (float(stimFiles[5,1])+float(stimFiles[5,2])) and sound_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_12.tStart = t  # underestimates by a little under one frame
        sound_12.frameNStart = frameN  # exact frame index
        sound_12.play()  # start the sound (it finishes automatically)
    elif sound_12.status == STARTED and t >= ((float(stimFiles[5,1])+float(stimFiles[5,2]))+ (float(stimFiles[6,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_12.stop()  # stop the sound (if longer than duration)
    # start/stop sound_13
    if t >= (float(stimFiles[5,1])+float(stimFiles[5,2])+float(stimFiles[6,1])+float(stimFiles[6,2])) and sound_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_13.tStart = t  # underestimates by a little under one frame
        sound_13.frameNStart = frameN  # exact frame index
        sound_13.play()  # start the sound (it finishes automatically)
    elif sound_13.status == STARTED and t >= ((float(stimFiles[5,1])+float(stimFiles[5,2])+float(stimFiles[6,1])+float(stimFiles[6,2])) + (float(stimFiles[7,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_13.stop()  # stop the sound (if longer than duration)
    # start/stop sound_14
    if t >= (float(stimFiles[5,1])+float(stimFiles[5,2])+float(stimFiles[6,1])+float(stimFiles[6,2])+float(stimFiles[7,1])+float(stimFiles[7,2])) and sound_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_14.tStart = t  # underestimates by a little under one frame
        sound_14.frameNStart = frameN  # exact frame index
        sound_14.play()  # start the sound (it finishes automatically)
    elif sound_14.status == STARTED and t >= ((float(stimFiles[5,1])+float(stimFiles[5,2])+float(stimFiles[6,1])+float(stimFiles[6,2])+float(stimFiles[7,1])+float(stimFiles[7,2])) + (float(stimFiles[8,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_14.stop()  # stop the sound (if longer than duration)
    # start/stop sound_15
    if t >= (float(stimFiles[5,1])+float(stimFiles[5,2])+float(stimFiles[6,1])+float(stimFiles[6,2])+float(stimFiles[7,1])+float(stimFiles[7,2])+float(stimFiles[8,1])+float(stimFiles[8,2])) and sound_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_15.tStart = t  # underestimates by a little under one frame
        sound_15.frameNStart = frameN  # exact frame index
        sound_15.play()  # start the sound (it finishes automatically)
    elif sound_15.status == STARTED and t >= ((float(stimFiles[5,1])+float(stimFiles[5,2])+float(stimFiles[6,1])+float(stimFiles[6,2])+float(stimFiles[7,1])+float(stimFiles[7,2])+float(stimFiles[8,1])+float(stimFiles[8,2])) + (float(stimFiles[9,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_15.stop()  # stop the sound (if longer than duration)
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    elif text_5.status == STARTED and t >= (0.0 + (16-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_5.setAutoDraw(False)
    # *ISI* period
    if t >= float(stimFiles[5,1]) and ISI.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI.tStart = t  # underestimates by a little under one frame
        ISI.frameNStart = frameN  # exact frame index
        ISI.start(float(stimFiles[5,2]))
    elif ISI.status == STARTED: #one frame should pass before updating params and completing
        ISI.complete() #finish the static period
    # *ISI_11* period
    if t >= (float(stimFiles[5,1])+float(stimFiles[5,2])+float(stimFiles[6,1])) and ISI_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_11.tStart = t  # underestimates by a little under one frame
        ISI_11.frameNStart = frameN  # exact frame index
        ISI_11.start(float(stimFiles[6,2]))
    elif ISI_11.status == STARTED: #one frame should pass before updating params and completing
        ISI_11.complete() #finish the static period
    # *ISI_12* period
    if t >= (float(stimFiles[5,1])+float(stimFiles[5,2])+float(stimFiles[6,1])+float(stimFiles[6,2])+float(stimFiles[7,1])) and ISI_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_12.tStart = t  # underestimates by a little under one frame
        ISI_12.frameNStart = frameN  # exact frame index
        ISI_12.start(float(stimFiles[7,2]))
    elif ISI_12.status == STARTED: #one frame should pass before updating params and completing
        ISI_12.complete() #finish the static period
    # *ISI_13* period
    if t >= (float(stimFiles[5,1])+float(stimFiles[5,2])+float(stimFiles[6,1])+float(stimFiles[6,2])+float(stimFiles[7,1])+float(stimFiles[7,2])+float(stimFiles[8,1])) and ISI_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_13.tStart = t  # underestimates by a little under one frame
        ISI_13.frameNStart = frameN  # exact frame index
        ISI_13.start(float(stimFiles[8,2]))
    elif ISI_13.status == STARTED: #one frame should pass before updating params and completing
        ISI_13.complete() #finish the static period
    # *ISI_14* period
    if t >= (float(stimFiles[5,1])+float(stimFiles[5,2])+float(stimFiles[6,1])+float(stimFiles[6,2])+float(stimFiles[7,1])+float(stimFiles[7,2])+float(stimFiles[8,1])+float(stimFiles[8,2])+float(stimFiles[9,1])) and ISI_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_14.tStart = t  # underestimates by a little under one frame
        ISI_14.frameNStart = frameN  # exact frame index
        ISI_14.start(float(stimFiles[9,2]))
    elif ISI_14.status == STARTED: #one frame should pass before updating params and completing
        ISI_14.complete() #finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockS2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "blockS2"-------
for thisComponent in blockS2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "compQ2"-------
t = 0
compQ2Clock.reset()  # clock 
frameN = -1
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
compQ2Components = []
compQ2Components.append(image_3)
for thisComponent in compQ2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "compQ2"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = compQ2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if t >= 0.0 and image_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_3.tStart = t  # underestimates by a little under one frame
        image_3.frameNStart = frameN  # exact frame index
        image_3.setAutoDraw(True)
    elif image_3.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in compQ2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "compQ2"-------
for thisComponent in compQ2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(16.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_11)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if t >= 0.0 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t  # underestimates by a little under one frame
        text_11.frameNStart = frameN  # exact frame index
        text_11.setAutoDraw(True)
    elif text_11.status == STARTED and t >= (0.0 + (16-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_11.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "compQS1"-------
t = 0
compQS1Clock.reset()  # clock 
frameN = -1
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
compQS1Components = []
compQS1Components.append(image_8)
for thisComponent in compQS1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "compQS1"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = compQS1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_8* updates
    if t >= 0.0 and image_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_8.tStart = t  # underestimates by a little under one frame
        image_8.frameNStart = frameN  # exact frame index
        image_8.setAutoDraw(True)
    elif image_8.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_8.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in compQS1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "compQS1"-------
for thisComponent in compQS1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "blockO1"-------
t = 0
blockO1Clock.reset()  # clock 
frameN = -1
routineTimer.add(16.000000)
# update component parameters for each repeat
# keep track of which components have finished
blockO1Components = []
blockO1Components.append(sound_26)
blockO1Components.append(ISI_23)
blockO1Components.append(sound_27)
blockO1Components.append(ISI_24)
blockO1Components.append(sound_28)
blockO1Components.append(ISI_25)
blockO1Components.append(sound_29)
blockO1Components.append(ISI_26)
blockO1Components.append(sound_30)
blockO1Components.append(ISI_27)
blockO1Components.append(text_3)
for thisComponent in blockO1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "blockO1"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blockO1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_26
    if t >= 0.0 and sound_26.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_26.tStart = t  # underestimates by a little under one frame
        sound_26.frameNStart = frameN  # exact frame index
        sound_26.play()  # start the sound (it finishes automatically)
    elif sound_26.status == STARTED and t >= (0.0 + (float(stimFiles[10,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_26.stop()  # stop the sound (if longer than duration)
    # start/stop sound_27
    if t >= (float(stimFiles[10,1])+float(stimFiles[10,2])) and sound_27.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_27.tStart = t  # underestimates by a little under one frame
        sound_27.frameNStart = frameN  # exact frame index
        sound_27.play()  # start the sound (it finishes automatically)
    elif sound_27.status == STARTED and t >= ((float(stimFiles[10,1])+float(stimFiles[10,2]))+ (float(stimFiles[11,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_27.stop()  # stop the sound (if longer than duration)
    # start/stop sound_28
    if t >= (float(stimFiles[10,1])+float(stimFiles[10,2])+float(stimFiles[11,1])+float(stimFiles[11,2])) and sound_28.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_28.tStart = t  # underestimates by a little under one frame
        sound_28.frameNStart = frameN  # exact frame index
        sound_28.play()  # start the sound (it finishes automatically)
    elif sound_28.status == STARTED and t >= ((float(stimFiles[10,1])+float(stimFiles[10,2])+float(stimFiles[11,1])+float(stimFiles[11,2])) + (float(stimFiles[12,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_28.stop()  # stop the sound (if longer than duration)
    # start/stop sound_29
    if t >= (float(stimFiles[10,1])+float(stimFiles[10,2])+float(stimFiles[11,1])+float(stimFiles[11,2])+float(stimFiles[12,1])+float(stimFiles[12,2])) and sound_29.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_29.tStart = t  # underestimates by a little under one frame
        sound_29.frameNStart = frameN  # exact frame index
        sound_29.play()  # start the sound (it finishes automatically)
    elif sound_29.status == STARTED and t >= ((float(stimFiles[10,1])+float(stimFiles[10,2])+float(stimFiles[11,1])+float(stimFiles[11,2])+float(stimFiles[12,1])+float(stimFiles[12,2])) + (float(stimFiles[13,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_29.stop()  # stop the sound (if longer than duration)
    # start/stop sound_30
    if t >= (float(stimFiles[10,1])+float(stimFiles[10,2])+float(stimFiles[11,1])+float(stimFiles[11,2])+float(stimFiles[12,1])+float(stimFiles[12,2])+float(stimFiles[13,1])+float(stimFiles[13,2])) and sound_30.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_30.tStart = t  # underestimates by a little under one frame
        sound_30.frameNStart = frameN  # exact frame index
        sound_30.play()  # start the sound (it finishes automatically)
    elif sound_30.status == STARTED and t >= ((float(stimFiles[10,1])+float(stimFiles[10,2])+float(stimFiles[11,1])+float(stimFiles[11,2])+float(stimFiles[12,1])+float(stimFiles[12,2])+float(stimFiles[13,1])+float(stimFiles[13,2])) + (float(stimFiles[14,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_30.stop()  # stop the sound (if longer than duration)
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    elif text_3.status == STARTED and t >= (0.0 + (16-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_3.setAutoDraw(False)
    # *ISI_23* period
    if t >= float(stimFiles[10,1]) and ISI_23.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_23.tStart = t  # underestimates by a little under one frame
        ISI_23.frameNStart = frameN  # exact frame index
        ISI_23.start(float(stimFiles[10,2]))
    elif ISI_23.status == STARTED: #one frame should pass before updating params and completing
        ISI_23.complete() #finish the static period
    # *ISI_24* period
    if t >= (float(stimFiles[10,1])+float(stimFiles[10,2])+float(stimFiles[11,1])) and ISI_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_24.tStart = t  # underestimates by a little under one frame
        ISI_24.frameNStart = frameN  # exact frame index
        ISI_24.start(float(stimFiles[11,2]))
    elif ISI_24.status == STARTED: #one frame should pass before updating params and completing
        ISI_24.complete() #finish the static period
    # *ISI_25* period
    if t >= (float(stimFiles[10,1])+float(stimFiles[10,2])+float(stimFiles[11,1])+float(stimFiles[11,2])+float(stimFiles[12,1])) and ISI_25.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_25.tStart = t  # underestimates by a little under one frame
        ISI_25.frameNStart = frameN  # exact frame index
        ISI_25.start(float(stimFiles[12,2]))
    elif ISI_25.status == STARTED: #one frame should pass before updating params and completing
        ISI_25.complete() #finish the static period
    # *ISI_26* period
    if t >= (float(stimFiles[10,1])+float(stimFiles[10,2])+float(stimFiles[11,1])+float(stimFiles[11,2])+float(stimFiles[12,1])+float(stimFiles[12,2])+float(stimFiles[13,1])) and ISI_26.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_26.tStart = t  # underestimates by a little under one frame
        ISI_26.frameNStart = frameN  # exact frame index
        ISI_26.start(float(stimFiles[13,2]))
    elif ISI_26.status == STARTED: #one frame should pass before updating params and completing
        ISI_26.complete() #finish the static period
    # *ISI_27* period
    if t >= (float(stimFiles[10,1])+float(stimFiles[10,2])+float(stimFiles[11,1])+float(stimFiles[11,2])+float(stimFiles[12,1])+float(stimFiles[12,2])+float(stimFiles[13,1])+float(stimFiles[13,2])+float(stimFiles[14,1])) and ISI_27.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_27.tStart = t  # underestimates by a little under one frame
        ISI_27.frameNStart = frameN  # exact frame index
        ISI_27.start(float(stimFiles[14,2]))
    elif ISI_27.status == STARTED: #one frame should pass before updating params and completing
        ISI_27.complete() #finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockO1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "blockO1"-------
for thisComponent in blockO1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "compQ3"-------
t = 0
compQ3Clock.reset()  # clock 
frameN = -1
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
compQ3Components = []
compQ3Components.append(image_4)
for thisComponent in compQ3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "compQ3"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = compQ3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if t >= 0.0 and image_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_4.tStart = t  # underestimates by a little under one frame
        image_4.frameNStart = frameN  # exact frame index
        image_4.setAutoDraw(True)
    elif image_4.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_4.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in compQ3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "compQ3"-------
for thisComponent in compQ3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "blockO2"-------
t = 0
blockO2Clock.reset()  # clock 
frameN = -1
routineTimer.add(16.000000)
# update component parameters for each repeat
# keep track of which components have finished
blockO2Components = []
blockO2Components.append(sound_31)
blockO2Components.append(ISI_28)
blockO2Components.append(sound_32)
blockO2Components.append(ISI_29)
blockO2Components.append(sound_33)
blockO2Components.append(ISI_30)
blockO2Components.append(sound_34)
blockO2Components.append(ISI_31)
blockO2Components.append(sound_35)
blockO2Components.append(ISI_32)
blockO2Components.append(text_8)
for thisComponent in blockO2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "blockO2"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blockO2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_31
    if t >= 0.0 and sound_31.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_31.tStart = t  # underestimates by a little under one frame
        sound_31.frameNStart = frameN  # exact frame index
        sound_31.play()  # start the sound (it finishes automatically)
    elif sound_31.status == STARTED and t >= (0.0 + (float(stimFiles[15,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_31.stop()  # stop the sound (if longer than duration)
    # start/stop sound_32
    if t >= (float(stimFiles[15,1])+float(stimFiles[15,2])) and sound_32.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_32.tStart = t  # underestimates by a little under one frame
        sound_32.frameNStart = frameN  # exact frame index
        sound_32.play()  # start the sound (it finishes automatically)
    elif sound_32.status == STARTED and t >= ((float(stimFiles[15,1])+float(stimFiles[15,2]))+ (float(stimFiles[16,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_32.stop()  # stop the sound (if longer than duration)
    # start/stop sound_33
    if t >= (float(stimFiles[15,1])+float(stimFiles[15,2])+float(stimFiles[16,1])+float(stimFiles[16,2])) and sound_33.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_33.tStart = t  # underestimates by a little under one frame
        sound_33.frameNStart = frameN  # exact frame index
        sound_33.play()  # start the sound (it finishes automatically)
    elif sound_33.status == STARTED and t >= ((float(stimFiles[15,1])+float(stimFiles[15,2])+float(stimFiles[16,1])+float(stimFiles[16,2])) + (float(stimFiles[17,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_33.stop()  # stop the sound (if longer than duration)
    # start/stop sound_34
    if t >= (float(stimFiles[15,1])+float(stimFiles[15,2])+float(stimFiles[16,1])+float(stimFiles[16,2])+float(stimFiles[17,1])+float(stimFiles[17,2])) and sound_34.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_34.tStart = t  # underestimates by a little under one frame
        sound_34.frameNStart = frameN  # exact frame index
        sound_34.play()  # start the sound (it finishes automatically)
    elif sound_34.status == STARTED and t >= ((float(stimFiles[15,1])+float(stimFiles[15,2])+float(stimFiles[16,1])+float(stimFiles[16,2])+float(stimFiles[17,1])+float(stimFiles[17,2])) + (float(stimFiles[18,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_34.stop()  # stop the sound (if longer than duration)
    # start/stop sound_35
    if t >= (float(stimFiles[15,1])+float(stimFiles[15,2])+float(stimFiles[16,1])+float(stimFiles[16,2])+float(stimFiles[17,1])+float(stimFiles[17,2])+float(stimFiles[18,1])+float(stimFiles[18,2])) and sound_35.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_35.tStart = t  # underestimates by a little under one frame
        sound_35.frameNStart = frameN  # exact frame index
        sound_35.play()  # start the sound (it finishes automatically)
    elif sound_35.status == STARTED and t >= ((float(stimFiles[15,1])+float(stimFiles[15,2])+float(stimFiles[16,1])+float(stimFiles[16,2])+float(stimFiles[17,1])+float(stimFiles[17,2])+float(stimFiles[18,1])+float(stimFiles[18,2])) + (float(stimFiles[19,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_35.stop()  # stop the sound (if longer than duration)
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t  # underestimates by a little under one frame
        text_8.frameNStart = frameN  # exact frame index
        text_8.setAutoDraw(True)
    elif text_8.status == STARTED and t >= (0.0 + (16-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_8.setAutoDraw(False)
    # *ISI_28* period
    if t >= float(stimFiles[15,1]) and ISI_28.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_28.tStart = t  # underestimates by a little under one frame
        ISI_28.frameNStart = frameN  # exact frame index
        ISI_28.start(float(stimFiles[15,2]))
    elif ISI_28.status == STARTED: #one frame should pass before updating params and completing
        ISI_28.complete() #finish the static period
    # *ISI_29* period
    if t >= (float(stimFiles[15,1])+float(stimFiles[15,2])+float(stimFiles[16,1])) and ISI_29.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_29.tStart = t  # underestimates by a little under one frame
        ISI_29.frameNStart = frameN  # exact frame index
        ISI_29.start(float(stimFiles[16,2]))
    elif ISI_29.status == STARTED: #one frame should pass before updating params and completing
        ISI_29.complete() #finish the static period
    # *ISI_30* period
    if t >= (float(stimFiles[15,1])+float(stimFiles[15,2])+float(stimFiles[16,1])+float(stimFiles[16,2])+float(stimFiles[17,1])) and ISI_30.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_30.tStart = t  # underestimates by a little under one frame
        ISI_30.frameNStart = frameN  # exact frame index
        ISI_30.start(float(stimFiles[17,2]))
    elif ISI_30.status == STARTED: #one frame should pass before updating params and completing
        ISI_30.complete() #finish the static period
    # *ISI_31* period
    if t >= (float(stimFiles[15,1])+float(stimFiles[15,2])+float(stimFiles[16,1])+float(stimFiles[16,2])+float(stimFiles[17,1])+float(stimFiles[17,2])+float(stimFiles[18,1])) and ISI_31.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_31.tStart = t  # underestimates by a little under one frame
        ISI_31.frameNStart = frameN  # exact frame index
        ISI_31.start(float(stimFiles[18,2]))
    elif ISI_31.status == STARTED: #one frame should pass before updating params and completing
        ISI_31.complete() #finish the static period
    # *ISI_32* period
    if t >= (float(stimFiles[15,1])+float(stimFiles[15,2])+float(stimFiles[16,1])+float(stimFiles[16,2])+float(stimFiles[17,1])+float(stimFiles[17,2])+float(stimFiles[18,1])+float(stimFiles[18,2])+float(stimFiles[19,1])) and ISI_32.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_32.tStart = t  # underestimates by a little under one frame
        ISI_32.frameNStart = frameN  # exact frame index
        ISI_32.start(float(stimFiles[19,2]))
    elif ISI_32.status == STARTED: #one frame should pass before updating params and completing
        ISI_32.complete() #finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockO2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "blockO2"-------
for thisComponent in blockO2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "compQ4"-------
t = 0
compQ4Clock.reset()  # clock 
frameN = -1
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
compQ4Components = []
compQ4Components.append(image_5)
for thisComponent in compQ4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "compQ4"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = compQ4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_5* updates
    if t >= 0.0 and image_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_5.tStart = t  # underestimates by a little under one frame
        image_5.frameNStart = frameN  # exact frame index
        image_5.setAutoDraw(True)
    elif image_5.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_5.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in compQ4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "compQ4"-------
for thisComponent in compQ4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(16.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_11)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if t >= 0.0 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t  # underestimates by a little under one frame
        text_11.frameNStart = frameN  # exact frame index
        text_11.setAutoDraw(True)
    elif text_11.status == STARTED and t >= (0.0 + (16-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_11.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "compQS2"-------
t = 0
compQS2Clock.reset()  # clock 
frameN = -1
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
compQS2Components = []
compQS2Components.append(image_9)
for thisComponent in compQS2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "compQS2"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = compQS2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_9* updates
    if t >= 0.0 and image_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_9.tStart = t  # underestimates by a little under one frame
        image_9.frameNStart = frameN  # exact frame index
        image_9.setAutoDraw(True)
    elif image_9.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_9.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in compQS2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "compQS2"-------
for thisComponent in compQS2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "blockS3"-------
t = 0
blockS3Clock.reset()  # clock 
frameN = -1
routineTimer.add(16.000000)
# update component parameters for each repeat
# keep track of which components have finished
blockS3Components = []
blockS3Components.append(sound_16)
blockS3Components.append(ISI_2)
blockS3Components.append(sound_17)
blockS3Components.append(ISI_15)
blockS3Components.append(sound_18)
blockS3Components.append(ISI_16)
blockS3Components.append(sound_19)
blockS3Components.append(ISI_17)
blockS3Components.append(sound_20)
blockS3Components.append(ISI_18)
blockS3Components.append(text_6)
for thisComponent in blockS3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "blockS3"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blockS3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_16
    if t >= 0.0 and sound_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_16.tStart = t  # underestimates by a little under one frame
        sound_16.frameNStart = frameN  # exact frame index
        sound_16.play()  # start the sound (it finishes automatically)
    elif sound_16.status == STARTED and t >= (0.0 + (float(stimFiles[20,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_16.stop()  # stop the sound (if longer than duration)
    # start/stop sound_17
    if t >= (float(stimFiles[20,1])+float(stimFiles[20,2])) and sound_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_17.tStart = t  # underestimates by a little under one frame
        sound_17.frameNStart = frameN  # exact frame index
        sound_17.play()  # start the sound (it finishes automatically)
    elif sound_17.status == STARTED and t >= ((float(stimFiles[20,1])+float(stimFiles[20,2]))+ (float(stimFiles[21,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_17.stop()  # stop the sound (if longer than duration)
    # start/stop sound_18
    if t >= (float(stimFiles[20,1])+float(stimFiles[20,2])+float(stimFiles[21,1])+float(stimFiles[21,2])) and sound_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_18.tStart = t  # underestimates by a little under one frame
        sound_18.frameNStart = frameN  # exact frame index
        sound_18.play()  # start the sound (it finishes automatically)
    elif sound_18.status == STARTED and t >= ((float(stimFiles[20,1])+float(stimFiles[20,2])+float(stimFiles[21,1])+float(stimFiles[21,2])) + (float(stimFiles[22,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_18.stop()  # stop the sound (if longer than duration)
    # start/stop sound_19
    if t >= (float(stimFiles[20,1])+float(stimFiles[20,2])+float(stimFiles[21,1])+float(stimFiles[21,2])+float(stimFiles[22,1])+float(stimFiles[22,2])) and sound_19.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_19.tStart = t  # underestimates by a little under one frame
        sound_19.frameNStart = frameN  # exact frame index
        sound_19.play()  # start the sound (it finishes automatically)
    elif sound_19.status == STARTED and t >= ((float(stimFiles[20,1])+float(stimFiles[20,2])+float(stimFiles[21,1])+float(stimFiles[21,2])+float(stimFiles[22,1])+float(stimFiles[22,2])) + (float(stimFiles[23,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_19.stop()  # stop the sound (if longer than duration)
    # start/stop sound_20
    if t >= (float(stimFiles[20,1])+float(stimFiles[20,2])+float(stimFiles[21,1])+float(stimFiles[21,2])+float(stimFiles[22,1])+float(stimFiles[22,2])+float(stimFiles[23,1])+float(stimFiles[23,2])) and sound_20.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_20.tStart = t  # underestimates by a little under one frame
        sound_20.frameNStart = frameN  # exact frame index
        sound_20.play()  # start the sound (it finishes automatically)
    elif sound_20.status == STARTED and t >= ((float(stimFiles[20,1])+float(stimFiles[20,2])+float(stimFiles[21,1])+float(stimFiles[21,2])+float(stimFiles[22,1])+float(stimFiles[22,2])+float(stimFiles[23,1])+float(stimFiles[23,2])) + (float(stimFiles[24,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_20.stop()  # stop the sound (if longer than duration)
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    elif text_6.status == STARTED and t >= (0.0 + (16-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_6.setAutoDraw(False)
    # *ISI_2* period
    if t >= float(stimFiles[20,1]) and ISI_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_2.tStart = t  # underestimates by a little under one frame
        ISI_2.frameNStart = frameN  # exact frame index
        ISI_2.start(float(stimFiles[20,2]))
    elif ISI_2.status == STARTED: #one frame should pass before updating params and completing
        ISI_2.complete() #finish the static period
    # *ISI_15* period
    if t >= (float(stimFiles[20,1])+float(stimFiles[20,2])+float(stimFiles[21,1])) and ISI_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_15.tStart = t  # underestimates by a little under one frame
        ISI_15.frameNStart = frameN  # exact frame index
        ISI_15.start(float(stimFiles[21,2]))
    elif ISI_15.status == STARTED: #one frame should pass before updating params and completing
        ISI_15.complete() #finish the static period
    # *ISI_16* period
    if t >= (float(stimFiles[20,1])+float(stimFiles[20,2])+float(stimFiles[21,1])+float(stimFiles[21,2])+float(stimFiles[22,1])) and ISI_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_16.tStart = t  # underestimates by a little under one frame
        ISI_16.frameNStart = frameN  # exact frame index
        ISI_16.start(float(stimFiles[22,2]))
    elif ISI_16.status == STARTED: #one frame should pass before updating params and completing
        ISI_16.complete() #finish the static period
    # *ISI_17* period
    if t >= (float(stimFiles[20,1])+float(stimFiles[20,2])+float(stimFiles[21,1])+float(stimFiles[21,2])+float(stimFiles[22,1])+float(stimFiles[22,2])+float(stimFiles[23,1])) and ISI_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_17.tStart = t  # underestimates by a little under one frame
        ISI_17.frameNStart = frameN  # exact frame index
        ISI_17.start(float(stimFiles[23,2]))
    elif ISI_17.status == STARTED: #one frame should pass before updating params and completing
        ISI_17.complete() #finish the static period
    # *ISI_18* period
    if t >= (float(stimFiles[20,1])+float(stimFiles[20,2])+float(stimFiles[21,1])+float(stimFiles[21,2])+float(stimFiles[22,1])+float(stimFiles[22,2])+float(stimFiles[23,1])+float(stimFiles[23,2])+float(stimFiles[24,1])) and ISI_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_18.tStart = t  # underestimates by a little under one frame
        ISI_18.frameNStart = frameN  # exact frame index
        ISI_18.start(float(stimFiles[24,2]))
    elif ISI_18.status == STARTED: #one frame should pass before updating params and completing
        ISI_18.complete() #finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockS3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "blockS3"-------
for thisComponent in blockS3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "compQ5"-------
t = 0
compQ5Clock.reset()  # clock 
frameN = -1
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
compQ5Components = []
compQ5Components.append(image_6)
for thisComponent in compQ5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "compQ5"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = compQ5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_6* updates
    if t >= 0.0 and image_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_6.tStart = t  # underestimates by a little under one frame
        image_6.frameNStart = frameN  # exact frame index
        image_6.setAutoDraw(True)
    elif image_6.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in compQ5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "compQ5"-------
for thisComponent in compQ5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(16.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_11)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if t >= 0.0 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t  # underestimates by a little under one frame
        text_11.frameNStart = frameN  # exact frame index
        text_11.setAutoDraw(True)
    elif text_11.status == STARTED and t >= (0.0 + (16-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_11.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "compQS3"-------
t = 0
compQS3Clock.reset()  # clock 
frameN = -1
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
compQS3Components = []
compQS3Components.append(image_10)
for thisComponent in compQS3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "compQS3"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = compQS3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_10* updates
    if t >= 0.0 and image_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_10.tStart = t  # underestimates by a little under one frame
        image_10.frameNStart = frameN  # exact frame index
        image_10.setAutoDraw(True)
    elif image_10.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_10.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in compQS3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "compQS3"-------
for thisComponent in compQS3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "blockS4"-------
t = 0
blockS4Clock.reset()  # clock 
frameN = -1
routineTimer.add(16.000000)
# update component parameters for each repeat
# keep track of which components have finished
blockS4Components = []
blockS4Components.append(sound_21)
blockS4Components.append(ISI_3)
blockS4Components.append(sound_22)
blockS4Components.append(ISI_19)
blockS4Components.append(sound_23)
blockS4Components.append(ISI_20)
blockS4Components.append(sound_24)
blockS4Components.append(ISI_21)
blockS4Components.append(sound_25)
blockS4Components.append(ISI_22)
blockS4Components.append(text_7)
for thisComponent in blockS4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "blockS4"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blockS4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_21
    if t >= 0.0 and sound_21.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_21.tStart = t  # underestimates by a little under one frame
        sound_21.frameNStart = frameN  # exact frame index
        sound_21.play()  # start the sound (it finishes automatically)
    elif sound_21.status == STARTED and t >= (0.0 + (float(stimFiles[25,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_21.stop()  # stop the sound (if longer than duration)
    # start/stop sound_22
    if t >= (float(stimFiles[25,1])+float(stimFiles[25,2])) and sound_22.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_22.tStart = t  # underestimates by a little under one frame
        sound_22.frameNStart = frameN  # exact frame index
        sound_22.play()  # start the sound (it finishes automatically)
    elif sound_22.status == STARTED and t >= ((float(stimFiles[25,1])+float(stimFiles[25,2]))+ (float(stimFiles[26,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_22.stop()  # stop the sound (if longer than duration)
    # start/stop sound_23
    if t >= (float(stimFiles[25,1])+float(stimFiles[25,2])+float(stimFiles[26,1])+float(stimFiles[26,2])) and sound_23.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_23.tStart = t  # underestimates by a little under one frame
        sound_23.frameNStart = frameN  # exact frame index
        sound_23.play()  # start the sound (it finishes automatically)
    elif sound_23.status == STARTED and t >= ((float(stimFiles[25,1])+float(stimFiles[25,2])+float(stimFiles[26,1])+float(stimFiles[26,2])) + (float(stimFiles[27,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_23.stop()  # stop the sound (if longer than duration)
    # start/stop sound_24
    if t >= (float(stimFiles[25,1])+float(stimFiles[25,2])+float(stimFiles[26,1])+float(stimFiles[26,2])+float(stimFiles[27,1])+float(stimFiles[27,2])) and sound_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_24.tStart = t  # underestimates by a little under one frame
        sound_24.frameNStart = frameN  # exact frame index
        sound_24.play()  # start the sound (it finishes automatically)
    elif sound_24.status == STARTED and t >= ((float(stimFiles[25,1])+float(stimFiles[25,2])+float(stimFiles[26,1])+float(stimFiles[26,2])+float(stimFiles[27,1])+float(stimFiles[27,2])) + (float(stimFiles[28,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_24.stop()  # stop the sound (if longer than duration)
    # start/stop sound_25
    if t >= (float(stimFiles[25,1])+float(stimFiles[25,2])+float(stimFiles[26,1])+float(stimFiles[26,2])+float(stimFiles[27,1])+float(stimFiles[27,2])+float(stimFiles[28,1])+float(stimFiles[28,2])) and sound_25.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_25.tStart = t  # underestimates by a little under one frame
        sound_25.frameNStart = frameN  # exact frame index
        sound_25.play()  # start the sound (it finishes automatically)
    elif sound_25.status == STARTED and t >= ((float(stimFiles[25,1])+float(stimFiles[25,2])+float(stimFiles[26,1])+float(stimFiles[26,2])+float(stimFiles[27,1])+float(stimFiles[27,2])+float(stimFiles[28,1])+float(stimFiles[28,2])) + (float(stimFiles[29,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_25.stop()  # stop the sound (if longer than duration)
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t  # underestimates by a little under one frame
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    elif text_7.status == STARTED and t >= (0.0 + (16-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_7.setAutoDraw(False)
    # *ISI_3* period
    if t >= float(stimFiles[25,1]) and ISI_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_3.tStart = t  # underestimates by a little under one frame
        ISI_3.frameNStart = frameN  # exact frame index
        ISI_3.start(float(stimFiles[25,2]))
    elif ISI_3.status == STARTED: #one frame should pass before updating params and completing
        ISI_3.complete() #finish the static period
    # *ISI_19* period
    if t >= (float(stimFiles[25,1])+float(stimFiles[25,2])+float(stimFiles[26,1])) and ISI_19.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_19.tStart = t  # underestimates by a little under one frame
        ISI_19.frameNStart = frameN  # exact frame index
        ISI_19.start(float(stimFiles[26,2]))
    elif ISI_19.status == STARTED: #one frame should pass before updating params and completing
        ISI_19.complete() #finish the static period
    # *ISI_20* period
    if t >= (float(stimFiles[25,1])+float(stimFiles[25,2])+float(stimFiles[26,1])+float(stimFiles[26,2])+float(stimFiles[27,1])) and ISI_20.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_20.tStart = t  # underestimates by a little under one frame
        ISI_20.frameNStart = frameN  # exact frame index
        ISI_20.start(float(stimFiles[27,2]))
    elif ISI_20.status == STARTED: #one frame should pass before updating params and completing
        ISI_20.complete() #finish the static period
    # *ISI_21* period
    if t >= (float(stimFiles[25,1])+float(stimFiles[25,2])+float(stimFiles[26,1])+float(stimFiles[26,2])+float(stimFiles[27,1])+float(stimFiles[27,2])+float(stimFiles[28,1])) and ISI_21.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_21.tStart = t  # underestimates by a little under one frame
        ISI_21.frameNStart = frameN  # exact frame index
        ISI_21.start(float(stimFiles[28,2]))
    elif ISI_21.status == STARTED: #one frame should pass before updating params and completing
        ISI_21.complete() #finish the static period
    # *ISI_22* period
    if t >= (float(stimFiles[25,1])+float(stimFiles[25,2])+float(stimFiles[26,1])+float(stimFiles[26,2])+float(stimFiles[27,1])+float(stimFiles[27,2])+float(stimFiles[28,1])+float(stimFiles[28,2])+float(stimFiles[29,1])) and ISI_22.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_22.tStart = t  # underestimates by a little under one frame
        ISI_22.frameNStart = frameN  # exact frame index
        ISI_22.start(float(stimFiles[29,2]))
    elif ISI_22.status == STARTED: #one frame should pass before updating params and completing
        ISI_22.complete() #finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockS4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "blockS4"-------
for thisComponent in blockS4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "compQ6"-------
t = 0
compQ6Clock.reset()  # clock 
frameN = -1
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
compQ6Components = []
compQ6Components.append(image_7)
for thisComponent in compQ6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "compQ6"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = compQ6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    if t >= 0.0 and image_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_7.tStart = t  # underestimates by a little under one frame
        image_7.frameNStart = frameN  # exact frame index
        image_7.setAutoDraw(True)
    elif image_7.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_7.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in compQ6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "compQ6"-------
for thisComponent in compQ6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "blockO3"-------
t = 0
blockO3Clock.reset()  # clock 
frameN = -1
routineTimer.add(16.000000)
# update component parameters for each repeat
# keep track of which components have finished
blockO3Components = []
blockO3Components.append(sound_36)
blockO3Components.append(ISI_33)
blockO3Components.append(sound_37)
blockO3Components.append(ISI_34)
blockO3Components.append(sound_38)
blockO3Components.append(ISI_35)
blockO3Components.append(sound_39)
blockO3Components.append(ISI_36)
blockO3Components.append(sound_40)
blockO3Components.append(ISI_37)
blockO3Components.append(text_9)
for thisComponent in blockO3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "blockO3"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blockO3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_36
    if t >= 0.0 and sound_36.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_36.tStart = t  # underestimates by a little under one frame
        sound_36.frameNStart = frameN  # exact frame index
        sound_36.play()  # start the sound (it finishes automatically)
    elif sound_36.status == STARTED and t >= (0.0 + (float(stimFiles[30,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_36.stop()  # stop the sound (if longer than duration)
    # start/stop sound_37
    if t >= (float(stimFiles[30,1])+float(stimFiles[30,2])) and sound_37.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_37.tStart = t  # underestimates by a little under one frame
        sound_37.frameNStart = frameN  # exact frame index
        sound_37.play()  # start the sound (it finishes automatically)
    elif sound_37.status == STARTED and t >= ((float(stimFiles[30,1])+float(stimFiles[30,2]))+ (float(stimFiles[31,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_37.stop()  # stop the sound (if longer than duration)
    # start/stop sound_38
    if t >= (float(stimFiles[30,1])+float(stimFiles[30,2])+float(stimFiles[31,1])+float(stimFiles[31,2])) and sound_38.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_38.tStart = t  # underestimates by a little under one frame
        sound_38.frameNStart = frameN  # exact frame index
        sound_38.play()  # start the sound (it finishes automatically)
    elif sound_38.status == STARTED and t >= ((float(stimFiles[30,1])+float(stimFiles[30,2])+float(stimFiles[31,1])+float(stimFiles[31,2])) + (float(stimFiles[32,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_38.stop()  # stop the sound (if longer than duration)
    # start/stop sound_39
    if t >= (float(stimFiles[30,1])+float(stimFiles[30,2])+float(stimFiles[31,1])+float(stimFiles[31,2])+float(stimFiles[32,1])+float(stimFiles[32,2])) and sound_39.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_39.tStart = t  # underestimates by a little under one frame
        sound_39.frameNStart = frameN  # exact frame index
        sound_39.play()  # start the sound (it finishes automatically)
    elif sound_39.status == STARTED and t >= ((float(stimFiles[30,1])+float(stimFiles[30,2])+float(stimFiles[31,1])+float(stimFiles[31,2])+float(stimFiles[32,1])+float(stimFiles[32,2])) + (float(stimFiles[33,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_39.stop()  # stop the sound (if longer than duration)
    # start/stop sound_40
    if t >= (float(stimFiles[30,1])+float(stimFiles[30,2])+float(stimFiles[31,1])+float(stimFiles[31,2])+float(stimFiles[32,1])+float(stimFiles[32,2])+float(stimFiles[33,1])+float(stimFiles[33,2])) and sound_40.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_40.tStart = t  # underestimates by a little under one frame
        sound_40.frameNStart = frameN  # exact frame index
        sound_40.play()  # start the sound (it finishes automatically)
    elif sound_40.status == STARTED and t >= ((float(stimFiles[30,1])+float(stimFiles[30,2])+float(stimFiles[31,1])+float(stimFiles[31,2])+float(stimFiles[32,1])+float(stimFiles[32,2])+float(stimFiles[33,1])+float(stimFiles[33,2])) + (float(stimFiles[34,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_40.stop()  # stop the sound (if longer than duration)
    
    # *text_9* updates
    if t >= 0.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t  # underestimates by a little under one frame
        text_9.frameNStart = frameN  # exact frame index
        text_9.setAutoDraw(True)
    elif text_9.status == STARTED and t >= (0.0 + (16-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_9.setAutoDraw(False)
    # *ISI_33* period
    if t >= float(stimFiles[30,1]) and ISI_33.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_33.tStart = t  # underestimates by a little under one frame
        ISI_33.frameNStart = frameN  # exact frame index
        ISI_33.start(float(stimFiles[30,2]))
    elif ISI_33.status == STARTED: #one frame should pass before updating params and completing
        ISI_33.complete() #finish the static period
    # *ISI_34* period
    if t >= (float(stimFiles[30,1])+float(stimFiles[30,2])+float(stimFiles[31,1])) and ISI_34.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_34.tStart = t  # underestimates by a little under one frame
        ISI_34.frameNStart = frameN  # exact frame index
        ISI_34.start(float(stimFiles[31,2]))
    elif ISI_34.status == STARTED: #one frame should pass before updating params and completing
        ISI_34.complete() #finish the static period
    # *ISI_35* period
    if t >= (float(stimFiles[30,1])+float(stimFiles[30,2])+float(stimFiles[31,1])+float(stimFiles[31,2])+float(stimFiles[32,1])) and ISI_35.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_35.tStart = t  # underestimates by a little under one frame
        ISI_35.frameNStart = frameN  # exact frame index
        ISI_35.start(float(stimFiles[32,2]))
    elif ISI_35.status == STARTED: #one frame should pass before updating params and completing
        ISI_35.complete() #finish the static period
    # *ISI_36* period
    if t >= (float(stimFiles[30,1])+float(stimFiles[30,2])+float(stimFiles[31,1])+float(stimFiles[31,2])+float(stimFiles[32,1])+float(stimFiles[32,2])+float(stimFiles[33,1])) and ISI_36.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_36.tStart = t  # underestimates by a little under one frame
        ISI_36.frameNStart = frameN  # exact frame index
        ISI_36.start(float(stimFiles[33,2]))
    elif ISI_36.status == STARTED: #one frame should pass before updating params and completing
        ISI_36.complete() #finish the static period
    # *ISI_37* period
    if t >= (float(stimFiles[30,1])+float(stimFiles[30,2])+float(stimFiles[31,1])+float(stimFiles[31,2])+float(stimFiles[32,1])+float(stimFiles[32,2])+float(stimFiles[33,1])+float(stimFiles[33,2])+float(stimFiles[34,1])) and ISI_37.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_37.tStart = t  # underestimates by a little under one frame
        ISI_37.frameNStart = frameN  # exact frame index
        ISI_37.start(float(stimFiles[34,2]))
    elif ISI_37.status == STARTED: #one frame should pass before updating params and completing
        ISI_37.complete() #finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockO3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "blockO3"-------
for thisComponent in blockO3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "compQ7"-------
t = 0
compQ7Clock.reset()  # clock 
frameN = -1
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
compQ7Components = []
compQ7Components.append(image_12)
for thisComponent in compQ7Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "compQ7"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = compQ7Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_12* updates
    if t >= 0.0 and image_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_12.tStart = t  # underestimates by a little under one frame
        image_12.frameNStart = frameN  # exact frame index
        image_12.setAutoDraw(True)
    elif image_12.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_12.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in compQ7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "compQ7"-------
for thisComponent in compQ7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "blockO4"-------
t = 0
blockO4Clock.reset()  # clock 
frameN = -1
routineTimer.add(16.000000)
# update component parameters for each repeat
# keep track of which components have finished
blockO4Components = []
blockO4Components.append(sound_41)
blockO4Components.append(ISI_38)
blockO4Components.append(sound_42)
blockO4Components.append(ISI_39)
blockO4Components.append(sound_43)
blockO4Components.append(ISI_40)
blockO4Components.append(sound_44)
blockO4Components.append(ISI_41)
blockO4Components.append(sound_45)
blockO4Components.append(ISI_42)
blockO4Components.append(text_10)
for thisComponent in blockO4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "blockO4"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blockO4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_41
    if t >= 0.0 and sound_41.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_41.tStart = t  # underestimates by a little under one frame
        sound_41.frameNStart = frameN  # exact frame index
        sound_41.play()  # start the sound (it finishes automatically)
    elif sound_41.status == STARTED and t >= (0.0 + (float(stimFiles[35,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_41.stop()  # stop the sound (if longer than duration)
    # start/stop sound_42
    if t >= (float(stimFiles[35,1])+float(stimFiles[35,2])) and sound_42.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_42.tStart = t  # underestimates by a little under one frame
        sound_42.frameNStart = frameN  # exact frame index
        sound_42.play()  # start the sound (it finishes automatically)
    elif sound_42.status == STARTED and t >= ((float(stimFiles[35,1])+float(stimFiles[35,2]))+ (float(stimFiles[36,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_42.stop()  # stop the sound (if longer than duration)
    # start/stop sound_43
    if t >= (float(stimFiles[35,1])+float(stimFiles[35,2])+float(stimFiles[36,1])+float(stimFiles[36,2])) and sound_43.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_43.tStart = t  # underestimates by a little under one frame
        sound_43.frameNStart = frameN  # exact frame index
        sound_43.play()  # start the sound (it finishes automatically)
    elif sound_43.status == STARTED and t >= ((float(stimFiles[35,1])+float(stimFiles[35,2])+float(stimFiles[36,1])+float(stimFiles[36,2])) + (float(stimFiles[37,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_43.stop()  # stop the sound (if longer than duration)
    # start/stop sound_44
    if t >= (float(stimFiles[35,1])+float(stimFiles[35,2])+float(stimFiles[36,1])+float(stimFiles[36,2])+float(stimFiles[37,1])+float(stimFiles[37,2])) and sound_44.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_44.tStart = t  # underestimates by a little under one frame
        sound_44.frameNStart = frameN  # exact frame index
        sound_44.play()  # start the sound (it finishes automatically)
    elif sound_44.status == STARTED and t >= ((float(stimFiles[35,1])+float(stimFiles[35,2])+float(stimFiles[36,1])+float(stimFiles[36,2])+float(stimFiles[37,1])+float(stimFiles[37,2])) + (float(stimFiles[38,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_44.stop()  # stop the sound (if longer than duration)
    # start/stop sound_45
    if t >= (float(stimFiles[35,1])+float(stimFiles[35,2])+float(stimFiles[36,1])+float(stimFiles[36,2])+float(stimFiles[37,1])+float(stimFiles[37,2])+float(stimFiles[38,1])+float(stimFiles[38,2])) and sound_45.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_45.tStart = t  # underestimates by a little under one frame
        sound_45.frameNStart = frameN  # exact frame index
        sound_45.play()  # start the sound (it finishes automatically)
    elif sound_45.status == STARTED and t >= ((float(stimFiles[35,1])+float(stimFiles[35,2])+float(stimFiles[36,1])+float(stimFiles[36,2])+float(stimFiles[37,1])+float(stimFiles[37,2])+float(stimFiles[38,1])+float(stimFiles[38,2])) + (float(stimFiles[39,1])-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_45.stop()  # stop the sound (if longer than duration)
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t  # underestimates by a little under one frame
        text_10.frameNStart = frameN  # exact frame index
        text_10.setAutoDraw(True)
    elif text_10.status == STARTED and t >= (0.0 + (16-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_10.setAutoDraw(False)
    # *ISI_38* period
    if t >= float(stimFiles[35,1]) and ISI_38.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_38.tStart = t  # underestimates by a little under one frame
        ISI_38.frameNStart = frameN  # exact frame index
        ISI_38.start(float(stimFiles[35,2]))
    elif ISI_38.status == STARTED: #one frame should pass before updating params and completing
        ISI_38.complete() #finish the static period
    # *ISI_39* period
    if t >= (float(stimFiles[35,1])+float(stimFiles[35,2])+float(stimFiles[36,1])) and ISI_39.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_39.tStart = t  # underestimates by a little under one frame
        ISI_39.frameNStart = frameN  # exact frame index
        ISI_39.start(float(stimFiles[36,2]))
    elif ISI_39.status == STARTED: #one frame should pass before updating params and completing
        ISI_39.complete() #finish the static period
    # *ISI_40* period
    if t >= (float(stimFiles[35,1])+float(stimFiles[35,2])+float(stimFiles[36,1])+float(stimFiles[36,2])+float(stimFiles[37,1])) and ISI_40.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_40.tStart = t  # underestimates by a little under one frame
        ISI_40.frameNStart = frameN  # exact frame index
        ISI_40.start(float(stimFiles[37,2]))
    elif ISI_40.status == STARTED: #one frame should pass before updating params and completing
        ISI_40.complete() #finish the static period
    # *ISI_41* period
    if t >= (float(stimFiles[35,1])+float(stimFiles[35,2])+float(stimFiles[36,1])+float(stimFiles[36,2])+float(stimFiles[37,1])+float(stimFiles[37,2])+float(stimFiles[38,1])) and ISI_41.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_41.tStart = t  # underestimates by a little under one frame
        ISI_41.frameNStart = frameN  # exact frame index
        ISI_41.start(float(stimFiles[38,2]))
    elif ISI_41.status == STARTED: #one frame should pass before updating params and completing
        ISI_41.complete() #finish the static period
    # *ISI_42* period
    if t >= (float(stimFiles[35,1])+float(stimFiles[35,2])+float(stimFiles[36,1])+float(stimFiles[36,2])+float(stimFiles[37,1])+float(stimFiles[37,2])+float(stimFiles[38,1])+float(stimFiles[38,2])+float(stimFiles[39,1])) and ISI_42.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_42.tStart = t  # underestimates by a little under one frame
        ISI_42.frameNStart = frameN  # exact frame index
        ISI_42.start(float(stimFiles[39,2]))
    elif ISI_42.status == STARTED: #one frame should pass before updating params and completing
        ISI_42.complete() #finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockO4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "blockO4"-------
for thisComponent in blockO4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "compQ8"-------
t = 0
compQ8Clock.reset()  # clock 
frameN = -1
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
compQ8Components = []
compQ8Components.append(image_13)
for thisComponent in compQ8Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "compQ8"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = compQ8Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_13* updates
    if t >= 0.0 and image_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_13.tStart = t  # underestimates by a little under one frame
        image_13.frameNStart = frameN  # exact frame index
        image_13.setAutoDraw(True)
    elif image_13.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_13.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in compQ8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "compQ8"-------
for thisComponent in compQ8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "rest"-------
t = 0
restClock.reset()  # clock 
frameN = -1
routineTimer.add(16.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = []
restComponents.append(text_11)
for thisComponent in restComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "rest"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if t >= 0.0 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t  # underestimates by a little under one frame
        text_11.frameNStart = frameN  # exact frame index
        text_11.setAutoDraw(True)
    elif text_11.status == STARTED and t >= (0.0 + (16-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_11.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "compQS4"-------
t = 0
compQS4Clock.reset()  # clock 
frameN = -1
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
compQS4Components = []
compQS4Components.append(image_11)
for thisComponent in compQS4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "compQS4"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = compQS4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_11* updates
    if t >= 0.0 and image_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_11.tStart = t  # underestimates by a little under one frame
        image_11.frameNStart = frameN  # exact frame index
        image_11.setAutoDraw(True)
    elif image_11.status == STARTED and t >= (0.0 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_11.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in compQS4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "compQS4"-------
for thisComponent in compQS4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
