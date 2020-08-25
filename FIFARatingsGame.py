import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\dozie\Downloads\FIFA 20 Player Ratings.xlsx")
index=list(df.index)
df['Index']=df.index
df=df[['Index', 'Name', 'Position(s)', 'Rating']]

remarks=["Life isn't all sunshine and rainbows after all.",
        '       You win some, you lose some.',
        'Gotta brush up on your football knowledge.',
        "        That's gotta be disappointing."]

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

def reveal():
    global L8, L9
    L8 = Label(top, text=str(df[df['Index']==set[0]].iloc[0]['Rating']),background='lavender')
    L8.place(x=100,y=100)
    L9 = Label(top, text=str(df[df['Index']==set[1]].iloc[0]['Rating']),background='lavender')
    L9.place(x=350,y=100)
    top.after(3000,L7.destroy)
    top.after(3000,L8.destroy)
    top.after(3000,L9.destroy)
        
def lose():       
    global L4, L5, L6, L10, B3, B4
    L4 = Label(top, width=70,height=20,background='lavender')
    L4.place(x=0,y=0)
    L6 = Label(top, text="Final score = " + str(score),background='lavender',font=("arial",15))
    L6.place(x=170,y=110)
    L5 = Label(top, text="You lose!", background='lavender', foreground='red',font=("arial",50))
    L5.place(x=100,y=10)
    B3 = Button(top, text = "Play again", command = playagain, width=15)
    B3.place(x = 100,y = 200)
    B4 = Button(top, text = "Quit", command = quit, width=15)
    B4.place(x = 250,y = 200)
    remark=np.random.randint(0,len(remarks))
    L10 = Label(top, text=remarks[remark],background='lavender',font=("arial",10))
    L10.place(x=125,y=150)

def playagain():
    L4.destroy()
    L5.destroy()
    L6.destroy()
    L10.destroy()
    B3.destroy()
    B4.destroy()
    global score
    score=0
    L3.configure(text="Score = " + str(score))
    restart()
    
def quit():
    top.destroy()        
        
def check():
    if ans=="C":
        global L7
        L7 = Label(top, text='Play again',background='lavender',font=("arial",15))
        L7.place(x=195,y=165)
        reveal()
        top.after(3000,restart)        
    elif value==ans:
        global score
        score=score+10
        L3.configure(text="Score = " + str(score))        
        L7 = Label(top, text='Correct!', foreground='green',background='lavender',font=("arial",15))
        L7.place(x=195,y=165)
        reveal()
        top.after(3000,restart)       
    else:       
        L7 = Label(top, text='Wrong!', foreground='red',background='lavender',font=("arial",15))
        L7.place(x=195,y=165)
        reveal()
        top.after(3000,lose)
    
top = Tk(className=" FIFA Ratings Game")
top.geometry("500x250")
top.configure(background='lavender')

B1 = Button(top, text = "Choice A", command = ChoiceA, width=15)
B1.place(x = 50,y = 125)
B2 = Button(top, text = "Choice B", command = ChoiceB, width=15)
B2.place(x = 300,y = 125)
B5 = Button(top, text = "Quit", command = quit, width=10)
B5.place(x = 400,y = 220)

global score
score=0
set=np.random.randint(index[0],index[len(index)-1],2)

L0 = Label(top, text='Which player has the higher FIFA rating?',background='lavender',font=("arial",15))
L0.place(x=60,y=20)
L1 = Label(top, text=df[df['Index']==set[0]].iloc[0]['Name']+', '+ df[df['Index']==set[0]].iloc[0]['Position(s)'],background='lavender') 
L1.place(x=50,y=75) 
L2 = Label(top, text=df[df['Index']==set[1]].iloc[0]['Name']+', '+df[df['Index']==set[1]].iloc[0]['Position(s)'],background='lavender')
L2.place(x=300,y=75)
L3 = Label(top, text="Score = " + str(score),background='lavender')
L3.place(x=200,y=200)

if int(df[df['Index']==set[0]]['Rating'])>int(df[df['Index']==set[1]]['Rating']):
    ans="A"
elif int(df[df['Index']==set[0]]['Rating'])<int(df[df['Index']==set[1]]['Rating']):
    ans="B"
else:
    ans="C"

top.mainloop()