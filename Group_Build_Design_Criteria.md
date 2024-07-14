---
Title: Group Build Design Criteria
---

# Introduction
This document is intended to be a record of the ideas that we have discussed for our group build project.
The Proposals section contains specific ideas for what could be built. The Constraints section details the design constraints for our project: both those stipulated b the course and those set internally by team members. The Ideals section is a collection of value statements: messages or themes that we would like to address with our maker project. The constraints are mandatory and we expect our final project to meet all of them. The ideals are optional and we would like our maker project to express some of them. In the interest of a comprehensible message for our demo day presentation, we expect that we will need to choose a small set of ideals to focus on.

# Constraints
<!--
I can't find the official marking criteria anywhere! It'd be good to write up the course constraints directly from the official marking criteria. For now I've just written what I could remember.  
-->
 - (course) Must present a convincing prototype on Demo Day
 - (course) Project must be delivered within a $500 budget
 - (course) Must include a physical component
 - (course) The physical component must be built by us
 - (course) Must include a machine-learning component
 - (course) Must include cyber component
 - (Bill) Must not be labour-saving device

# Ideals
 - (Bill) Eudaimonic AI that pushes humans to be better rather than allowing us to cut corners
 - (Bill) A message about the unpredictability of emergent phenomena
 - (Bill) Gives insight into the emergence of consciousness
 - (Bill) Computer vision
 - (Bill) Biomimetics
 - (Bill) A really fun and interactive presentation for demo day
 - (Bill) Something for demo day that makes people move around
 - (Bill) A radiative evolutionary project rather than a linear waterfall style project
 - (Bill) Critical making: the invention, and the making of it, helps us to reflect on current technological paradigms and our own worldviews
 - (Bill) Not aimed at commercialisation
 
# Proposals

