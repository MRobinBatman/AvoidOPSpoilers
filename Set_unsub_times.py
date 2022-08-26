# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import datetime
import customtkinter
from tkinter import messagebox

#Get todays date to enter into the calendar so you can have the correct day displayed
now = datetime.datetime.now()

year = int(now.strftime("%Y"))
month = int(now.strftime("%m"))
day = int(now.strftime("%d"))

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()


style = ttk.Style(root)

style.theme_use('alt')


root.title("Unsubscribe to Avoid spoilers:")

root.iconbitmap('OnePiece_Spoiler_Blocker.ico')

root.geometry("400x800")


cal = Calendar(root, selectmode = 'day', year = year, month = month, day = day, background="#3B8ED0", bordercolor="black")

cal.pack(pady=20)

timeframe = []

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

def break_up_date(date):
    d_splt = date.split("/")
    m = int(d_splt[0])
    d = int(d_splt[1])
    y = int(d_splt[2])
    y +=2000
    lis = []
    lis.append(m)
    lis.append(d)
    lis.append(y)
    # print(lis)
    result = datetime.date(y,m,d)
    return result

#Defining the functions that will pass back the days you select
def set_end_date():
    # end_date.config(text="Selected Date is: " + cal.get_date())
    ed = cal.get_date()
    print(ed)
    # datetime.datetime.
    dt_formatted = break_up_date(ed)
    result = dt_formatted.strftime("%a")
    print(result)
    end_date.configure(text="Selected Date is: " + " " + result + " " + dt_formatted.strftime("%x"))
    # timeframe.append((result,cal.get_date()))
    timeframe.append((result,dt_formatted.strftime("%x")))
    return result

def set_begining_date():
    # begin_date.config(text="Selected Date is: " + cal.get_date())
    bd = cal.get_date()
    print(bd)
    dt_formatted = break_up_date(bd)
    
    result = dt_formatted.strftime("%a")
    print(result)
    begin_date.configure(text="Selected Date is: " + " " + result + " " + dt_formatted.strftime("%x"))
    # timeframe.append((result,cal.get_date()))
    timeframe.append((result,dt_formatted.strftime("%x")))
    return result

def set_unsub_time_frame():
    start = timeframe[0][0]
    end = timeframe[1][0]
    print("Timeframe set to: " + start + " - " + end + ".")
    confirmation = "Timeframe set to: " + start + " - " + end + "."
    submit.configure(text = confirmation)

def set_date_file():
    start = timeframe[0][0]
    end = timeframe[1][0]
    file = open("dates.txt",'w')
    file.truncate
    # file.write(start+"\n"+end)
    file.write(start+" "+ timeframe[0][1]+"\n"+end+" "+timeframe[1][1])
    file.close()
    confirm_changes.configure(text= "Confirmed!")
    

### Put the rest of the Tkinter Frame Together
begin_date = customtkinter.CTkLabel(root,text="")
customtkinter.CTkButton(root, text="Set beginning of the sunsub time", command = set_begining_date).pack(pady = 20)
begin_date.pack(pady=20)

end_date = customtkinter.CTkLabel(root,text="")
customtkinter.CTkButton(root, text="Set the ending day of the unsub time", command = set_end_date).pack(pady=20)
end_date.pack(pady=20)

submit = customtkinter.CTkLabel(root,text="")
customtkinter.CTkButton(root, text="Get Unsubscribe timeframe.", command = set_unsub_time_frame).pack(pady=20)
submit.pack(pady=20)

confirm_changes = customtkinter.CTkLabel(root,text="")
customtkinter.CTkButton(root, text="Confirm Changes", command= set_date_file).pack(pady=20)
confirm_changes.pack(pady=20)
root.mainloop()
