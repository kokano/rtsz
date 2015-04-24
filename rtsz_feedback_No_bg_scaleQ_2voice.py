#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.00)
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
from math import floor

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'rtsz_feedback'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001','max':'','min':'','mid':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data\%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])  

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
win = visual.Window(size=(800, 600), fullscr=False, screen=1, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg',
    )
# store frame rate of monitor if we can measure it successfully
#expInfo['frameRate']=win.getActualFrameRate()
#if expInfo['frameRate']!=None:
#    frameDur = 1.0/round(expInfo['frameRate'])
#else:
frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "pretrigger_instr"
pretrigger_instrClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'In this task you will be asked to either attend to your own voice or ignore all sounds including the voices and any other noise in the environment.\n\nWhen ignoring sounds, you may use a strategy suggested by the experimenter or a strategy you came up with on your own. \n\nWhen you are ready please press the "YES" button.',    font=u'Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
show_feedback= True
if expInfo['session'][-1] == '1' or expInfo['session'][-1] == '8':
    show_feedback = False
condition_file=os.path.join('schedules','realtime_run00%s_%s.csv'%(expInfo['session'][-1],expInfo['participant']))
#instruction_text=''
#voice_file=''
init_baseline=30 #put this back for real experiment!!
#init_baseline=5 #PILOT_TEST
if expInfo['participant']=='test':
    init_baseline=3

#!/usr/bin/python

import math
import socket
import re
import random

class Murfi:
	def __init__(self, ip, port, tr, fake):
		self.IP = ip
		self.PORT = port
		self.TR = tr
		self.FAKE = fake
	
		self.FB_roi = [float('NaN')] * self.TR
		self.FB_bg = [float('NaN')] * self.TR
		#self.FB_FFA = [0] * self.TR
		#self.FB_PPA = [0] * self.TR
        
		self.roi_query = '<?xml version="1.0" encoding="UTF-8"?><info><get dataid=":*:*:*:__TR__:*:*:roi-weightedave:stg:"></get></info>\n'
		self.bg_query = '<?xml version="1.0" encoding="UTF-8"?><info><get dataid=":*:*:*:__TR__:*:*:roi-weightedave:non:"></get></info>\n'
	
	def sendQ(self, Q):
		if not self.FAKE:		
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((self.IP, self.PORT))
			s.send(Q)
			A = s.recv(4096)
			s.close()
			return A
		else:
			return str(random.gauss(0,1))

	def stripA(self, A):	
		Astrip = re.sub("<.*?>","",A)
		#print "Astrip: ", Astrip
		try:
			stripped = float(Astrip)
		except ValueError:
			stripped = float('nan')
		#print "Stripped is returning: ", stripped
		return stripped

	# These are 1-indexed (like murfi)
	def Q_roi(self, tr):
		if tr>self.TR:
			print "Q_roi(self, tr): ERROR: TR Out of Bounds"
			return		
		thisQ = self.roi_query.replace('__TR__', str(tr))				
		A = self.sendQ(thisQ)
		self.FB_roi[tr-1] = self.stripA(A)		
	
	# These are 1-indexed (like murfi)	
	def Q_bg(self, tr):
		if tr>self.TR:
			print "Q_bg(self, tr): ERROR: TR Out of Bounds"
			return	
		thisQ = self.bg_query.replace('__TR__', str(tr))
		A = self.sendQ(thisQ)	
		self.FB_bg[tr-1] = self.stripA(A)

	def update(self):
		#print "UPDATE START"
		roi_tr = self.TR-1
		for ii in range(0, self.TR-1):
			#print "ii:",  ii
			if math.isnan(self.FB_roi[ii]):
				roi_tr = ii
				break
		
		bg_tr = self.TR-1
		for ii in range(0, self.TR-1):
			#print "ii:",  ii
			if math.isnan(self.FB_bg[ii]):
				bg_tr = ii
				break

		#print "ffa_tr:", ffa_tr
		#print "ppa_tr:", ppa_tr
		
		for ii in range(roi_tr, self.TR-1):
			#print "Q_ffa:", ii			
			self.Q_roi(ii+1)
			if math.isnan(self.FB_roi[ii]):
				break

		for ii in range(bg_tr, self.TR-1):
			self.Q_bg(ii+1)

			if math.isnan(self.FB_bg[ii]):
				break
		return