## Personal Language Model 🦭🈶
Learns to understand your handwriting and the idiosyncrasies of your writing. Can generate messages as though they were written by you like in the movie *Her* (it's not a super original idea). Also tells you what you need to do to improve your handwriting and cut back the idiosyncrasies in your writing. It would allow you to practice handwriting a lot more oftem as it would be quite effective at digitizing your writing so you would be able to draft all your work in hand writing before digitizing to edit.

### Demo day
I think that the personal language model would be a bit lame on demo day because people would have to spend a it of time handwriting something like *the quick brown fox...* so that the model had enough of your data to start working.

## Sign Language Computer Interface 🫰🖥
[Plenty of work has been done](https://link.springer.com/article/10.1007/s11831-019-09384-2) on using AI to translate sign language. This would be using sign language as an interface to a computer so that you can interact with the computer by moving your body instead of sitting still. This is, however, still a symbolic interface to your computer. 

![Kinect data viz. example](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXB0NjNscnd3NHJlOHZ1bGhoOHN5bndjaGRhcDYwZ205Y3VzYWp1OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jh9FGY437Fd04/giphy.webp)

I think the [X-Box Kinect](https://en.wikipedia.org/wiki/Kinect) might have already had this kind of interface to some of its software. I did a bit of research and found that it is called a Natural Interface and there is an open-source SDK called [OpenNI](https://wiki.ros.org/openni). We could buy an old X-Box Kinect off ebay for less than $30 and make a novel Natural Interface.

## Hippocampus filing system 🌊🏇🗃
The way we store documents on our computers is a skewmorph of the way it was done when people used to write stuff down on dead trees 📃. I waste a lot of time trying to find documents in my own computer's filing system and when I have shared folders with other people it gets really confusing. On the other hand, I can remember where places are very well. I've been able to look at maps of cities that I visited, for a few days 5 years ago, and still remember all the places I went and the streets that I walked. If you were able to store your digital files in your physical environment as an augmented reality overlay, it'd be a lot easier to find stuff especially if there'd been a long time since you last retrieved it. There is evidence that spatial cognition and memory occurs in the [hippocampus](https://en.wikipedia.org/wiki/Hippocampus#Function) and is quite different from other abstract forms of thought.

This idea isn't super original because there are various tools that allow you to organise geotagged photos this way. Extending it to other types of media and making the location arbitrary wrt composition is nove but might also greatly reduce the utility.

### Components
- (physical) The only physical component is the geography of planet earth.
- (ML) I don't know what ML it would use.

### Demo day
You could get people to play with a world map and a complex file structure to see the contrast but you wouldn't be able to give people a direct experience.

## Ento-meteorology 🐜🌦
Using cameras to collect time-lapse images of ant colonies. Machine learning would look for patterns in the behaviour of the ants or the structure of their colonies. It would relate this to time-series weather data. The idea is that the model would learn to forecast the weather based on the behaviour of ants. I've heard that ants prepare their nests for heavy rain by building levees around the openings. 

## Waving Tube Man 🕺🐙

The idea is to make a waving-tube-man, wire him up to a neural network and get him to learn to move his body in an intentional way. It would probably be too hard, but the ideal would be to make him throw and catch frisbees. Getting him to block frisbees and change the periodicity of his waving to match the tempo of ambient music might be achievable. 

![Waving Tube Man](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExenBwbWhvN2F3ajVib2RhYjg4MTI1cDk5Njc1bzNvdHZtdTlramU1ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriOfe0A84SVqwr6w/giphy.webp)

The project would allow us to muck around with lots of different structures of neural nets as we would spend most of our time experimenting with different designs of neural nets and trying to use them to get the tube man to "understand" his own body and move in an intentional way. There might be some complicated physial making to build a tube man design that can move in either a random or an intentional way.

The cool part would be training him to move in an intentional way. Once we had something that moved in a non-deterministic way and a camera trained on it, we'd need to get the actuators to be able to assert imperfect control over the motion of the body. From there, we would add neural nets and let them work for hours watching what happens as they fiddle with different sequences of signals sent to the actuators. Hopefully, the neural net would be able to identify some patterns. For example; if you tighten the left side cord and turn off the blower, the tube man flops down to the left. If you then turn the blower on full power, he leaps up making a 90 degree arc.

We'd use computer vision to map the trajectory of incoming projectiles and the neaural net would be set the goal of maximising the chance of an intercept. To make it more simple, the tube man might just be able to watch the incoming projectile and gradually adjust left/right to align his head with it and execute a block.

### Components
- (sensor) Computer vision; maybe with depth perception to make him better at blocking projectiles
- (sensor) optionally, some proprioception to see if that makes him move better
- (sensor) optionally, a microphone to listen for music to dance to
- (actuator) blowers, fans, pumps, valves, etc. to animate his body
- (actuator) optionally, little cords that can be wound / unwound by motors
- (physical) a non-rigid body that moves in a non-deterministic way
- (machine learning) A neural network that translates patterns of sensor data into patterns of actuation that achieve goals

### Ideals

I got the idea from a [lecture by Manuel DeLanda](https://www.youtube.com/watch?v=ZC57sUilp44) where he joked that you could link a neaural network up to some sensors and train it to catch a frisbee. He went on to talk about how, in his philosophy, matter is fundamentally creative and that higher levels of emergent phenomena (biology, consciousness) work by directing natural emergence from the chaos of lower levels. A tube man's movement is typically chaotic. My idea is that, using the neural net, he will learn to direct the chaos so that his movement is a blend of intentionality and randomness. I reckon it'll freak people out if we can teach him to (sometimes) catch frisbees 😂 They'll initially percieve it as a bizzare coincidence but then they'll see him do it multiple times. 

These are some of the attractions of the project:
- Lots of machine learning using small, custom neural nets
- Biomimetics, as we'd be trying to replicate the way that simple organisms make intentional movements
- Embodied intelligence as the neural net would have to learn to understand and manipulate chaotic patterns to make intentional movements 
- Chaos theory / far from equilibrium thermodynamics
- Non-linear materialism
- Makes for a fun and interactive demo day presentation
- Uses computer vision
- [Soft-bodied robotics](https://en.wikipedia.org/wiki/Soft_robotics) for vulnerable people
- Is a cybernetic satire of conventional robotics

### MVP
For the MVP we could just make a bot that moves up and down a rail and can block a tennis ball that is rolled towards it. It would use a camera as a sensor and the machine learning would kinda be redundant because the problem would be quite deterministic 🤷

For the MVP +1  we could build a non-rigid arm that is swung around by a servo motor and tries to block incoming projectiles. The arm could be made in miniature from readily available motors and a couple of 3D printed segments. The idea being that the intentional movement is mediated by some non-deterministic part which the neural net has to learn to control.

### Demo Day
It would be a really fun presentation on demo day because people would be able to interact with the tube man by throwing different projectiles for him to block/catch. They could also change the song that he is dancing to. You could also potentially demo different versions of the neural net that demonstrate what tube man was like while he was still learning to control his body. 

There would be plenty to talk about as per the ideals section.


