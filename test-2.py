from naoqi import ALProxy
import time
tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
motionProxy = ALProxy("ALMotion", "127.0.0.1", 9559)
#textSpeakProxy = ALProxy("ALTextToSpeech", "zhanat-K56CB", 37826) 
#motionProxy = ALProxy("ALMotion", "zhanat-K56CB", 37826)
tts.say("Hi, Serzhan! I want to come with you!")

#10.1.198.45
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([1.16, 1.96])
keys.append([[0.00687858, [3, -0.4, 0], [3, 0.266667, 0]], [0.00687858, [3, -0.266667, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([1.16, 1.96])
keys.append([[0.0128947, [3, -0.4, 0], [3, 0.266667, 0]], [0.0128947, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([1.16, 1.96])
keys.append([[0.074846, [3, -0.4, 0], [3, 0.266667, 0]], [0.087441, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([1.16, 1.96])
keys.append([[-0.0911858, [3, -0.4, 0], [3, 0.266667, 0]], [-0.111946, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([1.16, 1.96])
keys.append([[-0.563347, [3, -0.4, 0], [3, 0.266667, 0]], [-0.42083, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([1.16, 1.96])
keys.append([[-1.18831, [3, -0.4, 0], [3, 0.266667, 0]], [-1.21014, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LHand")
times.append([1.16, 1.96])
keys.append([[0.3213, [3, -0.4, 0], [3, 0.266667, 0]], [0.290926, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([1.16, 1.96])
keys.append([[0.182409, [3, -0.4, 0], [3, 0.266667, 0]], [0.127409, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([1.16, 1.96])
keys.append([[0.0833382, [3, -0.4, 0], [3, 0.266667, 0]], [0.127509, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([1.16, 1.96])
keys.append([[-0.159645, [3, -0.4, 0], [3, 0.266667, 0]], [-0.169995, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([1.16, 1.96])
keys.append([[-0.0923203, [3, -0.4, 0], [3, 0.266667, 0]], [-0.0923203, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([1.16, 1.96, 6.4])
keys.append([[1.48725, [3, -0.4, 0], [3, 0.266667, 0]], [1.44734, [3, -0.266667, 0.0399129], [3, 1.48, -0.221517]], [-1.3439, [3, -1.48, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([1.16, 1.96])
keys.append([[0.19986, [3, -0.4, 0], [3, 0.266667, 0]], [0.215891, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([1.16, 1.96])
keys.append([[0.106985, [3, -0.4, 0], [3, 0.266667, 0]], [0.106985, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([1.16, 1.96])
keys.append([[0.0773957, [3, -0.4, 0], [3, 0.266667, 0]], [0.087441, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([1.16, 1.96])
keys.append([[0.107639, [3, -0.4, 0], [3, 0.266667, 0]], [0.108344, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([1.16, 1.96])
keys.append([[0.410161, [3, -0.4, 0], [3, 0.266667, 0]], [0.586431, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([1.16, 1.96])
keys.append([[1.19688, [3, -0.4, 0], [3, 0.266667, 0]], [1.309, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RHand")
times.append([1.16, 1.96])
keys.append([[0.304904, [3, -0.4, 0], [3, 0.266667, 0]], [0.302336, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([1.16, 1.96])
keys.append([[0.165433, [3, -0.4, 0], [3, 0.266667, 0]], [0.129933, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([1.16, 1.96])
keys.append([[-0.111041, [3, -0.4, 0], [3, 0.266667, 0]], [-0.119031, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([1.16, 1.96])
keys.append([[-0.159645, [3, -0.4, 0], [3, 0.266667, 0]], [-0.169995, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([1.16, 1.96])
keys.append([[-0.0821816, [3, -0.4, 0], [3, 0.266667, 0]], [-0.0923279, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([1.16, 1.96, 3.12, 4, 5, 5.76])
keys.append([[-1.37183, [3, -0.4, 0], [3, 0.266667, 0]], [-1.37183, [3, -0.266667, 0], [3, 0.386667, 0]], [-0.963422, [3, -0.386667, -0.0759217], [3, 0.293333, 0.0575958]], [-0.905826, [3, -0.293333, 0], [3, 0.333333, 0]], [-1.19381, [3, -0.333333, 0], [3, 0.253333, 0]], [1.53938, [3, -0.253333, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([1.16, 1.96, 3.12, 4, 5])
keys.append([[-0.235619, [3, -0.4, 0], [3, 0.266667, 0]], [-0.905826, [3, -0.266667, 0], [3, 0.386667, 0]], [0.0977384, [3, -0.386667, 0], [3, 0.293333, 0]], [-1.01404, [3, -0.293333, 0], [3, 0.333333, 0]], [0.0558505, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([1.16, 1.96])
keys.append([[-0.944223, [3, -0.4, 0], [3, 0.266667, 0]], [-0.944223, [3, -0.266667, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  motion = ALProxy("ALMotion", "127.0.0.1", 9559)
  #motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err

#//////////////////////////////////////////////////////////////////////////////////

handName = "LShoulderPitch"  # by this name we will control our robot to move forward or backward
wristName = "LWristYaw"  # the name of the wrist by which we will control the robot to move right or left
useSen = 0


while(1):

	x = motionProxy.getAngles(handName, useSen)
	y = motionProxy.getAngles(wristName, useSen)
	z = motionProxy.getAngles(wristName, useSen)
	print(x[0])
	if x[0] > 0:    #if the value is largr than 0, nao will stop, in other word when we drop hand the motion stops
		#motionProxy.move(0.0, 0.0, 0.0)
		if (y[0] > (-0.19) and y[0] < 0.19) or (z[0] > (-0.19) and z[0] < 0.19):
			motionProxy.move(0.0, 0.0, 0.0)
		elif ((y[0] > 0.19) or (y[0] < (-0.19)) or (z[0] > 0.19) or (z[0] < (-0.19))):
			motionProxy.move(0.0, y[0], z[0])
	elif x[0] < 0: #another condition when we take hand to continue motion in forward and backward directions
		if (y[0] > (-0.19) and y[0] < 0.19) or (z[0] > (-0.19) and z[0] < 0.19): # when the wrist in the normal condition, the robot will not turn left or right
			motionProxy.move((-x[0]), 0.0, 0.0) #the robot is moving forward
			if x[0] < (-1.30): # in certain condition (when we pull hand backward) the robot will move backwrds
			#so when the value is less then -75 degree according to LShoulderPich that was observed in choreographer
				if (y[0] > (-0.19) and y[0] < 0.19) or (z[0] > (-0.19) and z[0] < 0.19):
					motionProxy.move((x[0]), 0.0, 0.0)
				elif y[0] > 0.19 or y[0] < (-0.19) or z[0] > 0.19 or z[0] < (-0.19):
					motionProxy.move((x[0]), y[0], z[0])

		elif (y[0] > 0.19 or y[0] < (-0.19)) or (z[0] > 0.19 or z[0] < (-0.19)):
			motionProxy.move((-x[0]), y[0], z[0]) #it moves forwards, because the minus sign converts the digit to positive number
	#motionProxy.move(x[0], 0.0, 0.0)

        
        time.sleep(0.100)


        #motionProxy.move(0.0, 0.0, 0.0)

