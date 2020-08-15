# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 20:15:58 2020

@author: dozie
"""

import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\dozie\Downloads\FIFA 20 Player Ratings.xlsx")
index=list(df.index)
df['Index']=df.index
df=df[['Index', 'Name', 'Position(s)', 'Rating']]

from tkinter import *
from tkinter import messagebox

def ChoiceA():
    global value
    value="A"
    check()
    
def ChoiceB():
    global value
    value="B"
    check()
        
def restart():
    global set
    set=np.random.randint(index[0],index[len(index)-1],2)
    L1.configure(text=df[df['Index']==set[0]].iloc[0]['Name']+', '+ df[df['Index']==set[0]].iloc[0]['Position(s)'])
    L2.configure(text=df[df['Index']==set[1]].iloc[0]['Name']+', '+df[df['Index']==set[1]].iloc[0]['Position(s)'])
    
    global ans
    if int(df[df['Index']==set[0]]['Rating'])>int(df[df['Index']==set[1]]['Rating']):
        ans="A"
    elif int(df[df['Index']==set[0]]['Rating'])<int(df[df['Index']==set[1]]['Rating']):
        ans="B"
    else:
        ans="C"

def check():
    if ans=="C":
        messagebox.showinfo("Play Again", "Play again \n\n"+str(df[df['Index']==set[0]].iloc[0]['Rating'])+' vs '+str(df[df['Index']==set[1]].iloc[0]['Rating']))
        restart()
    elif value==ans:
        messagebox.showinfo("Win", "You win! \n\n"+str(df[df['Index']==set[0]].iloc[0]['Rating'])+' vs '+str(df[df['Index']==set[1]].iloc[0]['Rating']))
        global score
        score=score+10
        L3.configure(text="Score = " + str(score))
        restart()
    else:
        messagebox.showinfo("Lose", "You lose!" +"\n\n"+str(df[df['Index']==set[0]].iloc[0]['Rating'])+' vs '+str(df[df['Index']==set[1]].iloc[0]['Rating'])+"\n\n"+"Final score: "+str(score))
        top.destroy()

top = Tk(className=" FIFA Ratings Game")
top.geometry("500x250")

B1 = Button(top, text = "Choice A", command = ChoiceA, width=15)
B1.place(x = 50,y = 125)
B2 = Button(top, text = "Choice B", command = ChoiceB, width=15)
B2.place(x = 300,y = 125)

score=0
set=np.random.randint(index[0],index[len(index)-1],2)

L0 = Label(top, text='Who has the higher FIFA rating?')
L0.place(x=150,y=20)
L1 = Label(top, text=df[df['Index']==set[0]].iloc[0]['Name']+', '+ df[df['Index']==set[0]].iloc[0]['Position(s)']) 
L1.place(x=50,y=75) 
L2 = Label(top, text=df[df['Index']==set[1]].iloc[0]['Name']+', '+df[df['Index']==set[1]].iloc[0]['Position(s)'])
L2.place(x=300,y=75)
L3 = Label(top, text="Score = " + str(score))
L3.place(x=200,y=200)

if int(df[df['Index']==set[0]]['Rating'])>int(df[df['Index']==set[1]]['Rating']):
    ans="A"
elif int(df[df['Index']==set[0]]['Rating'])<int(df[df['Index']==set[1]]['Rating']):
    ans="B"
else:
    ans="C"

top.mainloop()