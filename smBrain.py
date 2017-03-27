import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
import math as m
from soar.io import io

class MySMClass(sm.SM):
    startState = 0
    def getNextValues(self, state, inp):
        p = 0
        if state == 0:
            print state
            print p
            if p == 0:
                if inp.sonars[2]< 0.3:
                    nextstate = 0
                    output = (io.Action(fvel = -0.5, rvel = 0))
                elif inp.sonars[2]>=0.5:
                    nextstate = 0
                    output = (io.Action(fvel = 0.5, rvel = 0))
                elif inp.sonars[2]>=0.3 and inp.sonars[2]<0.5:
                    nextstate = 1
                    output = (io.Action(fvel = 0, rvel = 0.2))
            elif p == 1: 
                if inp.sonars[2]>=0.3 and inp.sonars[2]<0.5:
                    nextstate = 1
                    output = (io.Action(fvel = 0, rvel = 0.2))
                if inp.sonars[4]>0.5 and inp.sonars[3]>0.75:
                    nextstate = 2
                    output = (io.Action(fvel = 0, rvel = -0.2))
        elif state == 1: 
            v = inp.sonars[3]
            c = m.sqrt(2)*inp.sonars[4]
            print v
            print c
            if v >= c-0.005 and v < c+0.005:
                p = 1
                nextstate = 0
                output = (io.Action(fvel = 0.5, rvel = 0))
            else: 
                nextstate = 1
                output = (io.Action(fvel = 0, rvel = 0.2))
        elif state == 2: 
            print state
            if inp.sonars[2]>1 and inp.sonars[3]<0.75:
                nextstate = 1
                output = (io.Action(fvel = 0.5, rvel = 0))
            else: 
                nextstate = 2
                output = (io.Action(fvel = 0, rvel = -0.2))
                
        return(nextstate, output)
            

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
