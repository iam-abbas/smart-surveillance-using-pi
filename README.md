
<p align="center">
<img style="padding:10px;" src="https://img.shields.io/github/stars/iam-abbas/smart-surveillance-using-pi?style=flat-square">
<img style="padding:10px;" src="https://img.shields.io/github/license/iam-abbas/smart-surveillance-using-pi?style=flat-square">
</p>

### Awards Collected
- 🥇Gold Medal - SRM AP Research Conference 2020

# Implementation of person detection using SSD-MobileNet on Microcomputer platform


### Abstract

With the growing rate of theft and robberies, surveillance cameras have become a piece of common household equipment for many. Although cameras only record the footage and make it possible to review the footage after a sense of malicious activity being spotted by someone. There have been ways to automate this process by installing a motion detection system and other IoT based sensors. However, there has been no reliable and affordable solutions to alert the property owner during the mishappening. 

We came up with this compact and complete solution to this problem all packed in single Raspberry Pi. We used pre-trained weights of Single Shot Multibox Detector with MobileNet to detect only human presence. We used advanced Image Enhancement technology to make the best use of model even under very low light conditions. The moment the model detects a human we built a trigger system that sends the user a Telegram Message with a captured image and sets up a Flask Server with Live video feed and Data Analytics.


### The Model

The Model used is pre-trained weights of Single Shot Multibox Detector with MobileNet dataset. It can be used to detect various objects but we limited it to humans. However, the algorithm cannot detect objects under low light conditions because there is not enough exposure to identify the shape of the contents. We used methods like automatic gamma adjustments and light intensity correction to tackle this problem and results turned out to be amazing. Here is an example of the model detecting a person under very low light.

![InsPi](https://raw.githubusercontent.com/iam-abbas/smart-surveillance-using-pi/master/webimg/3.jpg?token=AKAOFGNNVDHIWS2IUPM2E625VVOV6)


### Raspberry Pi

We used Raspberry Pi as our main platform for this project due to the following reasons.

- Very Compact
- Low Cost
- Efficient
- Can connect to devices wirelessly

### Alert System

We implemented the alert system using Telegram API to send data to user's telegram number directly. We are also implementing a phone call system using Twilio API to send an intimation to the police and neighbors during mishappening.


### Web Server

A Flask server has been set up with shows live feed and Recent Captures. For now, that's all it does.


## Usage Guide

### Software Requirements

- [Python 3.4 or higher](https://www.python.org/downloads/)
- [Telegram Bot Token](https://core.telegram.org/bots)
- [OpenCV for Python (opencv-python)](https://pypi.org/project/opencv-python/)
- [Flask](https://pypi.org/project/Flask/)
- [Numpy](https://pypi.org/project/numpy/)
- [Telepot](https://pypi.org/project/telepot/)

### Hardware Requirements

- [Raspberry Pi](https://www.raspberrypi.org/products/)
- Webcam/Any Camera
- Keyboard
- Mouse
- Monitor

### How to run?

Just clone this repository and run ```main.py```


## Future Updates

- A cleaner script
- Automatic trigger system using ARN
- Better Implementation of Telegram Bot
- Implementation of Twilio API for phone calls
- More features on web portal.
- Cloud based implementation of model to reduce load on Pi



