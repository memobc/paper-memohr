#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.06),
    on Thu Jun  1 11:12:44 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'recognition'  # from the Builder filename that created this script
expInfo = {u'participant': u'practice', u'condition': u'A'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Volumes/External/MemoHR/Scripts/share/task/recognition_practice.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(2560, 1440), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instrux = visual.TextStim(win=win, name='instrux',
    text='Determine whether the item is remembered, familiar, or new.\nThen select which question you answered about the image yesterday,\nand rate your confidence.\n\nPress any key to continue.',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "takebreak"
takebreakClock = core.Clock()
takeBreak = visual.TextStim(win=win, name='takeBreak',
    text='Take a break.\n\nPress any key to continue.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "itemrec"
itemrecClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
image_2 = visual.ImageStim(
    win=win, name='image_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1000, 750],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
scale_itemrec = visual.TextStim(win=win, name='scale_itemrec',
    text='OLD OR NEW?\nV: REMEMBER -- B: FAMILIAR -- N: NEW',
    font='Arial',
    pos=[0, -.9], height=0.08, wrapWidth=1600, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-2.0);
fixISI = visual.TextStim(win=win, name='fixISI',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "sourcerec"
sourcerecClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1000, 750],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
scale_sourcerec = visual.TextStim(win=win, name='scale_sourcerec',
    text='WHICH QUESTION?\nV: in SF -- B: prof. photog.',
    font='Arial',
    pos=[0, -.9], height=0.08, wrapWidth=1600, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "sourceconf"
sourceconfClock = core.Clock()
image_3 = visual.ImageStim(
    win=win, name='image_3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1000, 750],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
scale_sourceconf = visual.TextStim(win=win, name='scale_sourceconf',
    text='CONFIDENCE?\nV: SURE -- B: UNSURE',
    font='Arial',
    pos=[0, -.9], height=0.08, wrapWidth=1600, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "fixationISI"
fixationISIClock = core.Clock()
fixation_2 = visual.TextStim(win=win, name='fixation_2',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "finished"
finishedClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You are now finished with the experiment.\n',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instruxResp = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [instrux, instruxResp]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrux* updates
    if t >= 0.0 and instrux.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrux.tStart = t
        instrux.frameNStart = frameN  # exact frame index
        instrux.setAutoDraw(True)
    
    # *instruxResp* updates
    if t >= 0.0 and instruxResp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruxResp.tStart = t
        instruxResp.frameNStart = frameN  # exact frame index
        instruxResp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instruxResp.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('lists/s'+expInfo['participant']+'/'+expInfo['condition']+'_recognition.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "takebreak"-------
    t = 0
    takebreakClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    breakResp = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    takebreakComponents = [takeBreak, breakResp]
    for thisComponent in takebreakComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "takebreak"-------
    while continueRoutine:
        # get current time
        t = takebreakClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *takeBreak* updates
        if t >= 0.0 and takeBreak.status == NOT_STARTED:
            # keep track of start time/frame for later
            takeBreak.tStart = t
            takeBreak.frameNStart = frameN  # exact frame index
            takeBreak.setAutoDraw(True)
        
        # *breakResp* updates
        if t >= 0.0 and breakResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            breakResp.tStart = t
            breakResp.frameNStart = frameN  # exact frame index
            breakResp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if breakResp.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        if trials.thisTrialN not in [66,132,198]:
            continueRoutine=False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in takebreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "takebreak"-------
    for thisComponent in takebreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "takebreak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "itemrec"-------
    t = 0
    itemrecClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    image_2.setImage(ImageFile)
    response_itemrec = event.BuilderKeyResponse()
    # keep track of which components have finished
    itemrecComponents = [ISI, image_2, scale_itemrec, response_itemrec, fixISI]
    for thisComponent in itemrecComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "itemrec"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = itemrecClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if t >= 0.5 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        frameRemains = 0.5 + 4.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_2.status == STARTED and t >= frameRemains:
            image_2.setAutoDraw(False)
        
        # *scale_itemrec* updates
        if t >= 0.5 and scale_itemrec.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_itemrec.tStart = t
            scale_itemrec.frameNStart = frameN  # exact frame index
            scale_itemrec.setAutoDraw(True)
        frameRemains = 0.5 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if scale_itemrec.status == STARTED and t >= frameRemains:
            scale_itemrec.setAutoDraw(False)
        
        # *response_itemrec* updates
        if t >= 1 and response_itemrec.status == NOT_STARTED:
            # keep track of start time/frame for later
            response_itemrec.tStart = t
            response_itemrec.frameNStart = frameN  # exact frame index
            response_itemrec.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response_itemrec.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 1 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if response_itemrec.status == STARTED and t >= frameRemains:
            response_itemrec.status = STOPPED
        if response_itemrec.status == STARTED:
            theseKeys = event.getKeys(keyList=['v', 'b', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response_itemrec.keys = theseKeys[-1]  # just the last key pressed
                response_itemrec.rt = response_itemrec.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *fixISI* updates
        if t >= 0.0 and fixISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixISI.tStart = t
            fixISI.frameNStart = frameN  # exact frame index
            fixISI.setAutoDraw(True)
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixISI.status == STARTED and t >= frameRemains:
            fixISI.setAutoDraw(False)
        # *ISI* period
        if t >= 0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itemrecComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "itemrec"-------
    for thisComponent in itemrecComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_itemrec.keys in ['', [], None]:  # No response was made
        response_itemrec.keys=None
    trials.addData('response_itemrec.keys',response_itemrec.keys)
    if response_itemrec.keys != None:  # we had a response
        trials.addData('response_itemrec.rt', response_itemrec.rt)
    
    # ------Prepare to start Routine "sourcerec"-------
    t = 0
    sourcerecClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    response_sourcerec = event.BuilderKeyResponse()
    # keep track of which components have finished
    sourcerecComponents = [image, scale_sourcerec, response_sourcerec]
    for thisComponent in sourcerecComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "sourcerec"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = sourcerecClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 0 + 4.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # *scale_sourcerec* updates
        if t >= 0 and scale_sourcerec.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_sourcerec.tStart = t
            scale_sourcerec.frameNStart = frameN  # exact frame index
            scale_sourcerec.setAutoDraw(True)
        frameRemains = 0 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if scale_sourcerec.status == STARTED and t >= frameRemains:
            scale_sourcerec.setAutoDraw(False)
        
        # *response_sourcerec* updates
        if t >= 0 and response_sourcerec.status == NOT_STARTED:
            # keep track of start time/frame for later
            response_sourcerec.tStart = t
            response_sourcerec.frameNStart = frameN  # exact frame index
            response_sourcerec.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response_sourcerec.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0 + 4.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if response_sourcerec.status == STARTED and t >= frameRemains:
            response_sourcerec.status = STOPPED
        if response_sourcerec.status == STARTED:
            theseKeys = event.getKeys(keyList=['v', 'b', 'n', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response_sourcerec.keys = theseKeys[-1]  # just the last key pressed
                response_sourcerec.rt = response_sourcerec.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sourcerecComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sourcerec"-------
    for thisComponent in sourcerecComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_sourcerec.keys in ['', [], None]:  # No response was made
        response_sourcerec.keys=None
    trials.addData('response_sourcerec.keys',response_sourcerec.keys)
    if response_sourcerec.keys != None:  # we had a response
        trials.addData('response_sourcerec.rt', response_sourcerec.rt)
    
    # ------Prepare to start Routine "sourceconf"-------
    t = 0
    sourceconfClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    image_3.setImage(ImageFile)
    response_sourceconf = event.BuilderKeyResponse()
    # keep track of which components have finished
    sourceconfComponents = [image_3, scale_sourceconf, response_sourceconf]
    for thisComponent in sourceconfComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "sourceconf"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = sourceconfClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if t >= 0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        frameRemains = 0 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_3.status == STARTED and t >= frameRemains:
            image_3.setAutoDraw(False)
        
        # *scale_sourceconf* updates
        if t >= 0 and scale_sourceconf.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_sourceconf.tStart = t
            scale_sourceconf.frameNStart = frameN  # exact frame index
            scale_sourceconf.setAutoDraw(True)
        frameRemains = 0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if scale_sourceconf.status == STARTED and t >= frameRemains:
            scale_sourceconf.setAutoDraw(False)
        
        # *response_sourceconf* updates
        if t >= 0 and response_sourceconf.status == NOT_STARTED:
            # keep track of start time/frame for later
            response_sourceconf.tStart = t
            response_sourceconf.frameNStart = frameN  # exact frame index
            response_sourceconf.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response_sourceconf.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if response_sourceconf.status == STARTED and t >= frameRemains:
            response_sourceconf.status = STOPPED
        if response_sourceconf.status == STARTED:
            theseKeys = event.getKeys(keyList=['v', 'b'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response_sourceconf.keys = theseKeys[-1]  # just the last key pressed
                response_sourceconf.rt = response_sourceconf.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sourceconfComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sourceconf"-------
    for thisComponent in sourceconfComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_sourceconf.keys in ['', [], None]:  # No response was made
        response_sourceconf.keys=None
    trials.addData('response_sourceconf.keys',response_sourceconf.keys)
    if response_sourceconf.keys != None:  # we had a response
        trials.addData('response_sourceconf.rt', response_sourceconf.rt)
    
    # ------Prepare to start Routine "fixationISI"-------
    t = 0
    fixationISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.250000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationISIComponents = [fixation_2]
    for thisComponent in fixationISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixationISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_2* updates
        if t >= 0.0 and fixation_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_2.tStart = t
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.setAutoDraw(True)
        frameRemains = 0.0 + .25- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_2.status == STARTED and t >= frameRemains:
            fixation_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixationISI"-------
    for thisComponent in fixationISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "finished"-------
t = 0
finishedClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
finishedComponents = [text]
for thisComponent in finishedComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "finished"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finishedClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finished"-------
for thisComponent in finishedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
