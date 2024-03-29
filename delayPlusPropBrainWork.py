import math
import libdw.sm as sm
from soar.io import io
import libdw.gfx as gfx
import libdw.util as util
import libdw.eBotsonarDist as sonarDist
from time import sleep

######################################################################
#
#            Brain SM
#
######################################################################

desiredRight = 0.4
forwardVelocity = 0.2

rSensed = []
Dist = []

# No additional delay
class Sensor(sm.SM):
    def getNextValues(self, state, inp):
        v = sonarDist.getDistanceRight(inp.sonars)
        print 'Dist from robot center to wall on right', v
        sleep(0.05)
        return (state,v)

# inp is the distance to the right
class WallFollower(sm.SM):
    startState = None
    def getNextValues(self, state, inp):
        rSensed.append(inp)
        k1 = 100
        k2 = -97.36
        Dist.append(k1*(desiredRight-rSensed[len(rSensed)-1])+k2*(desiredRight-rSensed[len(rSensed)-2]))
        return (state, io.Action(fvel = forwardVelocity, rvel=Dist[len(Dist)-1]))    
        

# Your code here
        pass

sensorMachine = Sensor()
sensorMachine.name = 'sensor'
mySM = sm.Cascade(sensorMachine, WallFollower())

######################################################################
#
#            Running the robot
#
######################################################################

def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)
    robot.gfx.addStaticPlotSMProbe(y=('rightDistance', 'sensor',
                                      'output', lambda x:x))
    robot.behavior = mySM
    robot.behavior.start(traceTasks = robot.gfx.tasks())

def step():
    robot.behavior.step(io.SensorInput()).execute()
    io.done(robot.behavior.isDone())

def brainStop():
    pass
