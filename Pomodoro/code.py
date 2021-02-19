import pygame
import os
import tkinter as tk
from tkinter import font
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
    BEAUTIFUL = (51, 255, 255)  # don't know the color name so...
    BLACK = (0, 0, 0)
    ORANGE = (255, 69, 0)

    WIDTH = 100

    HEIGHT = 100

    MAIN_WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    FONT = pygame.font.SysFont('comicsans', 50)

    run = True

    SECONDS = 60
    TIME = MINUTES*SECONDS

    while run:

        MAIN_WIN.fill(BEAUTIFUL)

        pygame.time.wait(1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        message = str(TIME//60).zfill(2) + ':' + str(TIME % 60).zfill(2)
        txt = FONT.render(message, 1, ORANGE)

        MAIN_WIN.blit(txt, (WIDTH//2-txt.get_width() //
                            2, HEIGHT//2-txt.get_height()//2))

        TIME -= 1

        if TIME < 0:
            run = False

        pygame.display.update()

    pygame.quit()


def setting_window():
    pass


def graph_window(show_graph=True):

    with open('data.json') as json_file:
        data = json.load(json_file)

    today = date.today()

    day = today.day

    key = today.strftime("%b-%Y")  # creating the key

    if key not in data:

        month = today.month

        year = today.year

        no_of_weekend, days_in_month = monthrange(year, month)

        month_data = [0]*(days_in_month+1)

        data[key] = month_data

    # graph modification
    if show_graph:
        x_axis = list(range(1, 1+len(data[key])))

        y_axis = data[key]

        graph = plt  # plt object

        graph.plot(x_axis, y_axis, label='DAYS')

        graph.title('YOUR PROGRESS GRAPH')

        graph.xlabel('DAYS')

        graph.ylabel('NO OF POMODORO CYCLE')

        graph.show()

    else:
        data[key][day] += 1  # increase the no of pomodoro cycle by 1

    prev_data = open("data.json", "w")

    # this become heavy operation if we have lot of data
    json.dump(data, prev_data)

    prev_data.close()


# about window
def about_us_window():

    about_win = tk.Tk(screenName="About Us")

    about_win.title('POMODORO')

    about_win.geometry("800x590")

    sys.stdin = open('about_us.txt', 'r')

    total = ''

    for i in range(100):
        try:
            total = sys.stdin.readline().strip()
        except:
            break

        label = tk.Label(about_win,
                         text=total,
                         bg='orange',
                         font=('Times', '14', 'bold'))

        label.pack()


def set_default_time_button_help():

    global MINUTES

    # global minutes

    MINUTES = 25  # we are setting the minutes to 25

    timer_window(MINUTES)

    timer_window(5)

    update_json()

    # minutes.select_clear()


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

    minutes.select_clear()


def update_json():
    graph_window(False)

def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

# main window
root = tk.Tk(screenName="Main")
root.title('POMODORO')
root.configure(bg="#33ffff")
root.geometry("530x320")

# colors 
COL_A = "#ec7063"
COL_B = "#ea220e"
COL_C = "#61ee10"

MINUTES = 25
# creating the label

label_minute = tk.Label(root,
                        text="ENTER MINUTES : ",
                        bg=COL_C,
                        cursor='heart',
                        width=15,
                        bd=3,
                        height=3,
                        relief=tk.RAISED,
                        activeforeground='red',
                        font=('Times', '14', 'bold'))
label_minute.grid(row=0, column=0, padx=10, pady=10)

# taking input from the user
minutes = tk.Entry(root, text='50',
                   bd=4,
                   width=3,
                   bg='grey',
                   fg='white',
                   cursor="dotbox",
                   selectborderwidth=6,
                   font=('Times', '35', 'bold'))
minutes.insert(0, "25")
minutes.grid(row=0, column=1, padx=10, pady=10)

# creating the buttons
set_default_time_button = tk.Button(root,
                                    bg=COL_C,
                                    width=15,
                                    bd=4,
                                    height=2,
                                    font=('Times', '14', 'bold'),
                                    activebackground='blue',
                                    activeforeground='red',
                                    text='25 MINUTES',
                                    command=set_default_time_button_help)
set_default_time_button.grid(row=0, column=2, padx=10, pady=10)

# go button
go_button = tk.Button(root,
                      text='GO',
                      command=go_button_help,
                      height=4,
                      width=13,
                      bd=4,
                      bg = COL_B,
                      relief=tk.RAISED,
                      activebackground='blue',
                      font=('Times', '10', 'bold'),
                      activeforeground='red')
go_button.grid(row=1, column=1, padx=10, pady=10)

# graph window button
graph_window_button = tk.Button(root, text="SHOW GRAPH",
                                bd=4,
                                justify=tk.LEFT,
                                height=4,
                                width=13,
                                relief=tk.RAISED,
                                activeforeground='red',
                                activebackground='blue',
                                bg = COL_A,
                                font=('Times', '14', 'bold'),
                                command=graph_window)
graph_window_button.grid(row=2, column=0, padx=10, pady=10)

# setting window buttons
setting_button = tk.Button(root, text="SETTINGS",
                           bd=4,
                           justify=tk.LEFT,
                           height=4,
                           width=12,
                           relief=tk.RAISED,
                           activeforeground='red',
                           bg = COL_A,
                           font=('Times', '14', 'bold'),
                           activebackground='blue',
                           command=setting_window)
setting_button.grid(row=2, column=1, pady=10)

# about window buttons
about_button = tk.Button(root,
                         text="ABOUT US",
                         bd=4,
                         bg = COL_A,
                         justify=tk.LEFT,
                         height=4,
                         width=12,
                         relief=tk.RAISED,
                         activeforeground='red',
                         font=('Times', '14', 'bold'),
                         activebackground='blue',
                         command=about_us_window)
about_button.grid(row=2, column=2, padx=10, pady=10)


# this is the infinte loop for the root window
root.mainloop()
