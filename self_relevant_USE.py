#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.02), November 03, 2014, at 13:41
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'self_relevant'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

#list randomization
if int(expInfo['participant'])%3 == 1:
    expInfo['list'] = '1'
elif int(expInfo['participant'])%3 == 2:
    expInfo['list'] = '2'
elif int(expInfo['participant'])%3 == 0:
    expInfo['list'] = '3'

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
win = visual.Window(size=(1600, 1200), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
inst = visual.TextStim(win=win, ori=0, name='inst',
    text='You will hear words that describes personality attributes. You will be asked to answer whether these words apply to YOU or to Abrabam Lincoln, or whether these words describe positive attributes or not. There is no right or wrong answer so please make a judgement based on your gut instinct. Instructions will be displayed before every block of words. ',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trigger"
triggerClock = core.Clock()
trig = visual.ImageStim(win=win, name='trig',
    image=u'AndersonWords/crosshair.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
condition_file='list%s_rtsz_run%s.csv'%(expInfo['list'],expInfo['session'][-1])
print condition_file
fix = visual.ImageStim(win=win, name='fix',
    image=u'AndersonWords/crosshair.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "cue"
cueClock = core.Clock()
Cue1 = visual.ImageStim(win=win, name='Cue1',
    image=u'AndersonWords/self.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial_1"
trial_1Clock = core.Clock()
ISI_6 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_6')
sound_6 = sound.Sound('A', secs=3)
sound_6.setVolume(1)
fix1 = visual.ImageStim(win=win, name='fix1',
    image=u'AndersonWords/crosshair.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
condition_file='list%s_rtsz_run%s.csv'%(expInfo['list'],expInfo['session'][-1])
fix = visual.ImageStim(win=win, name='fix',
    image=u'AndersonWords/crosshair.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "cue_2"
cue_2Clock = core.Clock()
Cue2 = visual.ImageStim(win=win, name='Cue2',
    image=u'AndersonWords/other.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
ISI_7 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_7')
sound_7 = sound.Sound('A', secs=3)
sound_7.setVolume(1)
fix2 = visual.ImageStim(win=win, name='fix2',
    image=u'AndersonWords/crosshair.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
condition_file='list%s_rtsz_run%s.csv'%(expInfo['list'],expInfo['session'][-1])
fix = visual.ImageStim(win=win, name='fix',
    image=u'AndersonWords/crosshair.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "cue_3"
cue_3Clock = core.Clock()
Cue3 = visual.ImageStim(win=win, name='Cue3',
    image=u'AndersonWords/positive.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial_3"
trial_3Clock = core.Clock()
ISI_8 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_8')
sound_8 = sound.Sound('A', secs=3)
sound_8.setVolume(1)
fix3 = visual.ImageStim(win=win, name='fix3',
    image=u'AndersonWords/crosshair.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
condition_file='list%s_rtsz_run%s.csv'%(expInfo['list'],expInfo['session'][-1])
fix = visual.ImageStim(win=win, name='fix',
    image=u'AndersonWords/crosshair.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "cue_4"
cue_4Clock = core.Clock()
Cue4 = visual.ImageStim(win=win, name='Cue4',
    image=u'AndersonWords/other.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial_4"
trial_4Clock = core.Clock()
ISI_9 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_9')
sound_9 = sound.Sound('A', secs=3)
sound_9.setVolume(1)
fix4 = visual.ImageStim(win=win, name='fix4',
    image=u'AndersonWords/crosshair.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
condition_file='list%s_rtsz_run%s.csv'%(expInfo['list'],expInfo['session'][-1])
fix = visual.ImageStim(win=win, name='fix',
    image=u'AndersonWords/crosshair.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "cue_5"
cue_5Clock = core.Clock()
Cue5 = visual.ImageStim(win=win, name='Cue5',
    image=u'AndersonWords/self.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial_5"
trial_5Clock = core.Clock()
ISI_10 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_10')
sound_10 = sound.Sound('A', secs=3)
sound_10.setVolume(1)
fix5 = visual.ImageStim(win=win, name='fix5',
    image=u'AndersonWords/crosshair.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
condition_file='list%s_rtsz_run%s.csv'%(expInfo['list'],expInfo['session'][-1])
fix = visual.ImageStim(win=win, name='fix',
    image=u'AndersonWords/crosshair.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "cue_6"
cue_6Clock = core.Clock()
Cue6 = visual.ImageStim(win=win, name='Cue6',
    image=u'AndersonWords/positive.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial_6"
trial_6Clock = core.Clock()
ISI_11 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_11')
sound_11 = sound.Sound('A', secs=3)
sound_11.setVolume(1)
fix6 = visual.ImageStim(win=win, name='fix6',
    image=u'AndersonWords/crosshair.tif', mask=None,
    ori=0, pos=[0, 0], size=[1, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "end"
endClock = core.Clock()
done = visual.TextStim(win=win, ori=0, name='done',
    text='take a break!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
space = event.BuilderKeyResponse()  # create an object of type KeyResponse
space.status = NOT_STARTED
# keep track of which components have finished
instructionComponents = []
instructionComponents.append(inst)
instructionComponents.append(space)
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
    
    # *inst* updates
    if t >= 0.0 and inst.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst.tStart = t  # underestimates by a little under one frame
        inst.frameNStart = frameN  # exact frame index
        inst.setAutoDraw(True)
    
    # *space* updates
    if t >= 0.0 and space.status == NOT_STARTED:
        # keep track of start time/frame for later
        space.tStart = t  # underestimates by a little under one frame
        space.frameNStart = frameN  # exact frame index
        space.status = STARTED
        # keyboard checking is just starting
        space.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if space.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            space.keys = theseKeys[-1]  # just the last key pressed
            space.rt = space.clock.getTime()
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
if space.keys in ['', [], None]:  # No response was made
   space.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('space.keys',space.keys)
if space.keys != None:  # we had a response
    thisExp.addData('space.rt', space.rt)
thisExp.nextEntry()

#------Prepare to start Routine "trigger"-------
t = 0
triggerClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
scan_trigger = event.BuilderKeyResponse()  # create an object of type KeyResponse
scan_trigger.status = NOT_STARTED
# keep track of which components have finished
triggerComponents = []
triggerComponents.append(scan_trigger)
triggerComponents.append(trig)
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
    
    # *scan_trigger* updates
    if t >= 0.0 and scan_trigger.status == NOT_STARTED:
        # keep track of start time/frame for later
        scan_trigger.tStart = t  # underestimates by a little under one frame
        scan_trigger.frameNStart = frameN  # exact frame index
        scan_trigger.status = STARTED
        # keyboard checking is just starting
        scan_trigger.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if scan_trigger.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 't', 'return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            scan_trigger.keys = theseKeys[-1]  # just the last key pressed
            scan_trigger.rt = scan_trigger.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *trig* updates
    if t >= 0.0 and trig.status == NOT_STARTED:
        # keep track of start time/frame for later
        trig.tStart = t  # underestimates by a little under one frame
        trig.frameNStart = frameN  # exact frame index
        trig.setAutoDraw(True)
    
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
if scan_trigger.keys in ['', [], None]:  # No response was made
   scan_trigger.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('scan_trigger.keys',scan_trigger.keys)
if scan_trigger.keys != None:  # we had a response
    thisExp.addData('scan_trigger.rt', scan_trigger.rt)
thisExp.nextEntry()

#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(10.000000)
# update component parameters for each repeat

# keep track of which components have finished
fixationComponents = []
fixationComponents.append(fix)
for thisComponent in fixationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "fixation"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *fix* updates
    if t >= 0.0 and fix.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix.tStart = t  # underestimates by a little under one frame
        fix.frameNStart = frameN  # exact frame index
        fix.setAutoDraw(True)
    elif fix.status == STARTED and t >= (0.0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
        fix.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


#------Prepare to start Routine "cue"-------
t = 0
cueClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
cueComponents = []
cueComponents.append(Cue1)
for thisComponent in cueComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "cue"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = cueClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cue1* updates
    if t >= 0.0 and Cue1.status == NOT_STARTED:
        # keep track of start time/frame for later
        Cue1.tStart = t  # underestimates by a little under one frame
        Cue1.frameNStart = frameN  # exact frame index
        Cue1.setAutoDraw(True)
    elif Cue1.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        Cue1.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "cue"-------
for thisComponent in cueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trial1_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(condition_file),
    seed=None, name='trial1_loop')
thisExp.addLoop(trial1_loop)  # add the loop to the experiment
thisTrial1_loop = trial1_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial1_loop.rgb)
if thisTrial1_loop != None:
    for paramName in thisTrial1_loop.keys():
        exec(paramName + '= thisTrial1_loop.' + paramName)

for thisTrial1_loop in trial1_loop:
    currentLoop = trial1_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrial1_loop.rgb)
    if thisTrial1_loop != None:
        for paramName in thisTrial1_loop.keys():
            exec(paramName + '= thisTrial1_loop.' + paramName)
    
    #------Prepare to start Routine "trial_1"-------
    t = 0
    trial_1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    sound_6.setSound(trial1)
    selfrel_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    selfrel_resp_6.status = NOT_STARTED
    # keep track of which components have finished
    trial_1Components = []
    trial_1Components.append(ISI_6)
    trial_1Components.append(sound_6)
    trial_1Components.append(selfrel_resp_6)
    trial_1Components.append(fix1)
    for thisComponent in trial_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial_1"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_6
        if t >= 0.5 and sound_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_6.tStart = t  # underestimates by a little under one frame
            sound_6.frameNStart = frameN  # exact frame index
            sound_6.play()  # start the sound (it finishes automatically)
        elif sound_6.status == STARTED and t >= (0.5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_6.stop()  # stop the sound (if longer than duration)
        
        # *selfrel_resp_6* updates
        if t >= 0.5 and selfrel_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            selfrel_resp_6.tStart = t  # underestimates by a little under one frame
            selfrel_resp_6.frameNStart = frameN  # exact frame index
            selfrel_resp_6.status = STARTED
            # keyboard checking is just starting
            selfrel_resp_6.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif selfrel_resp_6.status == STARTED and t >= (0.5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            selfrel_resp_6.status = STOPPED
        if selfrel_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', 'num_1', 'num_2', 'num_3', 'num_4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                selfrel_resp_6.keys = theseKeys[-1]  # just the last key pressed
                selfrel_resp_6.rt = selfrel_resp_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *fix1* updates
        if t >= 0.0 and fix1.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix1.tStart = t  # underestimates by a little under one frame
            fix1.frameNStart = frameN  # exact frame index
            fix1.setAutoDraw(True)
        elif fix1.status == STARTED and t >= (0.0 + (3.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix1.setAutoDraw(False)
        # *ISI_6* period
        if t >= 0.0 and ISI_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_6.tStart = t  # underestimates by a little under one frame
            ISI_6.frameNStart = frameN  # exact frame index
            ISI_6.start(0.5)
        elif ISI_6.status == STARTED: #one frame should pass before updating params and completing
            ISI_6.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial_1"-------
    for thisComponent in trial_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if selfrel_resp_6.keys in ['', [], None]:  # No response was made
       selfrel_resp_6.keys=None
    # store data for trial1_loop (TrialHandler)
    trial1_loop.addData('selfrel_resp_6.keys',selfrel_resp_6.keys)
    if selfrel_resp_6.keys != None:  # we had a response
        trial1_loop.addData('selfrel_resp_6.rt', selfrel_resp_6.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trial1_loop'


#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(10.000000)
# update component parameters for each repeat

# keep track of which components have finished
fixationComponents = []
fixationComponents.append(fix)
for thisComponent in fixationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "fixation"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *fix* updates
    if t >= 0.0 and fix.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix.tStart = t  # underestimates by a little under one frame
        fix.frameNStart = frameN  # exact frame index
        fix.setAutoDraw(True)
    elif fix.status == STARTED and t >= (0.0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
        fix.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


#------Prepare to start Routine "cue_2"-------
t = 0
cue_2Clock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
cue_2Components = []
cue_2Components.append(Cue2)
for thisComponent in cue_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "cue_2"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = cue_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cue2* updates
    if t >= 0.0 and Cue2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Cue2.tStart = t  # underestimates by a little under one frame
        Cue2.frameNStart = frameN  # exact frame index
        Cue2.setAutoDraw(True)
    elif Cue2.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        Cue2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cue_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "cue_2"-------
for thisComponent in cue_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trial2_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(condition_file),
    seed=None, name='trial2_loop')
thisExp.addLoop(trial2_loop)  # add the loop to the experiment
thisTrial2_loop = trial2_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial2_loop.rgb)
if thisTrial2_loop != None:
    for paramName in thisTrial2_loop.keys():
        exec(paramName + '= thisTrial2_loop.' + paramName)

for thisTrial2_loop in trial2_loop:
    currentLoop = trial2_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrial2_loop.rgb)
    if thisTrial2_loop != None:
        for paramName in thisTrial2_loop.keys():
            exec(paramName + '= thisTrial2_loop.' + paramName)
    
    #------Prepare to start Routine "trial_2"-------
    t = 0
    trial_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    sound_7.setSound(trial2)
    selfrel_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    selfrel_resp_7.status = NOT_STARTED
    # keep track of which components have finished
    trial_2Components = []
    trial_2Components.append(ISI_7)
    trial_2Components.append(sound_7)
    trial_2Components.append(selfrel_resp_7)
    trial_2Components.append(fix2)
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_7
        if t >= 0.5 and sound_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_7.tStart = t  # underestimates by a little under one frame
            sound_7.frameNStart = frameN  # exact frame index
            sound_7.play()  # start the sound (it finishes automatically)
        elif sound_7.status == STARTED and t >= (0.5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_7.stop()  # stop the sound (if longer than duration)
        
        # *selfrel_resp_7* updates
        if t >= 0.5 and selfrel_resp_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            selfrel_resp_7.tStart = t  # underestimates by a little under one frame
            selfrel_resp_7.frameNStart = frameN  # exact frame index
            selfrel_resp_7.status = STARTED
            # keyboard checking is just starting
            selfrel_resp_7.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif selfrel_resp_7.status == STARTED and t >= (0.5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            selfrel_resp_7.status = STOPPED
        if selfrel_resp_7.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', 'num_1', 'num_2', 'num_3', 'num_4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                selfrel_resp_7.keys = theseKeys[-1]  # just the last key pressed
                selfrel_resp_7.rt = selfrel_resp_7.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *fix2* updates
        if t >= 0.0 and fix2.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix2.tStart = t  # underestimates by a little under one frame
            fix2.frameNStart = frameN  # exact frame index
            fix2.setAutoDraw(True)
        elif fix2.status == STARTED and t >= (0.0 + (3.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix2.setAutoDraw(False)
        # *ISI_7* period
        if t >= 0.0 and ISI_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_7.tStart = t  # underestimates by a little under one frame
            ISI_7.frameNStart = frameN  # exact frame index
            ISI_7.start(0.5)
        elif ISI_7.status == STARTED: #one frame should pass before updating params and completing
            ISI_7.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial_2"-------
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if selfrel_resp_7.keys in ['', [], None]:  # No response was made
       selfrel_resp_7.keys=None
    # store data for trial2_loop (TrialHandler)
    trial2_loop.addData('selfrel_resp_7.keys',selfrel_resp_7.keys)
    if selfrel_resp_7.keys != None:  # we had a response
        trial2_loop.addData('selfrel_resp_7.rt', selfrel_resp_7.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trial2_loop'


#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(10.000000)
# update component parameters for each repeat

# keep track of which components have finished
fixationComponents = []
fixationComponents.append(fix)
for thisComponent in fixationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "fixation"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *fix* updates
    if t >= 0.0 and fix.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix.tStart = t  # underestimates by a little under one frame
        fix.frameNStart = frameN  # exact frame index
        fix.setAutoDraw(True)
    elif fix.status == STARTED and t >= (0.0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
        fix.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


#------Prepare to start Routine "cue_3"-------
t = 0
cue_3Clock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
cue_3Components = []
cue_3Components.append(Cue3)
for thisComponent in cue_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "cue_3"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = cue_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cue3* updates
    if t >= 0.0 and Cue3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Cue3.tStart = t  # underestimates by a little under one frame
        Cue3.frameNStart = frameN  # exact frame index
        Cue3.setAutoDraw(True)
    elif Cue3.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        Cue3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cue_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "cue_3"-------
for thisComponent in cue_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trial3_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(condition_file),
    seed=None, name='trial3_loop')
thisExp.addLoop(trial3_loop)  # add the loop to the experiment
thisTrial3_loop = trial3_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial3_loop.rgb)
if thisTrial3_loop != None:
    for paramName in thisTrial3_loop.keys():
        exec(paramName + '= thisTrial3_loop.' + paramName)

for thisTrial3_loop in trial3_loop:
    currentLoop = trial3_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrial3_loop.rgb)
    if thisTrial3_loop != None:
        for paramName in thisTrial3_loop.keys():
            exec(paramName + '= thisTrial3_loop.' + paramName)
    
    #------Prepare to start Routine "trial_3"-------
    t = 0
    trial_3Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    sound_8.setSound(trial3)
    selfrel_resp_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    selfrel_resp_8.status = NOT_STARTED
    # keep track of which components have finished
    trial_3Components = []
    trial_3Components.append(ISI_8)
    trial_3Components.append(sound_8)
    trial_3Components.append(selfrel_resp_8)
    trial_3Components.append(fix3)
    for thisComponent in trial_3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial_3"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_8
        if t >= 0.5 and sound_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_8.tStart = t  # underestimates by a little under one frame
            sound_8.frameNStart = frameN  # exact frame index
            sound_8.play()  # start the sound (it finishes automatically)
        elif sound_8.status == STARTED and t >= (0.5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_8.stop()  # stop the sound (if longer than duration)
        
        # *selfrel_resp_8* updates
        if t >= 0.5 and selfrel_resp_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            selfrel_resp_8.tStart = t  # underestimates by a little under one frame
            selfrel_resp_8.frameNStart = frameN  # exact frame index
            selfrel_resp_8.status = STARTED
            # keyboard checking is just starting
            selfrel_resp_8.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif selfrel_resp_8.status == STARTED and t >= (0.5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            selfrel_resp_8.status = STOPPED
        if selfrel_resp_8.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', 'num_1', 'num_2', 'num_3', 'num_4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                selfrel_resp_8.keys = theseKeys[-1]  # just the last key pressed
                selfrel_resp_8.rt = selfrel_resp_8.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *fix3* updates
        if t >= 0.0 and fix3.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix3.tStart = t  # underestimates by a little under one frame
            fix3.frameNStart = frameN  # exact frame index
            fix3.setAutoDraw(True)
        elif fix3.status == STARTED and t >= (0.0 + (3.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix3.setAutoDraw(False)
        # *ISI_8* period
        if t >= 0.0 and ISI_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_8.tStart = t  # underestimates by a little under one frame
            ISI_8.frameNStart = frameN  # exact frame index
            ISI_8.start(0.5)
        elif ISI_8.status == STARTED: #one frame should pass before updating params and completing
            ISI_8.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial_3"-------
    for thisComponent in trial_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if selfrel_resp_8.keys in ['', [], None]:  # No response was made
       selfrel_resp_8.keys=None
    # store data for trial3_loop (TrialHandler)
    trial3_loop.addData('selfrel_resp_8.keys',selfrel_resp_8.keys)
    if selfrel_resp_8.keys != None:  # we had a response
        trial3_loop.addData('selfrel_resp_8.rt', selfrel_resp_8.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trial3_loop'


#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(10.000000)
# update component parameters for each repeat

# keep track of which components have finished
fixationComponents = []
fixationComponents.append(fix)
for thisComponent in fixationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "fixation"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *fix* updates
    if t >= 0.0 and fix.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix.tStart = t  # underestimates by a little under one frame
        fix.frameNStart = frameN  # exact frame index
        fix.setAutoDraw(True)
    elif fix.status == STARTED and t >= (0.0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
        fix.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


#------Prepare to start Routine "cue_4"-------
t = 0
cue_4Clock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
cue_4Components = []
cue_4Components.append(Cue4)
for thisComponent in cue_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "cue_4"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = cue_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cue4* updates
    if t >= 0.0 and Cue4.status == NOT_STARTED:
        # keep track of start time/frame for later
        Cue4.tStart = t  # underestimates by a little under one frame
        Cue4.frameNStart = frameN  # exact frame index
        Cue4.setAutoDraw(True)
    elif Cue4.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        Cue4.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cue_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "cue_4"-------
for thisComponent in cue_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(condition_file),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial_4"-------
    t = 0
    trial_4Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    sound_9.setSound(trial4)
    selfrel_resp_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    selfrel_resp_9.status = NOT_STARTED
    # keep track of which components have finished
    trial_4Components = []
    trial_4Components.append(ISI_9)
    trial_4Components.append(sound_9)
    trial_4Components.append(selfrel_resp_9)
    trial_4Components.append(fix4)
    for thisComponent in trial_4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial_4"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_9
        if t >= 0.5 and sound_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_9.tStart = t  # underestimates by a little under one frame
            sound_9.frameNStart = frameN  # exact frame index
            sound_9.play()  # start the sound (it finishes automatically)
        elif sound_9.status == STARTED and t >= (0.5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_9.stop()  # stop the sound (if longer than duration)
        
        # *selfrel_resp_9* updates
        if t >= 0.5 and selfrel_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            selfrel_resp_9.tStart = t  # underestimates by a little under one frame
            selfrel_resp_9.frameNStart = frameN  # exact frame index
            selfrel_resp_9.status = STARTED
            # keyboard checking is just starting
            selfrel_resp_9.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif selfrel_resp_9.status == STARTED and t >= (0.5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            selfrel_resp_9.status = STOPPED
        if selfrel_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', 'num_1', 'num_2', 'num_3', 'num_4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                selfrel_resp_9.keys = theseKeys[-1]  # just the last key pressed
                selfrel_resp_9.rt = selfrel_resp_9.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *fix4* updates
        if t >= 0.0 and fix4.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix4.tStart = t  # underestimates by a little under one frame
            fix4.frameNStart = frameN  # exact frame index
            fix4.setAutoDraw(True)
        elif fix4.status == STARTED and t >= (0.0 + (3.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix4.setAutoDraw(False)
        # *ISI_9* period
        if t >= 0.0 and ISI_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_9.tStart = t  # underestimates by a little under one frame
            ISI_9.frameNStart = frameN  # exact frame index
            ISI_9.start(0.5)
        elif ISI_9.status == STARTED: #one frame should pass before updating params and completing
            ISI_9.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial_4"-------
    for thisComponent in trial_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if selfrel_resp_9.keys in ['', [], None]:  # No response was made
       selfrel_resp_9.keys=None
    # store data for trials (TrialHandler)
    trials.addData('selfrel_resp_9.keys',selfrel_resp_9.keys)
    if selfrel_resp_9.keys != None:  # we had a response
        trials.addData('selfrel_resp_9.rt', selfrel_resp_9.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(10.000000)
# update component parameters for each repeat

# keep track of which components have finished
fixationComponents = []
fixationComponents.append(fix)
for thisComponent in fixationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "fixation"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *fix* updates
    if t >= 0.0 and fix.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix.tStart = t  # underestimates by a little under one frame
        fix.frameNStart = frameN  # exact frame index
        fix.setAutoDraw(True)
    elif fix.status == STARTED and t >= (0.0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
        fix.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


#------Prepare to start Routine "cue_5"-------
t = 0
cue_5Clock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
cue_5Components = []
cue_5Components.append(Cue5)
for thisComponent in cue_5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "cue_5"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = cue_5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cue5* updates
    if t >= 0.0 and Cue5.status == NOT_STARTED:
        # keep track of start time/frame for later
        Cue5.tStart = t  # underestimates by a little under one frame
        Cue5.frameNStart = frameN  # exact frame index
        Cue5.setAutoDraw(True)
    elif Cue5.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        Cue5.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cue_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "cue_5"-------
for thisComponent in cue_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trial5_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(condition_file),
    seed=None, name='trial5_loop')
thisExp.addLoop(trial5_loop)  # add the loop to the experiment
thisTrial5_loop = trial5_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial5_loop.rgb)
if thisTrial5_loop != None:
    for paramName in thisTrial5_loop.keys():
        exec(paramName + '= thisTrial5_loop.' + paramName)

for thisTrial5_loop in trial5_loop:
    currentLoop = trial5_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrial5_loop.rgb)
    if thisTrial5_loop != None:
        for paramName in thisTrial5_loop.keys():
            exec(paramName + '= thisTrial5_loop.' + paramName)
    
    #------Prepare to start Routine "trial_5"-------
    t = 0
    trial_5Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    sound_10.setSound(trial5)
    selfrel_resp_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    selfrel_resp_10.status = NOT_STARTED
    # keep track of which components have finished
    trial_5Components = []
    trial_5Components.append(ISI_10)
    trial_5Components.append(sound_10)
    trial_5Components.append(selfrel_resp_10)
    trial_5Components.append(fix5)
    for thisComponent in trial_5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial_5"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_10
        if t >= 0.5 and sound_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_10.tStart = t  # underestimates by a little under one frame
            sound_10.frameNStart = frameN  # exact frame index
            sound_10.play()  # start the sound (it finishes automatically)
        elif sound_10.status == STARTED and t >= (0.5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_10.stop()  # stop the sound (if longer than duration)
        
        # *selfrel_resp_10* updates
        if t >= 0.5 and selfrel_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            selfrel_resp_10.tStart = t  # underestimates by a little under one frame
            selfrel_resp_10.frameNStart = frameN  # exact frame index
            selfrel_resp_10.status = STARTED
            # keyboard checking is just starting
            selfrel_resp_10.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif selfrel_resp_10.status == STARTED and t >= (0.5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            selfrel_resp_10.status = STOPPED
        if selfrel_resp_10.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', 'num_1', 'num_2', 'num_3', 'num_4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                selfrel_resp_10.keys = theseKeys[-1]  # just the last key pressed
                selfrel_resp_10.rt = selfrel_resp_10.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *fix5* updates
        if t >= 0.0 and fix5.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix5.tStart = t  # underestimates by a little under one frame
            fix5.frameNStart = frameN  # exact frame index
            fix5.setAutoDraw(True)
        elif fix5.status == STARTED and t >= (0.0 + (3.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix5.setAutoDraw(False)
        # *ISI_10* period
        if t >= 0.0 and ISI_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_10.tStart = t  # underestimates by a little under one frame
            ISI_10.frameNStart = frameN  # exact frame index
            ISI_10.start(0.5)
        elif ISI_10.status == STARTED: #one frame should pass before updating params and completing
            ISI_10.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial_5"-------
    for thisComponent in trial_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if selfrel_resp_10.keys in ['', [], None]:  # No response was made
       selfrel_resp_10.keys=None
    # store data for trial5_loop (TrialHandler)
    trial5_loop.addData('selfrel_resp_10.keys',selfrel_resp_10.keys)
    if selfrel_resp_10.keys != None:  # we had a response
        trial5_loop.addData('selfrel_resp_10.rt', selfrel_resp_10.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trial5_loop'


#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(10.000000)
# update component parameters for each repeat

# keep track of which components have finished
fixationComponents = []
fixationComponents.append(fix)
for thisComponent in fixationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "fixation"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *fix* updates
    if t >= 0.0 and fix.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix.tStart = t  # underestimates by a little under one frame
        fix.frameNStart = frameN  # exact frame index
        fix.setAutoDraw(True)
    elif fix.status == STARTED and t >= (0.0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
        fix.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


#------Prepare to start Routine "cue_6"-------
t = 0
cue_6Clock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
cue_6Components = []
cue_6Components.append(Cue6)
for thisComponent in cue_6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "cue_6"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = cue_6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Cue6* updates
    if t >= 0.0 and Cue6.status == NOT_STARTED:
        # keep track of start time/frame for later
        Cue6.tStart = t  # underestimates by a little under one frame
        Cue6.frameNStart = frameN  # exact frame index
        Cue6.setAutoDraw(True)
    elif Cue6.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        Cue6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cue_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "cue_6"-------
for thisComponent in cue_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trial6_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(condition_file),
    seed=None, name='trial6_loop')
thisExp.addLoop(trial6_loop)  # add the loop to the experiment
thisTrial6_loop = trial6_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial6_loop.rgb)
if thisTrial6_loop != None:
    for paramName in thisTrial6_loop.keys():
        exec(paramName + '= thisTrial6_loop.' + paramName)

for thisTrial6_loop in trial6_loop:
    currentLoop = trial6_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrial6_loop.rgb)
    if thisTrial6_loop != None:
        for paramName in thisTrial6_loop.keys():
            exec(paramName + '= thisTrial6_loop.' + paramName)
    
    #------Prepare to start Routine "trial_6"-------
    t = 0
    trial_6Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    sound_11.setSound(trial6)
    selfrel_resp_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    selfrel_resp_11.status = NOT_STARTED
    # keep track of which components have finished
    trial_6Components = []
    trial_6Components.append(ISI_11)
    trial_6Components.append(sound_11)
    trial_6Components.append(selfrel_resp_11)
    trial_6Components.append(fix6)
    for thisComponent in trial_6Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial_6"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_6Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_11
        if t >= 0.5 and sound_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_11.tStart = t  # underestimates by a little under one frame
            sound_11.frameNStart = frameN  # exact frame index
            sound_11.play()  # start the sound (it finishes automatically)
        elif sound_11.status == STARTED and t >= (0.5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_11.stop()  # stop the sound (if longer than duration)
        
        # *selfrel_resp_11* updates
        if t >= 0.5 and selfrel_resp_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            selfrel_resp_11.tStart = t  # underestimates by a little under one frame
            selfrel_resp_11.frameNStart = frameN  # exact frame index
            selfrel_resp_11.status = STARTED
            # keyboard checking is just starting
            selfrel_resp_11.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif selfrel_resp_11.status == STARTED and t >= (0.5 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            selfrel_resp_11.status = STOPPED
        if selfrel_resp_11.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', 'num_1', 'num_2', 'num_3', 'num_4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                selfrel_resp_11.keys = theseKeys[-1]  # just the last key pressed
                selfrel_resp_11.rt = selfrel_resp_11.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *fix6* updates
        if t >= 0.0 and fix6.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix6.tStart = t  # underestimates by a little under one frame
            fix6.frameNStart = frameN  # exact frame index
            fix6.setAutoDraw(True)
        elif fix6.status == STARTED and t >= (0.0 + (3.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fix6.setAutoDraw(False)
        # *ISI_11* period
        if t >= 0.0 and ISI_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_11.tStart = t  # underestimates by a little under one frame
            ISI_11.frameNStart = frameN  # exact frame index
            ISI_11.start(0.5)
        elif ISI_11.status == STARTED: #one frame should pass before updating params and completing
            ISI_11.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial_6"-------
    for thisComponent in trial_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if selfrel_resp_11.keys in ['', [], None]:  # No response was made
       selfrel_resp_11.keys=None
    # store data for trial6_loop (TrialHandler)
    trial6_loop.addData('selfrel_resp_11.keys',selfrel_resp_11.keys)
    if selfrel_resp_11.keys != None:  # we had a response
        trial6_loop.addData('selfrel_resp_11.rt', selfrel_resp_11.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trial6_loop'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(done)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *done* updates
    if t >= 0.0 and done.status == NOT_STARTED:
        # keep track of start time/frame for later
        done.tStart = t  # underestimates by a little under one frame
        done.frameNStart = frameN  # exact frame index
        done.setAutoDraw(True)
    elif done.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        done.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

win.close()
core.quit()
