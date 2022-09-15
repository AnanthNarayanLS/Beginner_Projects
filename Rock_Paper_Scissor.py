

import random
from tkinter import *
import pygame

root = Tk()
root.geometry("700x400")
root.config(bg='#4C0033')

pygame.mixer.init()
pygame.mixer.music.load('req/pixelsound.mp3')
pygame.mixer.music.play(loops=1000)


l1 = Label(root,text='',font=('times',15))
l2 = Label(root,text='',font=('times',15))
l3 = Label(root,text='',font=('times',10))


def player1():

    rock = '''  
        _____
    ---'   ____)  
          (_____)  
          (_____)  
          (____)
    ---.__(___)  
    '''

    paper = '''  
  ____
    ---'   ____)___ 
              ___________)  
              __________)  
             _________)
    ---.__________)  
    '''

    scissors = '''  
    
___
    ---'   ____)____
              __________)  
           ____________)  
          (____)
    ---.__(___)  
    '''

    options = [rock,scissors,paper]
    p1 = random.choice(options)
    p2 = random.choice(options)

    if (p1==rock and p2==scissors) or (p1==paper and p2==rock) or (p1==scissors and p2==paper):
        res = 'YOU WON !!'
    elif p1==p2:
        res = "IT'S A TIE"
    else:
        res = 'YOU LOST!!'

    l1.config(text=f'{p1}',bg='#277BC0')
    l1.place(x=50,y=100)
    l2.config(text=f'{p2}',bg='#277BC0')
    l2.place(x=450,y=100)
    l3.config(text=f'{res}',bg='#E80F88')
    l3.place(x=300, y=150)

b1 = Button(root,text='PLAYER',command=player1,bg='#AF0171')
b1.place(x=70,y=50)
b2 = Button(root,text='COMPUTER',bg='#AF0171')
b2.place(x=500,y=50)

root.mainloop()
