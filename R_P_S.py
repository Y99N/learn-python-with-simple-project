from tkinter import *
import random

root = Tk()
root.geometry("350x300")
root.title('Rock Papper Scissor')
me = ccc= 0

def computer():
    c = ["Scissor","Papper","Rock"]
    cc = random.choice(c)
    return cc 

global scoreme
global scorehim
scoreme=scorehim=0

def winner(me , him ): 
    global scoreme
    global scorehim
    if me == "Papper" and him == "Rock": 
        t = Label(root,text='  you win  ').grid(row=4,column=1) 
        scoreme+=1  
        myscore = Label(root,text='my score : ').grid(row=5 ,column=1)
        my = Label(root,text = scoreme).grid(row=6,column=1)
        cscore = Label(root,text='computer score : ').grid(row=7 ,column=1)
        him = Label(root,text=scorehim).grid(row=8,column=1)

    elif me == "Scissor" and him == "Papper":
        t = Label(root,text='  you win  ').grid(row=4,column=1)
        scoreme+=1  
        myscore = Label(root,text='my score : ').grid(row=5 ,column=1)
        my = Label(root,text = scoreme).grid(row=6,column=1)
        cscore = Label(root,text='computer score : ').grid(row=7 ,column=1)
        him = Label(root,text=scorehim).grid(row=8,column=1)
    elif me == "Rock" and him == "Scissor":
        t = Label(root,text='  you win  ').grid(row=4,column=1)
        scoreme+=1  
        myscore = Label(root,text='my score : ').grid(row=5 ,column=1)
        my = Label(root,text = scoreme).grid(row=6,column=1)
        cscore = Label(root,text='computer score : ').grid(row=7 ,column=1)
        him = Label(root,text=scorehim).grid(row=8,column=1)
    elif me == him:
        t = Label(root,text='  no winner  ').grid(row=4,column=1)
        myscore = Label(root,text='my score : ').grid(row=5 ,column=1)
        my = Label(root,text = scoreme).grid(row=6,column=1)
        cscore = Label(root,text='computer score : ').grid(row=7 ,column=1)
        him = Label(root,text=scorehim).grid(row=8,column=1)
    else:
        t = Label(root,text='computer wins').grid(row=4,column=1)
        scorehim+=1  
        myscore = Label(root,text='my score : ').grid(row=5 ,column=1)
        my = Label(root,text = scoreme).grid(row=6,column=1)
        cscore = Label(root,text='computer score : ').grid(row=7 ,column=1)
        him = Label(root,text=scorehim).grid(row=8,column=1)

def game(b):
    cc = computer()
    text = Label(root,text= "you choosed : ").grid(row=2,column=1)
    text2 = Label(root,text= "  "+b["text"]+"  ").grid(row=2,column=2)
    txt = Label(root,text="computer choosed : ").grid(row=3,column=1)
    txt2 = Label(root,text="  "+cc+"  ").grid(row=3,column=2)
    winner(b["text"],cc)

def reset():
    global scoreme
    global scorehim
    scoreme=scorehim=0
    myscore = Label(root,text='my score : ').grid(row=5 ,column=1)
    my = Label(root,text = scoreme).grid(row=6,column=1)
    cscore = Label(root,text='computer score : ').grid(row=7 ,column=1)
    him = Label(root,text=scorehim).grid(row=8,column=1)

text1 = Label(root, text= 'Take a choice : ')
text1.grid(row=0, column=1)
b1 = Button(root,text='Rock',padx=30,pady=10,command=lambda:game(b1),bg='#ff9999')
b1.grid(row=1,column=0)
b2 = Button(root,text='Scissor',padx=30,pady=10,command=lambda:game(b2),bg='#8cff66')
b2.grid(row=1,column=1)
b3 = Button(root,text='Papper',padx=30,pady=10,command=lambda:game(b3),bg='#4ddbff')
b3.grid(row=1,column=2)
b4=Button(root,text='reset',bg='gray',command=reset).grid(row=9,column=2)

root.mainloop()
