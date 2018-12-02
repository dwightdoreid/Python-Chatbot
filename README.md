# Basic Overview

System uses a basic chatbot whose commands and actions are implemented in apps.

## 1\. Chatbot Directory Structure

The Chatbot has the following directory structure

*   Chatbot
    *   main.py
    *   Chatbot.py
    *   Apps Folders

### Main (main.py)

This file provides the interface to the chatbot. In this case interface is via an API on port 9090.

It imports the Chatbot as a class that is implemented in another file (Chatbot.py).

### Chatbot.py

This file implements the Chatbot as a class to be imported into main.

The Chatbot class will initialise by detecting all folders in its current directory and determine if they are apps by their folder structure.

It will them build a master list of all commands, their variations and their respective actions.

A consequence of this is that every command and it's variations have to be uniques across all apps.

## 2\. Apps Directory Structure

Apps are implemnted as folders in the chatbot directory and have the following folder structure

*   AppName
    *   __init__.py
    *   commands.xml
    *   actions.py

### The __init__.py

The is for python stuff :)

### The commands.xml

This file contains the commands that the chatbot can respond to and their variations.

Each command has several variations and one action.

An example of the commands.xml file is shown below:

<pre>
&lt?xml version="1.0" encoding="UTF-8"?&gt
&ltcommands&gt
&ltcommand&gt
    &ltvar&gtWhat is the temperature in here?&lt/var&gt
    &ltvar&gtwhat is the temperature&lt/var&gt
    &ltvar&gttemperature&lt/var&gt
    &ltactn&gtmqtt.actions.subscribe&lt/actn&gt
&lt/command&gt  
&ltcommand&gt
    &ltvar&gtwhat is your name?&lt/var&gt
    &ltvar&gtname&lt/var&gt 
    &ltactn&gt2&lt/actn&gt
&lt/command&gt
&lt/commands&gt
</pre>


### The actions.py file

This file contains the methods for the actions that the Chatbot will carry out implemented as python functions.
