#test_intro.py
from naoqi import ALProxy
import time
tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
motionProxy = ALProxy("ALMotion", "127.0.0.1", 9559)

handName = "LShoulderPitch"  # by this name we will control our robot to move forward or backward
#wristName = "LWristYaw"  # the name of the wrist by which we will control the robot to move right or left
useSen = 0

# this was a demonstration of the speed that was implemented if the certain angle would apply

while(1):
	
	x = motionProxy.getAngles(handName, useSen)
	print(x[0])
	if x[0] > 0:
		motionProxy.move(0.0, 0.0, 0.0)
	elif x[0] < 0:
		if x[0] > (-1.30) and x[0] < (-0.7):
			motionProxy.move(1.0, 0.0, 0.0)
		elif x[0] < (0) and x[0] > (-0.7):
			motionProxy.move(0.005, 0.0, 0.0)
		elif x[0] > (-1.30):
			motionProxy.move(0.3, 0.0, 0.0)

	

        
        time.sleep(0.100)