# hri_assignment2
The project was aimed to learn to control the NAO robot using choreography. (Choreographe is a desktop
application, which allows to create behaviors and test them on a simulated NAO robot)
The goal was to implement the "Follow me" application on NAO robot using Python NaoQi.
To understand better you can see this [video](https://www.youtube.com/watch?v=K-fXHvKL86w)

## Installation
The first thing that should be installed is choreograph for this project
There is a link [to download choreograph](https://developer.softbankrobotics.com/nao6/downloads/nao6-downloads-linux)
There you can use prefferable OS.
Choose the right one for you and please read installation guide in the website.
My Ubuntu is 16.04 and I have chosen Choregraphe Setup version 2.8.6, Linux 64.


## Implementation
Choreographe uses NaoQi, which is a software library for programming NAO. Choreographe, NaoQi documentation and API are very useful when programming the robot and can be accessed at: [http://doc.aldebaran.com/2-1/index_dev_guide.html](http://doc.aldebaran.com/2-1/index_dev_guide.html)
Go through this guide to intall and start to implement.
Open the terminal and write there your path to Python NaoQi. My path was like this:

1) export PYTHONPATH=${PYTHONPATH}:~/Downloads/pynaoqi-python2.7/lib/python2.7/site-packages
2) export QI_SDK_PREFIX=~/Downloads/pynaoqi-python2.7

Then the follow command was written to activate python naoqi:
3) python
4) import naoqi
After that:
exit()
And now the scripts can be used for implementation.


## Technologies

- Python 2.7.12
- Choreography
