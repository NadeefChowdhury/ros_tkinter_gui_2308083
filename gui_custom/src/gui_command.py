#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from tkinter import *
import time
global currentTime
global prevTime
global meula_num
global message_txt
global direction

prevTime = None
meula_num = 10
message_txt = "Message"

pub = rospy.Publisher("/nadeef_command", String, queue_size=10) 
def stop(e):
    global message
    global currentTime
    global meula_num
    global meula2
    global prevTime
    global direction
    if(prevTime != 0):
        currentTime = time.time()
        difference = int(currentTime-prevTime) * direction
        meula_num = meula_num - difference
        meula2.config(text=meula_num)
        message.config(text="BOT STOPPED")
        
        pub.publish("stop")
        prevTime = None
    else:
        meula2.config(text="0")
def forward(e):
    global message
    global prevTime
    global direction
    global meula_num
    if meula_num > 0:
        direction = 1
        if(not prevTime):
            prevTime = time.time()

        message.config(text="BOT IS GOING FORWARD")
        pub.publish("forward")
        rospy.loginfo("FORWARD")
    else:
        prevTime = 0
        message.config(text="PLEASE INCREASE MEULA")
def left(e):
    global message
    global prevTime
    global direction
    global meula_num
    if meula_num > 0:
        direction = 2
        if(not prevTime):
            prevTime = time.time()
        message.config(text="BOT IS TURNING LEFT")
        pub.publish("left")
        rospy.loginfo("LEFT")
    else:
        prevTime = 0
        message.config(text="PLEASE INCREASE MEULA")
def right(e):
    global message
    global prevTime
    global direction
    global meula_num
    if meula_num > 0:
        direction = 2
        if(not prevTime):
            prevTime = time.time()
        message.config(text="BOT IS TURNING RIGHT")
        pub.publish("right")
        rospy.loginfo("RIGHT")
    else:
        prevTime = 0
        message.config(text="PLEASE INCREASE MEULA")
def back(e):
    global message
    global prevTime
    global direction
    global meula_num
    if meula_num > 0:
        direction = 1
        if(not prevTime):
            prevTime = time.time()
        message.config(text="BOT IS GOING BACKWARD")
        pub.publish("backward")
        rospy.loginfo("BACKWARD")
    else:
        prevTime = 0
        message.config(text="PLEASE INCREASE MEULA")
def increase():
    global meula2
    global meula_num
    meula_num = 10
    meula2.config(text=meula_num)
    pub.publish("meula")
def command():
    rospy.init_node("command_node", anonymous=True)
    rate = rospy.Rate(10)
    global meula_num
    global message_txt
    root = Tk()
    root.title("GUI for Turtlebot")
    root.geometry("800x600")
    frame1 = Frame(root)
    frame1.grid(row=0, column=0,)
    warning = Label(frame1, text="PRESS AND HOLD THE BUTTONS TO MOVE THE BOT")
    warning.grid(row=0, column=1, padx=5, pady=5)
    button = Button(frame1, text='Forward')
    button.grid(row=1, column=1, pady=10)
    button.bind('<ButtonPress-1>',forward)
    button.bind('<ButtonRelease-1>',stop)

    button2 = Button(frame1, text='Left')
    button2.grid(row=2, column=0, pady=10)
    button2.bind('<ButtonPress-1>',left)
    button2.bind('<ButtonRelease-1>',stop)

    button3 = Button(frame1, text='Right')
    button3.grid(row=2, column=2, pady=10)
    button3.bind('<ButtonPress-1>',right)
    button3.bind('<ButtonRelease-1>',stop)


    button4 = Button(frame1, text='Backward')
    button4.grid(row=3, column=1, pady=10)
    button4.bind('<ButtonPress-1>',back)
    button4.bind('<ButtonRelease-1>',stop)
    
    frame2 = Frame(root)
    frame2.grid(row=0, column=1)
    
    meula = Label(frame2, text="Remaining meulas: ", borderwidth=1)
    meula.grid(row=0, column=0, padx=40, pady=10)
    global meula2
    meula2 = Label(frame2, text=meula_num, borderwidth=1)
    meula2.grid(row=0, column=1, pady=10)
    increase_meula = Button(frame2, text="Increase Meulas", command=increase)
    increase_meula.grid(row=1, column=0, columnspan=2, padx=(40,0), pady=10)
    global message
    message = Label(frame2, text=message_txt, borderwidth=1)
    message.grid(row=2, column=0, columnspan=2, padx=(40,0), pady=10)
    root.mainloop()
    
if __name__=='__main__':
    command()