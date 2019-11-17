import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import os
import sys
import tensorflow as tf
import numpy as np

Choice_List = [
    ("0:Irrelevant","1:Sharp_Curve","2:Traffic","3:Junction","4:Divider","5:BadRoads","6:Near Residential Area","7:Near Hospitals","8:Near Schools","9:ParkingLot","10:U-Turn","11:Unlit roads","12:Rural highways","13:signals","14:Pedestrian path","15:Flyovers","16:Construction work","17:Highways","18:Unlit roads","19:Slippery road","20:Underpass"),
    ("0:Excellent","1:Worst","2:Very Bad","3:Bad","4:Good","5:Very Good","6:Worse","7:Better"),
    ("0:Not_Specified","1:Rain","2:Fog","3:Haze","4:Heat","5:Lightning","6:Flooding","7:Wind","8:Snow","9:winter","10:Cloudy","16:Winter"),
    ("0:Irrelevant","1:Negligence in Driving","2:Road conditions","3:Weather conditions","4:Night driving","5:Unforeseen conditions","6:Tire blowouts"),
    ("0:Sunday","1:Monday","2:Tuesday","3:Wednesday","4:Thursday","5:Friday","6:Saturday"),
    ("1:January","2:February","3:March","4:April","5:May","6:June","7:July","8:August","9:September","10:October","11:November","12:December"),
    tuple(range(24)),
    ("0:Irrelavant","1:Tar roads","2:Concrete Roads","3:Muddy Roads","4:Pedestrian roads","5:Worn out roads","6:Flyover","7:Footpath")
]
mapping_dict = {0:"Minor",1:"Major",2:"Grevious",3:"Nearly_Fatal",4:"Fatal"}
default_value_list = [0,0,0,0,0,0,0,0,0,0,0]

root = Tk()
root.geometry("1000x1000")
root.title("Dashboard")

l1 = tk.Label(root,text='MoRTH Data Analytic Tool',font=("Agency FB",25))
l1.grid(column = 20,row=0)
#l1.pack()

def click():
    default_value_list[0] = int(age.get())
    default_value_list[1] = Choice_List[0].index(Acc_spot.get())
    default_value_list[2] = 1
    default_value_list[3] = int(road.get())
    default_value_list[4] = Choice_List[7].index(surface.get())
    default_value_list[5] = Choice_List[1].index(road_cond.get())
    default_value_list[6] = Choice_List[2].index(weather.get())
    default_value_list[7] = Choice_List[3].index(main.get())
    default_value_list[8] = Choice_List[4].index(day.get())
    default_value_list[9] = Choice_List[5].index(month.get())
    default_value_list[10] = Choice_List[6].index(int(hour.get()))
    model = tf.keras.models.load_model('trained_model (2).h5')
    arr = np.array(default_value_list).reshape((1,11))
    print(default_value_list)
    pred = model.predict(arr)
    len(pred)
    level_of_accident = np.argmax(pred)
    percentage_confidence = pred[level_of_accident]
    print(type(pred))
    Printing = "According To The Above Given Conditions, \nA {} (Level {}) is predicted \nwith {}% confidence.".format(mapping_dict[level_of_accident],level_of_accident,int((percentage_confidence[level_of_accident]*100))
    print(Printing)
    display = Label(root,text=Printing,font=("Arial Bold",10))
    display.grid(row=50,column=10)

l3 = Label(root,text='Prediction',font=("Arial Bold",15))
l3.grid(row=9,column=0)

l14 = Label(root,text='Age',font=("Arial Bold",10))
l14.grid(row=12,column=10)
age=Entry(root,width=10)
age.grid(row=13,column=10)


l4 = Label(root,text='Accident Spot',font=("Arial Bold",10))
l4.grid(row=18,column=10)
Acc_spot = Combobox(root)
Acc_spot['values']=Choice_List[0]
Acc_spot.grid(row=19,column=10)
Acc_spot.current(2)


l5 = Label(root,text='Junction Control',font=("Arial Bold",10))
l5.grid(row=24,column=10)
junction=Entry(root,width=10)
junction.grid(row=25,column=10)


l6 = Label(root,text='Road Width In Feet',font=("Arial Bold",10))
l6.grid(row=30,column=10)
road = Entry(root,width=10)
road.grid(row=31,column=10)


l7 = Label(root,text='Surface Type',font=("Arial Bold",10))
l7.grid(row=36,column=10)
surface = Combobox(root)
surface['values'] = Choice_List[7]
surface.grid(row=37,column=10)
surface.current(2)


l8 = Label(root,text='Road Condition',font=("Arial Bold",10))
l8.grid(row=12,column=100)
road_cond = Combobox(root)
road_cond['values']=Choice_List[1]
road_cond.grid(row=13,column=100)
road_cond.current(2)


l9 = Label(root,text='Weather',font=("Arial Bold",10))
l9.grid(row=18,column=100)
weather = Combobox(root)
weather['values']=Choice_List[2]
weather.grid(row=19,column=100)
weather.current(2)

l10 = Label(root,text='Main Cause',font=("Arial Bold",10))
l10.grid(row=24,column=100)
main = Combobox(root)
main['values']=Choice_List[3]
main.grid(row=25,column=100)
main.current(2)



l11 = Label(root,text='Day Of The Week',font=("Arial Bold",10))
l11.grid(row=30,column=100)
day = Combobox(root)
day['values']=Choice_List[4]
day.grid(row=31,column=100)
day.current(2)


l12 = Label(root,text='Month',font=("Arial Bold",10))
l12.grid(row=36,column=100)
month = Combobox(root)
month['values']=Choice_List[5]
month.grid(row=37,column=100)
month.current(2)



l13 = Label(root,text='Hour',font=("Arial Bold",10))
l13.grid(row=42,column=100)
hour = Combobox(root)
hour['values']=Choice_List[6]
hour.grid(row=43,column=100)
hour.current(2)


bt10=Button(root,text="Enter",command=click,width=10)
bt10.grid(row=12,column=20)


root.mainloop()






 


































