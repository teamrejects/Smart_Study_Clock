import tkinter as Tkinter 
import tkinter as tk  
from datetime import datetime 
from tkinter import *
counter1 = 0
running1 = False
counter = 0
running = False
root = Tkinter.Tk()  
root.title("ARK CS")      
root.minsize(width=350, height=550) 
laps = []
L =  []
t_counter = 0
import time
t_list = []
r=[]
T = 0
t_list2 = []
#____________________________________________________________________________________________________________________________________________________________________



# STUDY TIME TEXT
def study_time(text):
    T1 = Tkinter.Text(root, height = 1, width = 13 , highlightthickness = 0 ,borderwidth=0)  
    Fact1 = text
    T1.insert(Tkinter.END, Fact1)
    T1.pack(anchor = 'w') 
    T1.configure(state="disabled")
study_time("Study Clock :")


#CLOCK1
def counter_label1(label1 , t_counter):  #clock1
    def count1():  
        if running1:
            
            global t_counter
            global counter1    
            if counter1==0:              
                display1=""
            else: 
                tt1 = datetime.utcfromtimestamp(counter1) 
                
                string1 = tt1.strftime( "%H:%M:%S") 
                display1=string1  
    
            label1['text']=display1   
            label1.after(1000, count1)   
            counter1 += 1
            t_counter += 1
            return t_counter
            
    count1()

def Start1(label1):          #start button of clock 1 and stop button of clock2
    global running1 
    global running 
    running1=True
    running = False
    counter_label1(label1 , t_counter)  
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
def counter_label(label , T):    #clock2
    def count():  
        if running:  
            global counter
            tt = datetime.utcfromtimestamp(counter+T) # T = time to be added in the timer
            string = tt.strftime("%H:%M:%S") 
            display=string  
            label['text']=display   
            label.after(1000, count)   
            counter -= 1
            if counter == 66600:
                Start1(label1)
    count()       
def Start(label):            #start button of clock2 and stop button of clock2
    global running 
    global running1 
    running=True
    running1 = False
    counter_label(label ,T)  
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
    fc=Tkinter.Frame(root)
    var1 = Tkinter.IntVar()
    var2 = Tkinter.IntVar()
    var3 = Tkinter.IntVar()
    chk1 = Tkinter.Checkbutton(fc, text='1st', variable=var1)
    chk2 = Tkinter.Checkbutton(fc, text='2nd', variable=var2)
    chk3 = Tkinter.Checkbutton(fc, text='3rd', variable=var3)
    chk1.grid(row=0,column=0)
    chk2.grid(row=1,column=0)
    chk3.grid(row=2,column=0)

    def info():
        n1=var1.get()
        n2=var2.get()
        n3=var3.get()
        def limit1():
            if n1==1:
                t_list.append(t_counter)
                calc_T(t_list)
            
        def limit2():
            if n2==1:
                t_list.append(t_counter)
                calc_T(t_list)

        def limit3():
            if n3==1:
                t_list.append(t_counter)
                calc_T(t_list)
        limit1()
        limit2()
        limit3()
    
    b1=Tkinter.Button(fc,text="update",command=info,bg="yellow",state=Tkinter.NORMAL)
    b1.grid(row=3,column=1)


    fc.pack(anchor='sw')
checklists()

def close_window():
    global entry
    entry = E.get()
    L.append(entry)
    

def calc_T(t_list ):
    t_list2 = []
    global T
    for i in range(1, len(t_list)): 
        t_list2.append((t_list[i] - t_list[i-1])/3) 
    for ele in range(0, len(t_list2)): 
        T = T + t_list2[ele]
    
    return T 

E = Tkinter.Entry(root , highlightthickness = 0 ,borderwidth=0)
E.pack(anchor = CENTER)
B = Button(root, text = "Enter the websites \n that distract you.", command = close_window )
B.pack(anchor = S)


b2 = Tkinter.Button(root, text = "Exit", 
            command = root.destroy)
b2.pack(anchor = 'se')
root.mainloop()



























































#the checklist should be updated on clikcing so no update button should be required
#if checkbox gets checked it should not be able to get unchecked







#bugs / features to be added

# the stopwatch and timer should only work if websites to be blocked have been entered 
#disable update button when redeem timer is going on
# list only updates when exit button is clicked , it should update when submit button is clicked
# stop watch should start if timer reaches 00:00:00
#checklist should be editable
