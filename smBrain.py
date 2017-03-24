import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io

BUF = 0.1
OBS_DIST = 0.5
class MySMClass(sm.SM):
    startState = 0
    def getNextValues(self, state, inp):
        if state == 0 and inp.sonars[2] <0.3:
            nextstate = 0
            output = (io.Action(fvel = -0.5, rvel = 0))
        elif state == 0 and inp.sonars[2]>0.5:
            nextstate = 0
            output = (io.Action(fvel = 0.5, rvel = 0))
        elif state == 0 and inp.sonars[2]>=0.3 and inp.sonars[2]<=0.5:
            nextstate = 1
            output = (io.Action(fvel = 0, rvel = 0.5))
        elif state == 1:
            if inp.sonars[4]>0.5: 
                nextstate = 1
                output = (io.Action(fvel = 0, rvel = 0.5))
            elif inp.sonars[4]<=0.5: 
                nextstate = 2
                output = (io.Action(fvel = 0.5, rvel = 0))
        elif state == 2 and inp.sonars[4]>0.5 or inp.sonars[4]<0.3:
            nextstate = 1
            output = (io.Action(fvel = 0.5, rvel = 0))
        return (nextstate, output)

mySM = MySMClass()
mySM.name = 'brainSM'

######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar'+str(sonarNum),
                                        lambda: 
                                        io.SensorInput().sonars[sonarNum]))

# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=True, # slime trails
                                  sonarMonitor=False) # sonar monitor widget
    
    # set robot's behavior
    robot.behavior = mySM

# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks = robot.gfx.tasks())

# this function is called 10 times per second
def step():
    inp = io.SensorInput()
    # print inp.sonars[3]
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())

# called when the stop button is pushed
def brainStop():
    pass

# called when brain or world is reloaded (before setup)
def shutdown():
    pass
