#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.01),
    on Thu Jun  1 11:11:36 2017
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
expName = 'encoding'  # from the Builder filename that created this script
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
    originPath=u'/Volumes/External/MemoHR/Scripts/share/task/encoding_practice.psyexp',
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
    text='Decide how likely the photo could have been:\n- taken within San Francisco OR\n- taken by a professional photographer\n\nThe question will change every 4 images.\n\nEXPERIMENTER: press space bar',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "beginScan"
beginScanClock = core.Clock()
prescanFixation = visual.TextStim(win=win, name='prescanFixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "preblock"
preblockClock = core.Clock()
blockInstrux = visual.TextStim(win=win, name='blockInstrux',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
ISI_2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')
image = visual.ImageStim(
    win=win, name='image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1200, 900],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
scale = visual.TextStim(win=win, name='scale',
    text='least -- 1 -- 2 -- 3 -- 4 -- most',
    font='Arial',
    pos=[0, -.9], height=0.08, wrapWidth=1600, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
fixISI_1 = visual.TextStim(win=win, name='fixISI_1',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
scaleLabel = visual.TextStim(win=win, name='scaleLabel',
    text='default text',
    font='Arial',
    pos=[0, -.8], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
fixISI_after = visual.TextStim(win=win, name='fixISI_after',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);

# Initialize components for Routine "jitterISI"
jitterISIClock = core.Clock()
fixJitter = visual.TextStim(win=win, name='fixJitter',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "postblock"
postblockClock = core.Clock()
postFixation = visual.TextStim(win=win, name='postFixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "endScan"
endScanClock = core.Clock()
postscanFixation = visual.TextStim(win=win, name='postscanFixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "finished"
finishedClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You are now finished with the task.\n',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('lists/s'+expInfo['participant']+'/'+expInfo['condition']+'_encoding_runlists.csv'),
    seed=None, name='runs')
thisExp.addLoop(runs)  # add the loop to the experiment
thisRun = runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun.keys():
        exec(paramName + '= thisRun.' + paramName)

for thisRun in runs:
    currentLoop = runs
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun.keys():
            exec(paramName + '= thisRun.' + paramName)
    
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
            win.callOnFlip(instruxResp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if instruxResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                instruxResp.keys = theseKeys[-1]  # just the last key pressed
                instruxResp.rt = instruxResp.clock.getTime()
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
    # check responses
    if instruxResp.keys in ['', [], None]:  # No response was made
        instruxResp.keys=None
    runs.addData('instruxResp.keys',instruxResp.keys)
    if instruxResp.keys != None:  # we had a response
        runs.addData('instruxResp.rt', instruxResp.rt)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "beginScan"-------
    t = 0
    beginScanClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    beginScanComponents = [prescanFixation]
    for thisComponent in beginScanComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "beginScan"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = beginScanClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prescanFixation* updates
        if t >= 0.0 and prescanFixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            prescanFixation.tStart = t
            prescanFixation.frameNStart = frameN  # exact frame index
            prescanFixation.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if prescanFixation.status == STARTED and t >= frameRemains:
            prescanFixation.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in beginScanComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "beginScan"-------
    for thisComponent in beginScanComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(x),
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
        
        # ------Prepare to start Routine "preblock"-------
        t = 0
        preblockClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        blockInstrux.setText(ConLabel)
        
        # keep track of which components have finished
        preblockComponents = [blockInstrux]
        for thisComponent in preblockComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "preblock"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = preblockClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blockInstrux* updates
            if t >= 0.0 and blockInstrux.status == NOT_STARTED:
                # keep track of start time/frame for later
                blockInstrux.tStart = t
                blockInstrux.frameNStart = frameN  # exact frame index
                blockInstrux.setAutoDraw(True)
            frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if blockInstrux.status == STARTED and t >= frameRemains:
                blockInstrux.setAutoDraw(False)
            if trials.thisTrialN not in [0,2]:
                continueRoutine=False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in preblockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "preblock"-------
        for thisComponent in preblockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # ------Prepare to start Routine "trial_2"-------
        t = 0
        trial_2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        response = event.BuilderKeyResponse()
        scaleLabel.setText(ConLabel)
        # keep track of which components have finished
        trial_2Components = [ISI_2, image, scale, response, fixISI_1, scaleLabel, fixISI_after]
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial_2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if t >= 0.5 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            frameRemains = 0.5 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image.status == STARTED and t >= frameRemains:
                image.setAutoDraw(False)
            
            # *scale* updates
            if t >= 0.5 and scale.status == NOT_STARTED:
                # keep track of start time/frame for later
                scale.tStart = t
                scale.frameNStart = frameN  # exact frame index
                scale.setAutoDraw(True)
            frameRemains = 0.5 + 3.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if scale.status == STARTED and t >= frameRemains:
                scale.setAutoDraw(False)
            
            # *response* updates
            if t >= 0.5 and response.status == NOT_STARTED:
                # keep track of start time/frame for later
                response.tStart = t
                response.frameNStart = frameN  # exact frame index
                response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.5 + 3.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if response.status == STARTED and t >= frameRemains:
                response.status = STOPPED
            if response.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    response.keys = theseKeys[-1]  # just the last key pressed
                    response.rt = response.clock.getTime()
            
            # *fixISI_1* updates
            if t >= 0.0 and fixISI_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixISI_1.tStart = t
                fixISI_1.frameNStart = frameN  # exact frame index
                fixISI_1.setAutoDraw(True)
            frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixISI_1.status == STARTED and t >= frameRemains:
                fixISI_1.setAutoDraw(False)
            
            # *scaleLabel* updates
            if t >= .5 and scaleLabel.status == NOT_STARTED:
                # keep track of start time/frame for later
                scaleLabel.tStart = t
                scaleLabel.frameNStart = frameN  # exact frame index
                scaleLabel.setAutoDraw(True)
            frameRemains = .5 + 3.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if scaleLabel.status == STARTED and t >= frameRemains:
                scaleLabel.setAutoDraw(False)
            
            # *fixISI_after* updates
            if t >= 3.0 and fixISI_after.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixISI_after.tStart = t
                fixISI_after.frameNStart = frameN  # exact frame index
                fixISI_after.setAutoDraw(True)
            frameRemains = 3.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixISI_after.status == STARTED and t >= frameRemains:
                fixISI_after.setAutoDraw(False)
            # *ISI_2* period
            if t >= 0 and ISI_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_2.tStart = t
                ISI_2.frameNStart = frameN  # exact frame index
                ISI_2.start(.5)
            elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
                # updating other components during *ISI_2*
                image.setImage(ImageFile)
                # component updates done
                ISI_2.complete()  # finish the static period
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
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
        
        # -------Ending Routine "trial_2"-------
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys=None
        trials.addData('response.keys',response.keys)
        if response.keys != None:  # we had a response
            trials.addData('response.rt', response.rt)
        
        # ------Prepare to start Routine "jitterISI"-------
        t = 0
        jitterISIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        jitterISIComponents = [fixJitter]
        for thisComponent in jitterISIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "jitterISI"-------
        while continueRoutine:
            # get current time
            t = jitterISIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixJitter* updates
            if t >= 0.0 and fixJitter.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixJitter.tStart = t
                fixJitter.frameNStart = frameN  # exact frame index
                fixJitter.setAutoDraw(True)
            frameRemains = 0.0 + FixISI- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixJitter.status == STARTED and t >= frameRemains:
                fixJitter.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in jitterISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "jitterISI"-------
        for thisComponent in jitterISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "jitterISI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "postblock"-------
        t = 0
        postblockClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        
        # keep track of which components have finished
        postblockComponents = [postFixation]
        for thisComponent in postblockComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "postblock"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = postblockClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *postFixation* updates
            if t >= 0.0 and postFixation.status == NOT_STARTED:
                # keep track of start time/frame for later
                postFixation.tStart = t
                postFixation.frameNStart = frameN  # exact frame index
                postFixation.setAutoDraw(True)
            frameRemains = 0.0 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if postFixation.status == STARTED and t >= frameRemains:
                postFixation.setAutoDraw(False)
            if trials.thisTrialN not in [1,3]:
                continueRoutine=False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in postblockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "postblock"-------
        for thisComponent in postblockComponents:
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
    
    # ------Prepare to start Routine "endScan"-------
    t = 0
    endScanClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    endScanComponents = [postscanFixation]
    for thisComponent in endScanComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "endScan"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = endScanClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *postscanFixation* updates
        if t >= 0.0 and postscanFixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            postscanFixation.tStart = t
            postscanFixation.frameNStart = frameN  # exact frame index
            postscanFixation.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if postscanFixation.status == STARTED and t >= frameRemains:
            postscanFixation.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endScanComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "endScan"-------
    for thisComponent in endScanComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'runs'

# get names of stimulus parameters
if runs.trialList in ([], [None], None):
    params = []
else:
    params = runs.trialList[0].keys()
# save data for this loop
runs.saveAsText(filename + 'runs.csv', delim=',',
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
