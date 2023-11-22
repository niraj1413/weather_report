from tkinter import *
from tkinter import ttk  # Import ttk module for Combobox
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=08464b1c1de0a5e3efa963d8a6c8abc4").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    wt_label1.config(text=str(data["main"]["temp"]-273.15))
    wp_label1.config(text=data["main"]["pressure"])

#city_name = "raipur"
#data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=08464b1c1de0a5e3efa963d8a6c8abc4").json()
#print(data)

win = Tk()
win.title("Weather Report")
win.config(bg="blue")
win.geometry("500x600")

name_label = Label(win, text="WEATHER REPORT APP", font=("Time New Roman", 25, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

state_list = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]

city_name = StringVar()

com = ttk.Combobox(win, values=state_list, font=("Time New Roman", 20, "bold"),textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

w_label = Label(win, text="Wheather Climate", font=("Time New Roman", 12, "bold"),)
w_label.place(x=25, y=290, height=50, width=220)

w_label1 = Label(win, text="", font=("Time New Roman", 17, "bold"),)
w_label1.place(x=250, y=290, height=50, width=210)

wd_label = Label(win, text="Wheather Description", font=("Time New Roman", 12  , "bold"),)
wd_label.place(x=25, y=350, height=50, width=220)

wd_label1 = Label(win, text="", font=("Time New Roman", 17  , "bold"),)
wd_label1.place(x=250, y=350, height=50, width=210)

wt_label = Label(win, text="Temperature", font=("Time New Roman", 15  , "bold"),)
wt_label.place(x=25, y=410, height=50, width=220)

wt_label1 = Label(win, text="", font=("Time New Roman", 12  , "bold"),)
wt_label1.place(x=250, y=410, height=50, width=210)

wp_label = Label(win, text="Pressure", font=("Time New Roman", 15 , "bold"), )
wp_label.place(x=25, y=470, height=50, width=220)

wp_label1 = Label(win, text="", font=("Time New Roman", 17 , "bold"), )
wp_label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win , text=" CHECK ", font=("Time New Roman", 17, "bold"), relief=RAISED, command= data_get)
done_button.place(x=170, y=190, height=50, width=150)

win.mainloop()
