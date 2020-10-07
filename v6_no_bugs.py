import tkinter as Tkinter 
import tkinter as tk  
from datetime import datetime 
from tkinter import *
counter1 = 66600
running1 = False
counter = 66600
running = False
root = Tkinter.Tk()  
root.title("Stopwatch")      
root.minsize(width=350, height=550) 
laps = []
L =  []
 
import time

#____________________________________________________________________________________________________________________________________________________________________


# STUDY TIME TEXT
def study_time(text):
    T1 = Tkinter.Text(root, height = 1, width = 13 , highlightthickness = 0 ,borderwidth=0)  
    Fact1 = text
    T1.insert(Tkinter.END, Fact1)
    T1.pack(anchor = 'w') 
    T1.configure(state="disabled")
study_time("Study Clock :")

"complete checklists! to get more break time to browse the blocked websites =>"

#CLOCK1
def counter_label1(label1):  #clock1
    def count1():  
        if running1:  
            global counter1    
            if counter1==0:              
                display1=""
            else: 
                tt1 = datetime.fromtimestamp(counter1) 
                
                string1 = tt1.strftime( "%H:%M:%S") 
                display1=string1  
    
            label1['text']=display1   
            label1.after(1000, count1)   
            counter1 += 1
    count1()       
def Start1(label1):          #start button of clock 1 and stop button of clock2
    global running1 
    global running 
    running1=True
    running = False
    counter_label1(label1)  
    start1['state']='disabled'
    start['state']='normal'

# CLOCK1 ATTRIBUTES
label1 = Tkinter.Label(root, text="00:00:00", fg="black", font="Verdana 30 bold")  
label1.pack(anchor = 'w')  
f = Tkinter.Frame(root) 
start1 = Tkinter.Button(f, text='Start', width=6, command=lambda:Start1(label1))  
f.pack(anchor = 'w',pady=5) 
start1.pack(side="left")  



# BREAK TIME TEXT
def break_time(text):
    T = Tkinter.Text(root, height = 1, width = 13 , highlightthickness = 0 ,borderwidth=0)  
    Fact = text
    T.insert(Tkinter.END, Fact)
    T.pack(anchor = 'w')  
    T.configure(state="disabled") 
break_time("Break Timer :")



#CLOCK2
def counter_label(label):    #clock2
    def count():  
        if running:  
            global counter
            tt = datetime.fromtimestamp(counter+120) # T = time to be added in the timer
            string = tt.strftime("%H:%M:%S") 
            display=string  
            label['text']=display   
            label.after(1000, count)   
            counter -= 1
    count()       
def Start(label):            #start button of clock2 and stop button of clock2
    global running 
    global running1 
    running=True
    running1 = False
    counter_label(label)  
    start['state']='disabled'
    start1['state']='normal'
 
# CLOCK2 ATTRIBUTES
label = Tkinter.Label(root, text="00:00:00", fg="black", font="Verdana 30 bold" )  
label.pack(anchor = 'w')  
f = Tkinter.Frame(root) 
start = Tkinter.Button(f, text='Redeem ', width=6, command=lambda:Start(label))  
f.pack(anchor = 'w',pady=5) 
start.pack(side="left")  

def checklist_Text(text):
    T1 = Tkinter.Text(root, height = 2, width = 44 , highlightthickness = 0 ,borderwidth=0)  
    Fact1 = text
    T1.insert(Tkinter.END, Fact1)
    T1.pack(anchor = 'w') 
    T1.configure(state="disabled")
checklist_Text("Complete Checklists! to get more break time\nto browse the blocked websites =>")

# CHECKLIST
def checklists():
    Checkbutton1 = IntVar()   
    Checkbutton2 = IntVar()   
    Checkbutton3 = IntVar() 
    Button1 = Checkbutton(root, text = "Checklist1",  
                        variable = Checkbutton1, 
                        onvalue = 1, 
                        offvalue = 0, 
                        height = 2, 
                        width = 10)  
    Button2 = Checkbutton(root, text = "Checklist2", 
                        variable = Checkbutton2, 
                        onvalue = 1, 
                        offvalue = 0, 
                        height = 2, 
                        width = 10)   
    Button3 = Checkbutton(root, text = "Checklist3", 
                        variable = Checkbutton3, 
                        onvalue = 1, 
                        offvalue = 0, 
                        height = 2, 
                        width = 10)       
    Button1.pack(anchor = "w")   
    Button2.pack(anchor = "w")   
    Button3.pack(anchor = "w")
checklists()

def close_window():
    global entry
    entry = E.get()
    L.append(entry)
    

E = Tkinter.Entry(root , highlightthickness = 0 ,borderwidth=0)
E.pack(anchor = CENTER)
B = Button(root, text = "Enter the websites \n that distract you.", command = close_window )
B.pack(anchor = S)


#bugs / features to be added
# the stopwatch and timer should only work if websites to be blocked have been entered 
# when the timer runs out it starts from 23:59:59 , instead when timer times out (counter = 66600) then study clock should start
# we need to make a button to add more checklists


# EXIT BUTTON
b2 = Tkinter.Button(root, text = "Exit", 
            command = root.destroy)
b2.pack(anchor = 'se')
root.mainloop() 
print(L)

