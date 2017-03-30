import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    startState=0
    def getNextValues(self, state, inp):
        if state == 0:
            if inp.sonars[2] > 0.5:
                nextState = 0
                outp = io.Action(fvel = 0.1, rvel = 0.00)
            elif inp.sonars[2] <= 0.5:
                nextState = 1
                outp = io.Action(fvel = 0.05, rvel = 0.0)
                
        elif state == 1:
            if inp.sonars[2] >0.5 and inp.sonars[3] >0.5 and inp.sonars[4] >0.3:
                nextState = 2
                outp = io.Action(fvel = 0.1, rvel = -0.1)
            elif inp.sonars[2] >0.5 and inp.sonars[3] > 0.3:
                nextState = 1
                outp = io.Action(fvel = 0.1, rvel = 0.0)
            elif inp.sonars[2] > 0.3:
                nextState = 1
                outp = io.Action(fvel = 0.00, rvel = 0.1)

                
        elif state == 2:
            if inp.sonars[2] >0.5 and inp.sonars[3] > 0.3:
                nextState = 2 
                outp = io.Action(fvel = 0.05, rvel = -0.1)
            else:
                nextState = 1
                outp = io.Action(fvel = 0.1, rvel = 0.0)

        print inp.sonars[2]
        print inp.odometry.theta
        return (nextState, outp)

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
                                  sonarMonitor=True) # sonar monitor widget
    
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
