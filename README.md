
# IT Project 2
![alt text](https://github.com/bunCha-cob/ITP2-group-5/blob/master/Images/Logo.png)

# Satisfactory Assessment of Customers by Tracking People in Marketplaces
Created and designed by Group 5
## Introduction
This project aims to automatically analyse the walking patterns of the customers in the marketplaces and shopping areas. The customers are monitored with cameras and the footages of these cameras will be analysed to highlight the different rates of satisfaction to enhance the services provided to them. 
We aim to develop a tool that can automatically analyse the walking patterns of customers in shopping areas and analyse the different rates of satisfaction in order to enhance service to them. This tool will be tested, and results should be documented accordingly.
### Background

According to the initial project description the project aims to “automatically analyse the walking patterns of the customers in the marketplaces and shopping areas. The customers are monitored with cameras and the footages of these cameras will be analysed to highlight the different rates of satisfaction to enhance the services provided to them” (https://moodle.telt.unsw.edu.au/).

The project will be used as a source of further research into how to rate satisfaction of customers in marketplaces. There is currently publicly available research concerning the detection and tracking of people and objects given footage (see the Research Log for more information). There is also research concerning possible key satisfaction indicators of customers based on their engagement in terms of distance and time with objects in stores (see the Research Log for more information). This research will provide the basis for the background of our project and be utilized to develop our own application to track and rate customers satisfaction. The application developed in this project will be used ultimately in order to enhance the service to customers in order to increase their rate of satisfaction when shopping. This will help to provide further insight into research in this area and provide a tool to test and gather data relating to this field of work and the satisfaction indicators chosen for this project. The project will provide future capabilities to analyse walking patterns in relation to customer satisfaction and provide a tool that can gather data that marks satisfaction based on engagement-based indicators.

Machine learning tactics will used in this project in order to get results that are relatively accurate and precise. Current research and applications can be found to use machine learning in order to detect and track people and objects (see the Research Log and 8. Intellectual Property of this contract for more information). These pre-trained machine learning applications can be utilized in this project in order to form the basis of tracking people’s trajectories and engagement with objects. Research of machine learning algorithms can facilitate enhancing these applications in order to gain better accuracy and precision. This provides the background for our critical systems in the project and the basis of how we will be able to detect the people and objects in the shop
### Architecture
This tool utilizes several other free online tools that use machine learning to track humans and objects. 
The project will utilize publicly available software produced and delivered on the GitHub repository yolov3_deepsort developed by theAIGuysCode. This repository can be found under the following link: https://github.com/theAIGuysCode/yolov3_deepsort?fbclid=IwAR1pTROfr90DNreMSxcPZ42AkAEDUQoGRaYXylFuZwB5JQWJv8857co8Fmk

This Object Tracking using YOLOv3, Deep Sort and Tesorflow will be utilized to track objects and people in marketplaces. The data produced and tracking will enable our application to automatically recognise these objects and people, allowing tracking of trajectories and use this information to track engagement time in order to rate satisfaction. Other associated links for object tracking and detection may also be used in this process: https://github.com/theAIGuysCode/yolov3_deepsort https://github.com/Qidian213/deep_sort_yolov3 https://github.com/LeonLok/Deep-SORT-YOLOv4 https://github.com/adipandas/multi-object-tracker

This project will also utilize SQL databases to track and transform the data, this will be either through SQLite (https://sqlite.org/index.html) or through the mariaDB SQL database platform (https://mariadb.com/). The database will be used to record and keep the data to be used in the satisfaction rating.

Python will be used to code the application. Visual Studio Code will be utilized by each team member as an IDE to develop python code on (https://code.visualstudio.com/). GitHub will also be used to store our code on in accordance with their terms and conditions (https://github.com/). Virtual Machine Ware workstation environment (https://download.cnet.com/VMware-Workstation-Player/3000-2094_4-10470784.html) will be used to create a Ubuntu 18.04.4 Linux environment (http://releases.ubuntu.com/18.04/) if at any point software features are not working with any team members usual environments. Other applications will be used to store our drafting, design and systems diagrams, such as on Microsoft Teams and its accompany extensions in accordance with its terms and conditions (https://teams.microsoft.com/go#).

Use of known mathematical algorithms and equations to transform data may be used against satisfaction ratings to get accurate weighted ratings. Researched machine learning algorithms may be used to speed up object and person tracking to increase accuracy and efficiency. These algorithms may be confirmed later during testing and later development of the code. See the Research Log for information concerning ideas and research that may be used or used to inform the project.

## Quick Start