#murfi_IP = '192.168.2.5'
murfi_IP='18.189.24.205'
murfi_PORT = 15001
murfi_TR = 108

#murfi_FAKE = False

murfi_FAKE = True
if murfi_FAKE:
    print "::::IN DEBUG MODE.RUNNING MURFI SIMULATOR::::"

murfi = Murfi(murfi_IP, murfi_PORT, murfi_TR, murfi_FAKE)
murfi.update()

#create output data file
datFile=open('data'+os.path.sep+'rtsz_feedback_%s_dat_%s.txt'%(expInfo['participant'],expInfo['date']),'w')


# Initialize components for Routine "trigger"
triggerClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'waiting for scanner trigger\n',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
image = visual.ImageStim(win=win, name='image',
    image=os.path.join('stimulus','fixation.png'), mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "instruction"
instructionClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "transition"
transitionClock = core.Clock()
image_2 = visual.ImageStim(win=win, name='image_2',
    image=os.path.join('stimulus','fixation.png'), mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "stimulus_1"
stimulus_1Clock = core.Clock()
image_3 = visual.ImageStim(win=win, name='image_3',
    image=os.path.join('stimulus','fixation.png'), mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
sound_1 = sound.Sound('A', secs=3.5)
sound_1.setVolume(1)

# Initialize components for Routine "transition"
transitionClock = core.Clock()
image_2 = visual.ImageStim(win=win, name='image_2',
    image=os.path.join('stimulus','fixation.png'), mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "stimulus_2"
stimulus_2Clock = core.Clock()
image_6 = visual.ImageStim(win=win, name='image_6',
    image=os.path.join('stimulus','fixation.png'), mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
sound_2 = sound.Sound('A', secs=3.5)
sound_2.setVolume(1)

# Initialize components for Routine "transition"
transitionClock = core.Clock()
image_2 = visual.ImageStim(win=win, name='image_2',
    image=os.path.join('stimulus','fixation.png'), mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "stimulus_3"
stimulus_3Clock = core.Clock()
image_7 = visual.ImageStim(win=win, name='image_7',
    image=os.path.join('stimulus','fixation.png'), mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
sound_3 = sound.Sound('A', secs=3.5)
sound_3.setVolume(1)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
rating = visual.RatingScale(win=win, name='rating', marker='triangle',size=1.0, pos=[0.0,-0.3], low = 1, high =  6, labels=['Completely','Not at all'],markerStart='3.5', leftKeys='1',rightKeys='2',scale=None)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
image_8 = visual.ImageStim(win=win, name='image_8',
    image=os.path.join('stimulus','fixation.png'), mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
image_5 = visual.ImageStim(win=win, name='image_5',
    image=os.path.join('stimulus','fixation.png'), mask=None,
    ori=0, pos=[0, 0], size=[.5,.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "end"
endClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "pretrigger_instr"-------
t = 0
pretrigger_instrClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED

# keep track of which components have finished
pretrigger_instrComponents = []
pretrigger_instrComponents.append(key_resp_2)
pretrigger_instrComponents.append(text)
for thisComponent in pretrigger_instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pretrigger_instr"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pretrigger_instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
        theseKeys = event.getKeys(keyList=['space','num_1','1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pretrigger_instrComponents:
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

#-------Ending Routine "pretrigger_instr"-------
for thisComponent in pretrigger_instrComponents:
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
trigger_button = event.BuilderKeyResponse()  # create an object of type KeyResponse
trigger_button.status = NOT_STARTED
# keep track of which components have finished
triggerComponents = []
triggerComponents.append(trigger_button)
triggerComponents.append(text_2)
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
    
    # *trigger_button* updates
    if t >= 0.0 and trigger_button.status == NOT_STARTED:
        # keep track of start time/frame for later
        trigger_button.tStart = t  # underestimates by a little under one frame
        trigger_button.frameNStart = frameN  # exact frame index
        trigger_button.status = STARTED
        # keyboard checking is just starting
        trigger_button.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if trigger_button.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', 't'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            trigger_button.keys = theseKeys[-1]  # just the last key pressed
            trigger_button.rt = trigger_button.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
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
    else:  # this Routine was not non-slip safe so reset non-slip timer+++
        routineTimer.reset()

#-------Ending Routine "trigger"-------
for thisComponent in triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trigger_button.keys in ['', [], None]:  # No response was made
   trigger_button.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('trigger_button.keys',trigger_button.keys)
if trigger_button.keys != None:  # we had a response
    thisExp.addData('trigger_button.rt', trigger_button.rt)
thisExp.nextEntry()

#------Prepare to start Routine "baseline"-------
t = 0
baselineClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# Initialize components for Routine "feedback"
#vector_indices=[[17,34],[45,62],[73,90],[101,118]]
vector_indices=[[17,28],[41,52],[65,76],[89,100]]
top_condition='listen to self'
bottom_condition='ignore all sounds'
self_other_conditions=[]
block_count=0
background_bar = visual.ShapeStim(win=win, name='background_bar', lineWidth=2.0, lineColor=(1.0,1.0,1.0), lineColorSpace='rgb',
pos=(0,0),size=1,opacity=1,depth=2,interpolate=True,vertices=((-.125,-.5),(.125,-.5),(.125,.5),(-.125,.5)))#, fillColor='white', fillColorSpace='rgb')
zero_val_line=visual.ShapeStim(win=win, name='zero_val_line', lineWidth=2.0, lineColor=(1.0,1.0,1.0),lineColorSpace='rgb',
pos=(0,0),size=1,opacity=1,depth=2,interpolate=True,vertices=((-.125,0),(.125,0)))
zero=visual.TextStim(win,text='0',font='', pos=(.155,0),depth=2,rgb=None,color=(1.0,1.0,1.0),colorSpace='rgb',opacity=1.0)
top_text=visual.TextStim(win,text='placeholder',pos=(.325,.5),depth=2,rgb=None,color=(1.0,1.0,1.0),colorSpace='rgb',opacity=1.0)
bottom_text=visual.TextStim(win,text='placeholder',pos=(.325,-.5),depth=2,rgb=None,color=(1.0,1.0,1.0),colorSpace='rgb',opacity=1.0)
top_star = visual.TextStim(win=win, ori=0, name='top_star',
    text=u'*',    font=u'Arial',
    pos=[.5, .5], height=0.5, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
bottom_star = visual.TextStim(win=win, ori=0, name='top_star',
    text=u'*',    font=u'Arial',
    pos=[.5, -.5], height=0.5, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
# keep track of which components have finished
baselineComponents = []
baselineComponents.append(image)
for thisComponent in baselineComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
def makeFBrecs(zero_val,fb,fillColor=None,xoffset=0):
    if instruction_text=='ignore all sounds':
        if fb >=zero_val:
            rec_height=1*(fb-zero_val)/(30*(max-zero_val))*.5
            for idx in range(30):
                rec=visual.ShapeStim(win, closeShape=True, vertices=((xoffset-.125,idx*rec_height),(xoffset+.125,idx*rec_height),(xoffset+.125,(idx+1)*rec_height),(xoffset-.125,(idx+1)*rec_height)),depth=-3,opacity=1,fillColor='Red',lineColor='Red')
                recs.append(rec)
        elif fb<zero_val:
            rec_height=(fb-zero_val)/(30*(min-zero_val))*.5
            for idx in range(30):
            #rec=visual.ShapeStim(win, closeShape=True, vertices=((-.125,idx*rec_height),(.125,idx*rec_height),(.125,(idx+1)*rec_height),(-.125,(idx+1)*rec_height),depth=1,opacity=1,fillColor='Green')
                rec=visual.ShapeStim(win, closeShape=True, vertices=((xoffset-.125,idx*-1*rec_height),(xoffset+.125,idx*-1*rec_height),(xoffset+.125,(idx+1)*-1*rec_height),(xoffset-.125,(idx+1)*-1*rec_height)),depth=-3,opacity=1,fillColor='Green',lineColor='Green')
                recs.append(rec)
     #   if fb <=zero_val:
      #      rec_height=-1*(fb-zero_val)/(30*(max-zero_val))*.5
      #      for idx in range(30):
      #          rec=visual.ShapeStim(win, closeShape=True, vertices=((-.125,idx*rec_height),(.125,idx*rec_height),(.125,(idx+1)*rec_height),(-.125,(idx+1)*rec_height)),depth=-3,opacity=1,fillColor='Green',lineColor='Green')
      #          recs.append(rec)
      #  elif fb>zero_val:
      #      rec_height=-1*(fb-zero_val)/(30*(min-zero_val))*.5
      #      for idx in range(30):
      #      #rec=visual.ShapeStim(win, closeShape=True, vertices=((-.125,idx*rec_height),(.125,idx*rec_height),(.125,(idx+1)*rec_height),(-.125,(idx+1)*rec_height),depth=1,opacity=1,fillColor='Green')
      #          rec=visual.ShapeStim(win, closeShape=True, vertices=((-.125,idx*-1*rec_height),(.125,idx*-1*rec_height),(.125,(idx+1)*-1*rec_height),(-.125,(idx+1)*-1*rec_height)),depth=-3,opacity=1,fillColor='Red',lineColor='Red')
      #          recs.append(rec)
    if instruction_text=='listen to self':
        if fb >=zero_val:
            rec_height=1*(fb-zero_val)/(30*(max-zero_val))*.5
            for idx in range(30):
                rec=visual.ShapeStim(win, closeShape=True, vertices=((xoffset-.125,idx*rec_height),(xoffset+.125,idx*rec_height),(xoffset+.125,(idx+1)*rec_height),(xoffset-.125,(idx+1)*rec_height)),depth=-3,opacity=1,fillColor='Green',lineColor='Green')
                recs.append(rec)
        elif fb<zero_val:
            rec_height=(fb-zero_val)/(30*(min-zero_val))*.5
            for idx in range(30):
            #rec=visual.ShapeStim(win, closeShape=True, vertices=((-.125,idx*rec_height),(.125,idx*rec_height),(.125,(idx+1)*rec_height),(-.125,(idx+1)*rec_height),depth=1,opacity=1,fillColor='Green')
                rec=visual.ShapeStim(win, closeShape=True, vertices=((xoffset-.125,idx*-1*rec_height),(xoffset+.125,idx*-1*rec_height),(xoffset+.125,(idx+1)*-1*rec_height),(xoffset-.125,(idx+1)*-1*rec_height)),depth=-3,opacity=1,fillColor='Red',lineColor='Red')
                recs.append(rec)
    return recs
#-------Start Routine "baseline"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = baselineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if t >= 0.0 and image.status == NOT_STARTED:
        # keep track of start time/frame for later
        image.tStart = t  # underestimates by a little under one frame
        image.frameNStart = frameN  # exact frame index
        image.setAutoDraw(True)
    elif image.status == STARTED and t >=((init_baseline)):
        image.setAutoDraw(False)
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baselineComponents:
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

#-------Ending Routine "baseline"-------
for thisComponent in baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# set up handler to look after randomisation of conditions etc
block_order = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(condition_file),
    seed=None, name='block_order')
thisExp.addLoop(block_order)  # add the loop to the experiment
thisBlock_order = block_order.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock_order.rgb)
if thisBlock_order != None:
    for paramName in thisBlock_order.keys():
        exec(paramName + '= thisBlock_order.' + paramName)

for thisBlock_order in block_order:
    currentLoop = block_order
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_order.rgb)
    if thisBlock_order != None:
        for paramName in thisBlock_order.keys():
            exec(paramName + '= thisBlock_order.' + paramName)
    
    #------Prepare to start Routine "instruction"-------
    t = 0
    instructionClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    text_3.setText(instruction_text)
    # keep track of which components have finished
    instructionComponents = []
    instructionComponents.append(text_3)
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instruction"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = instructionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        elif text_3.status == STARTED and t >= (0.0 + (2.0)): #most of one frame period left
            text_3.setAutoDraw(False)
        
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
    
    #-------Ending Routine "instruction"-------
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    voice_1 = data.TrialHandler(nReps=2, method='sequential', 
    #voice_1 = data.TrialHandler(nReps=1, method='sequential', #PILOT_TEST
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='voice_1')
    thisExp.addLoop(voice_1)  # add the loop to the experiment
    thisVoice_1 = voice_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisVoice_1.rgb)
    if thisVoice_1 != None:
        for paramName in thisVoice_1.keys():
            exec(paramName + '= thisVoice_1.' + paramName)
    
    for thisVoice_1 in voice_1:
        currentLoop = voice_1
        # abbreviate parameter names if possible (e.g. rgb = thisVoice_1.rgb)
        if thisVoice_1 != None:
            for paramName in thisVoice_1.keys():
                exec(paramName + '= thisVoice_1.' + paramName)
        
        #------Prepare to start Routine "transition"-------
        t = 0
        transitionClock.reset()  # clock 
        frameN = -1
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        transitionComponents = []
        transitionComponents.append(image_2)
        for thisComponent in transitionComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "transition"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = transitionClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_2* updates
            if t >= 0.0 and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t  # underestimates by a little under one frame
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            elif image_2.status == STARTED and t >= (0.0 + (.5)): #most of one frame period left
                image_2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in transitionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "transition"-------
        for thisComponent in transitionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        #------Prepare to start Routine "stimulus_1"-------
        t = 0
        stimulus_1Clock.reset()  # clock 
        frameN = -1
        routineTimer.add(3.500000)
        # update component parameters for each repeat
        sound_1.setSound(voice_file1)
        # keep track of which components have finished
        stimulus_1Components = []
        stimulus_1Components.append(image_3)
        stimulus_1Components.append(sound_1)
        for thisComponent in stimulus_1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "stimulus_1"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimulus_1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_3* updates
            if t >= 0.0 and image_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_3.tStart = t  # underestimates by a little under one frame
                image_3.frameNStart = frameN  # exact frame index
                image_3.setAutoDraw(True)
            elif image_3.status == STARTED and t >= (0.0 + (3.5)):#most of one frame period left
                image_3.setAutoDraw(False)
            # start/stop sound_1
            if t >= 0.0 and sound_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_1.tStart = t  # underestimates by a little under one frame
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.play()  # start the sound (it finishes automatically)
            elif sound_1.status == STARTED and t >= (0.0 + (3.5)): #most of one frame period left
                sound_1.stop()  # stop the sound (if longer than duration)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimulus_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "stimulus_1"-------
        for thisComponent in stimulus_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 3 repeats of 'voice_1'
    
    
    # set up handler to look after randomisation of conditions etc
    voice_2 = data.TrialHandler(nReps=2, method='sequential', 
    #voice_2 = data.TrialHandler(nReps=1, method='sequential', #PILOT_TEST
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='voice_2')
    thisExp.addLoop(voice_2)  # add the loop to the experiment
    thisVoice_2 = voice_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisVoice_2.rgb)
    if thisVoice_2 != None:
        for paramName in thisVoice_2.keys():
            exec(paramName + '= thisVoice_2.' + paramName)
    
    for thisVoice_2 in voice_2:
        currentLoop = voice_2
        # abbreviate parameter names if possible (e.g. rgb = thisVoice_2.rgb)
        if thisVoice_2 != None:
            for paramName in thisVoice_2.keys():
                exec(paramName + '= thisVoice_2.' + paramName)
        
        #------Prepare to start Routine "transition"-------
        t = 0
        transitionClock.reset()  # clock 
        frameN = -1
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        transitionComponents = []
        transitionComponents.append(image_2)
        for thisComponent in transitionComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "transition"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = transitionClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_2* updates
            if t >= 0.0 and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t  # underestimates by a little under one frame
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            elif image_2.status == STARTED and t >= (0.0 + (.5)): #most of one frame period left
                image_2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in transitionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "transition"-------
        for thisComponent in transitionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        #------Prepare to start Routine "stimulus_2"-------
        t = 0
        stimulus_2Clock.reset()  # clock 
        frameN = -1
        routineTimer.add(3.500000)
        # update component parameters for each repeat
        sound_2.setSound(voice_file2)
        # keep track of which components have finished
        stimulus_2Components = []
        stimulus_2Components.append(image_6)
        stimulus_2Components.append(sound_2)
        for thisComponent in stimulus_2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "stimulus_2"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimulus_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_6* updates
            if t >= 0.0 and image_6.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_6.tStart = t  # underestimates by a little under one frame
                image_6.frameNStart = frameN  # exact frame index
                image_6.setAutoDraw(True)
            elif image_6.status == STARTED and t >= (0.0 + (3.5)): #most of one frame period left
                image_6.setAutoDraw(False)
            # start/stop sound_2
            if t >= 0.0 and sound_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_2.tStart = t  # underestimates by a little under one frame
                sound_2.frameNStart = frameN  # exact frame index
                sound_2.play()  # start the sound (it finishes automatically)
            elif sound_2.status == STARTED and t >= (0.0 + (3.5)): #most of one frame period left
                sound_2.stop()  # stop the sound (if longer than duration)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimulus_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "stimulus_2"-------
        for thisComponent in stimulus_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 3 repeats of 'voice_2'
    
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=2, method='sequential', 
    #trials = data.TrialHandler(nReps=1, method='sequential', #PILOT_TEST
        extraInfo=expInfo, originPath=None,
        trialList=[None],
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
        
    #------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock 
    frameN = -1
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    text_4.setText(question)
    murfi.update()
    
    # keep track of which components have finished
    fixationComponents = []
    fixationComponents.append(text_4)
    fixationComponents.append(rating)    
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
            
    
    #-------Start Routine "fixation"-------
    continueRoutine = True
    rating.reset()
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        elif text_4.status == STARTED and t >= (0.0 + (4.0)): #most of one frame period left
            text_4.setAutoDraw(False)
        
        #*rating* updates
        if t > 0.0:
            rating.draw()
            continueRoutine = rating.noResponse
            if rating.noResponse == True:
                #rating.response = rating.getRating()
                #rating.rt = rating.getRT()
                lastRating=rating.getHistory()[-1]
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            lastRating=rs.getHistory()[-1]
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
    # store data for block_order (TrialHandler)
    #thisExp.addData('rating.response', rating.getRating())
    #thisExp.addData('rating.rt', rating.getRT())
    thisExp.addData('lastRating',lastRating)
    thisExp.nextEntry()
    murfi.update()
    #push to datFile
    datFile.write('%s\t%s\t%s\n'%(expInfo['participant'],instruction_text,lastRating))
# completed 1 repeats of 'block_order'

    #------Prepare to start Routine "feedback"-------
    feedbackComponents = []
    feedbackComponents.append(image_8)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    feedbackClock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    if show_feedback==False:
        image_8.setOpacity(1)
    else:
        image_8.setOpacity(0)
        feedbackComponents.append(background_bar)
        feedbackComponents.append(zero_val_line)
        feedbackComponents.append(zero)
        feedbackComponents.append(top_text)
        feedbackComponents.append(bottom_text)
        if instruction_text=='listen to self':
            top_text.setText('listen to self')
            bottom_text.setText('ignore all sounds')
            self_other_conditions.append('listen to self')
            feedbackComponents.append(top_star)
        elif instruction_text=='ignore all sounds':
            top_text.setText('listen to self')
            bottom_text.setText('ignore all sounds')
            self_other_conditions.append('ignore all sounds')
            feedbackComponents.append(bottom_star)
        feedbackClock.reset()  # clock 
        frameN = 0
        routineTimer.add(4.000000)
        murfi.update()
        # update component parameters for each repeat
        if instruction_text=='ignore all sounds':
            top_text.setText('listen to self')
            bottom_text.setText('ignore all sounds')
            feedbackComponents.append('bottom_star')
            max=float(expInfo['max'])
            min=float(expInfo['min'])
            zero_val=float(expInfo['mid'])
            #zero_val=float(0)
            #zero_val=np.mean(float(expInfo['max']))-(float(expInfo['min']))
            index1= int(vector_indices[block_count][0])
            index2= int(vector_indices[block_count][1])
            roi_vector=np.array(murfi.FB_roi[index1:index2])
            #bg_vector=np.array(murfi.FB_bg[index1:index2])
            indices_to_remove=[]
            for idx,val in enumerate(roi_vector):
                if math.isnan(roi_vector[idx]): #or math.isnan(bg_vector[idx]):
                    indices_to_remove.append(idx)
            roi_vector_vector=np.delete(roi_vector,indices_to_remove)
            #bg_vector_vector=np.delete(bg_vector,indices_to_remove)
            fb_average=np.median(np.array(roi_vector_vector))#-np.array(bg_vector_vector))
        elif instruction_text =='listen to self':
            top_text.setText('listen to self')
            bottom_text.setText('ignore all sounds')
            max=float(expInfo['max'])
            min=float(expInfo['min'])
            #zero_val=float(expInfo['mid'])
            #zero_val=float(0)
            zero_val=np.mean(float(expInfo['max']))-(float(expInfo['min']))
            feedbackComponents.append('top_star')
            index1= int(vector_indices[block_count][0])
            index2= int(vector_indices[block_count][1])
            roi_vector=np.array(murfi.FB_roi[index1:index2])
            #bg_vector=np.array(murfi.FB_bg[index1:index2])
            indices_to_remove=[]
            for idx,val in enumerate(roi_vector):
                if math.isnan(roi_vector[idx]): # or math.isnan(bg_vector[idx]):
                    indices_to_remove.append(idx)
            roi_vector_vector=np.delete(roi_vector,indices_to_remove)
            #bg_vector_vector=np.delete(bg_vector,indices_to_remove)
            fb_average=np.median(np.array(roi_vector_vector))#-np.array(bg_vector_vector))
        print instruction_text
        print block_count
        print index1
        print index2
        print roi_vector
        #print bg_vector
        print fb_average 
        #print roi_vector
        #print bg_vector
        #print (np.array(roi_vector_vector)-np.array(bg_vector_vector))
        fb=[]
        if fb_average > max:
           fb = max
        elif fb_average< min:
           fb = min
        else:
           fb = fb_average
        rec=[]
        recs=[]
        recs=makeFBrecs(zero_val,fb,fillColor=None)
    # keep track of which components have finished

    
    #-------Start Routine "feedback"-------
    frameN=-1
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        if show_feedback==False:
            continue
        else:
            # *patch_2* updates
            if t >= 0.0:
                # keep track of start time/frame for later
                background_bar.setAutoDraw(True)
                zero_val_line.setAutoDraw(True)
                zero.setAutoDraw(True)
                top_text.setAutoDraw(True)
                bottom_text.setAutoDraw(True)
                if instruction_text=='ignore all sounds':
                    bottom_star.setAutoDraw(True)
                    
                elif instruction_text=='listen to self':
                    top_star.setAutoDraw(True)
                if show_feedback==False:
                    image_8.setAutoDraw(True)
            
                
            #elif patch_2.status == STARTED and t >= (0.0 + 4):
            elif t >=(0.0+4):
                background_bar.setAutoDraw(False)
                zero_val_line.setAutoDraw(False)
                zero.setAutoDraw(False)
                bottom_text.setAutoDraw(False)
                top_text.setAutoDraw(False)
                try:
                    bottom_star.setAutoDraw(False)
                    top_star.setAutoDraw(False)
                    image_8.setAutoDraw(False)
                except:
                    continue
            if frameN>=30:
                max_idx=30
            else:
                max_idx=floor(frameN)
        if show_feedback==False:
            continue
        else:
            if int(max_idx)>1:
                for idx in range(int(max_idx)):
                    recs[idx].setAutoDraw(True)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        if show_feedback==False:
            continue
        else:
            for idx in range(30):
                recs[idx].setAutoDraw(False)
        #-------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
    
    #------Prepare to start Routine "fixation_2"-------
    t = 0
    fixation_2Clock.reset()  # clock 
    frameN = -1
    if show_feedback==False:
        fixation_duration=15
    else:
        fixation_duration=11
    routineTimer.add(fixation_duration)
    # update component parameters for each repeat
    block_count=block_count+1
    # keep track of which components have finished
    fixation_2Components = []
    fixation_2Components.append(image_5)
    for thisComponent in fixation_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fixation_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if t >= 0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t  # underestimates by a little under one frame
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        elif image_5.status == STARTED and t >= (0 + (fixation_duration)): #most of one frame period left
            image_5.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fixation_2"-------
    for thisComponent in fixation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
   

#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




datFile.close()
win.close()
core.quit()
