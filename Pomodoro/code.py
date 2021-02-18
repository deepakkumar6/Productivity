import pygame
import os 
import tkinter as tk 
from matplotlib import pyplot as plt
import json
import sys
from datetime import date
from calendar import monthrange

 

# time_window 
# setting_window
# graph_window
# about_us window
# root window

def timer_window(MINUTES):
    # Initilising the pygame 
    pygame.init()

    # color's code
    BEAUTIFUL = (51,255,255) # don't know the color name so...
    BLACK = (0,0,0)
    ORANGE = (255,69,0)

    WIDTH = 100 

    HEIGHT = 100 

    MAIN_WIN = pygame.display.set_mode((WIDTH,HEIGHT))

    FONT = pygame.font.SysFont('comicsans',50)

    run = True 

    SECONDS = 60
    TIME = MINUTES*SECONDS

    while run:

        MAIN_WIN.fill(BEAUTIFUL)

        pygame.time.wait(1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

        message = str(TIME//60).zfill(2) +':'+ str(TIME%60).zfill(2)
        txt = FONT.render(message,1,ORANGE)

        MAIN_WIN.blit(txt,(WIDTH//2-txt.get_width()//2,HEIGHT//2-txt.get_height()//2))

        TIME-=1

        if TIME<0:
            run = False 

        pygame.display.update()

    pygame.quit()

def setting_window():
    pass
    

def graph_window(show_graph = True):

    with open('data.json') as json_file:
        data = json.load(json_file)

    today = date.today()

    day = today.day

    key = today.strftime("%b-%Y") # creating the key 

    if key not in data:

        month = today.month

        year = today.year

        no_of_weekend,days_in_month = monthrange(year,month)

        month_data = [0]*(days_in_month+1)

        data[key] = month_data

    
    # graph modification
    if show_graph:
        x_axis = list(range(1,1+len(data[key])))

        y_axis = data[key]

        graph = plt # plt object

        graph.plot(x_axis,y_axis,label = 'DAYS')

        graph.title('YOUR PROGRESS GRAPH')

        graph.xlabel('DAYS')

        graph.ylabel('NO OF POMODORO CYCLE')

        graph.show()

    else:
        data[key][day] += 1 # increase the no of pomodoro cycle by 1

    prev_data = open("data.json","w")
    
    json.dump(data,prev_data) # this become heavy operation if we have lot of data 

    prev_data.close()


# about window 
def about_us_window():

    about_win = tk.Tk(screenName="About Us")

    about_win.title('POMODORO')

    about_win.geometry("400x200")

    sys.stdin=open('about_us.txt','r')

    total = ''

    for i in range(100):
        try:
            total = sys.stdin.readline().strip()
        except:
            break

        label = tk.Label(about_win,text = total)

        label.pack()
    

def set_default_time_button_help():

    global MINUTES

    MINUTES = 25 # we are setting the minutes to 25

    timer_window(MINUTES)

    timer_window(5)

    update_json()

def go_button_help():

    global MINUTES 

    data = minutes.get()

    try:
        min = int(data)
    except:
        min = 25 

    MINUTES = min 

    timer_window(MINUTES)

    timer_window(5)

    update_json()

def update_json():
    graph_window(False)



# main window 
root = tk.Tk(screenName="Main")
root.title('POMODORO')
root.geometry("400x200")

MINUTES = 25

# creating the label
label_minute = tk.Label(root,text = "ENTER MINUTES : ",bg = 'orange',cursor='heart',width=15,height = 3,relief=tk.RAISED,font=('Times', '10', 'italic'))
label_minute.grid(row = 0 , column = 0,padx = 10,pady = 10)

# taking input from the user 
minutes = tk.Entry(root,text = '25')
minutes.grid(row= 0,column = 1,padx = 10,pady = 10)

#creating the buttons
set_default_time_button = tk.Button(root,text = 'SET DEFAULT',command = set_default_time_button_help)
set_default_time_button.grid(row = 0,column = 2,padx = 10,pady = 10)

go_button = tk.Button(root,text = 'READY TO GO',command = go_button_help,relief=tk.FLAT)
go_button.grid(row = 1,column = 1,padx = 10,pady = 10)

graph_window_button = tk.Button(root,text="SHOW GRAPH",command = graph_window)
graph_window_button.grid(row = 2,column = 0,pady = 10)

setting_button = tk.Button(root,text="SETTINGS")
setting_button.grid(row = 2, column = 1,pady = 10)

about_button = tk.Button(root,text = "ABOUT US",bd = 4,command = about_us_window)
about_button.grid(row = 2,column = 2,padx = 10,pady = 10)

root.mainloop()







        