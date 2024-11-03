# Focused Hearing Prototype Documentation

# Makers 

> Clearly list and credit all individuals involved in the creation of the prototype.

 - Shi Pui Ng
 - Izak Lindsay
 - Bill McAlister
 - Amanda Topaz

[The Focused Hearing development team. From Left to right, Bill, Amanda, Shi and Izak.](src/fh_team.jpg)

# Objective of prototype 

> Define the purpose and goals of your prototype. Outline what you aim to achieve with its development.

Focused Hearing is an alternative to AI-assisted hearing aids. Speech recognition in a noisy environment can be challenging. Rather than trusting an algorithm to decide what constitutes background noise, the user can focus on the mouth of the speaker they wish to hear, and through cross modal fusion <ref> of a lip reading and speech recognition model, be given the data they need. In our view this leverages our natural habit of looking at the person that we want to hear rather than conceding agency to an AI to decide what is noise.

Objective:
    Enable hearing impaired people to communicate naturally in noisy environments.
    
# List of (desired/fulfilled) functions

> Specify both desired and fulfilled functions of the prototype. Detail how each function is implemented, including sensing, actuation, computation, and machine learning.

## Fulfilled
 - Transcribe English language from audio data of speakers.
 - Compare transcripts originating from different data sources to infer whether the incoming message is background noise or not.
 - Display transcripts to the user in a way that helps them understand their speaking partner.
    
## Partly Fulfilled
 - Transcribe English language from silent video data of speakers.
 - Transcribe speaker's in real time.
 - Make the device wearable on the head so that the direction of gaze naturally controls the information drawn from the environment.

## Desired
 - Use the aligned message to suppress background noise in an audio feed sent to the user's earing aids or noise canceling headphones. 

# Architecture

![The physical and software components comprising Focused Hearing and how information flows between them](src/architecture.png)

## Software Components

Focused Hearing comprises 
Below is a diagram illustrating the relationship between the different software components that comprise Focused Hearing. 
    
### Lip Reading Model

### Speech to Text Model

### Alignment Model

The alignment model is a customised [Needleman-Wunsch algoritm](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm).

### Recording Software

Video is recorded using python's [Open-CV library](https://pypi.org/project/opencv-python/)
Audio Is recorded with the [pyAudio library](https://pypi.org/project/PyAudio/)


### Communication Software

It was also necessary to establish a [Virtual Private Network](https://en.wikipedia.org/wiki/Virtual_private_network) (VPN) amongst the devices as the ANU WiFi network has a restrictive firewall that blocks SMB and socket communication. The [Tailscale](https://tailscale.com) service helps to


### Web Host

The reults of Focused Hearing are displayed back to the user through a custom web host. 

## Physical components

> Offer a breakdown of the physical components used in your prototype, elucidating their roles and interactions.

### Izak's Laptop
### Raspberry Pi
### Camera
### Battery
### Headset
### USB Microphone
### Screen
### Button
### LEDs
### WiFi

# Materials and tools

> Enumerate the materials and tools used in constructing the prototype, providing a comprehensive list for easy reference. 

# Process of making the prototype 

> Provide an overview of the development process, highlighting key milestones, challenges faced, and solutions implemented.

## Training the Lip-Reading Model

## Deploying the Speech to Text Model

## Developing the Alignment Model

## Developing the Recording Software

## Developing the Communication Software

## Developing the Web Host

## Developing a Physical Interface

## Building the Physical Prototype 

# Step-by-step interaction guide 

> Present a step-by-step description guiding users on how to interact with the prototype. This should encompass various modes of engagement and highlight the user experience.

 - Maybe we should make a video of this early next week?
 - Getting some stills to include in the document would be good.

# References

> cite any external sources, references, or inspirations that contributed to the development of your prototype.

# Acknowledgment

> Express gratitude and acknowledgment to individuals, organisations, and/or resources that played a significant role in supporting or influencing the prototype's creation.

 - Mark Pesce gave Amanda the idea
 - Damian inspired our Build Pitch