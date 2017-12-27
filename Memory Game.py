from tkinter import *
import tkinter.messagebox as box
import time
import random

window = Tk()
window.title('Memory Game')
window.resizable(width= False, height = False)

file = open('words.txt', 'r')
lines = file.readlines()
file.close()

def quit():
    window.destroy()
    window.quit()

def easy():
    global remaining
    remaining = 3

    easy.destroy()
    hard.destroy()
    info.destroy()
    
    set1 = random.sample(range(0,10),9)
    a1,a2,a3,a4,a5,a6,a7,a8,a9 = set1
     
    one = lines[a1]    
    two = lines[a2]    
    three = lines[a3]    
    four = lines[a4]    
    five = lines[a5]    
    six = lines[a6]    
    seven = lines[a7]
    eight = lines[a8]
    nine = lines[a9]

    timer = Label(text = 'You have 30 seconds!')
    timer.configure(bg = 'yellow')
    label1 = Label(text = one)
    label2 = Label(text = two)
    label3 = Label(text = three)
    label4 = Label(text = four)
    label5 = Label(text = five)
    label6 = Label(text = six)
    label7 = Label(text = seven)
    label8 = Label(text = eight)
    label9 = Label(text = nine)
    label1.grid(row = 2, column = 1, pady = 5, padx = 2)
    label2.grid(row = 2, column = 2, pady = 5, padx = 2)
    label3.grid(row = 2, column = 3, pady = 5, padx = 2)
    label4.grid(row = 3, column = 1, pady = 5, padx = 2)
    label5.grid(row = 3, column = 2, pady = 5, padx = 2)
    label6.grid(row = 3, column = 3, pady = 5, padx = 2)
    label7.grid(row = 4, column = 1, pady = 5, padx = 2)
    label8.grid(row = 4, column = 2, pady = 5, padx = 2)
    label9.grid(row = 4, column = 3, pady = 5, padx = 2)
    timer.grid(row = 5, column = 1, pady = 5, padx = 5, columnspan = 3)
    window.update()
    
    i = 30    #Should equal 30
    
    while i > 0:
        timer.configure(text = i)
        i = i - 1
        if i < 5:
            timer.configure(bg = 'red')
        else:
            timer.configure(bg = 'yellow')
        time.sleep(1)
        window.update()

    timer.destroy()
    
    SetProblem = True
    while SetProblem == True:
        try:
            set2 = random.sample(range(0,10),9)  
            change = list(set(set1) - set(set2))
            #print (change)
            value = change[0]
            SetProblem = False
        except IndexError:
            SetProblem= True
    b1,b2,b3,b4,b5,b6,b7,b8,b9 = set2
    one = lines[b1]    
    two = lines[b2]    
    three = lines[b3]    
    four = lines[b4]    
    five = lines[b5]    
    six = lines[b6]    
    seven = lines[b7]
    eight = lines[b8]
    nine = lines[b9]

    word = lines[value]
    word = word.strip('\n')
    
    def enter():
        entry = str(answer.get())
        entry = entry.upper()
        if entry != word:
            global remaining
            remaining = remaining - 1
            box.showwarning('Incorrect', 'You have ' + str(remaining) + ' turn(s) remaining!')
            if remaining > 0:
                turns.configure(text = 'Turns: ' + str(remaining))
            if remaining == 0:
                turns.configure(text = 'Turns: ' + str(remaining))
                enter.configure(state = DISABLED)
                box.showwarning('Game Over!', 'You have had all of your turns!')
                window.destroy()
                window.quit()
                
        else:
            box.showinfo('Well Done!', 'You completed the easy game')
            window.destroy()
            window.quit()
               
    answer = Entry(window)
    enter = Button(text = 'Enter', command = enter)
    turns = Label(text = 'Turns: ' + str(remaining), bg = 'yellow')
    label1.configure(text = one)
    label2.configure(text = two)
    label3.configure(text = three)
    label4.configure(text = four)
    label5.configure(text = five)
    label6.configure(text = six)
    label7.configure(text = seven)
    label8.configure(text = eight)
    label9.configure(text = nine)
    turns.grid(row = 1 , column = 1, padx = 5, pady = 5)
    answer.grid(row = 5, column = 1, columnspan = 3, padx = 5,  pady = 5)
    enter.grid(row = 6, column = 2, pady = 5)
    window.update()

def hard():
    global remaining
    remaining = 3
    
    hard.destroy()
    easy.destroy()
    info.destroy()
    set1 = random.sample(range(0, 17),16)
    a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16 = set1

    one = lines[a1]
    two = lines[a2]
    three = lines[a3]
    four = lines[a4]
    five = lines[a5]
    six = lines[a6]
    seven = lines[a7]
    eight = lines[a8]
    nine = lines[a9]
    ten = lines[a10]
    eleven = lines[a11]
    twelve = lines[a12]
    thirteen = lines[a13]
    fourteen = lines[a14]
    fifteen = lines[a15]
    sixteen = lines[a16]

    timer = Label(text = 'You have 45 seconds!')
    timer.configure(bg = 'orange')
    exit.grid(row = 1, column = 4, pady = 5)
    label1 = Label(text = one)
    label2 = Label(text = two)
    label3 = Label(text = three)
    label4 = Label(text = four)
    label5 = Label(text = five)
    label6 = Label(text = six)
    label7 = Label(text = seven)
    label8 = Label(text = eight)
    label9 = Label(text = nine)
    label10 = Label(text = ten)
    label11 = Label(text = eleven)
    label12 = Label(text = twelve)
    label13 = Label(text = thirteen)
    label14 = Label(text = fourteen)
    label15 = Label(text = fifteen)
    label16 = Label(text = sixteen)
    label1.grid(row = 2, column = 1, padx = 5, pady = 2)
    label2.grid(row = 2, column = 2, padx = 5, pady = 2)
    label3.grid(row = 2, column = 3, padx = 5, pady = 2)
    label4.grid(row = 2, column = 4, padx = 5, pady = 2)
    label5.grid(row = 3, column = 1, padx = 5, pady = 2)
    label6.grid(row = 3, column = 2, padx = 5, pady = 2)
    label7.grid(row = 3, column = 3, padx = 5, pady = 2)
    label8.grid(row = 3, column = 4, padx = 5, pady = 2)
    label9.grid(row = 4, column = 1, padx = 5, pady = 2)
    label10.grid(row = 4, column = 2, padx = 5, pady = 2)
    label11.grid(row = 4, column = 3, padx = 5, pady = 2)
    label12.grid(row = 4, column = 4, padx = 5, pady = 2)
    label13.grid(row = 5, column = 1, padx = 5, pady = 2)
    label14.grid(row = 5, column = 2, padx = 5, pady = 2)
    label15.grid(row = 5, column = 3, padx = 5, pady = 2)
    label16.grid(row = 5, column = 4, padx = 5, pady = 2)
    timer.grid(row = 6, column = 1, columnspan = 4, padx = 5, pady = 5)
    window.update()

    i = 45    #Should equal 45!

    while i > 0:
        timer.configure(text = i)
        i = i - 1
        if i < 5:
            timer.configure(bg = 'red')
        else:
            timer.configure(bg = 'orange')
        time.sleep(1)
        window.update()

    timer.destroy()

    SetProblem = True
    while SetProblem == True:
        try:
            set2 = random.sample(range(0,17),16)  
            change = list(set(set1) - set(set2))
            #print (change)
            value = change[0]
            SetProblem = False
        except IndexError:
            SetProblem= True

    b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16 = set2

    one = lines[b1]
    two = lines[b2]
    three = lines[b3]
    four = lines[b4]
    five = lines[b5]
    six = lines[b6]
    seven = lines[b7]
    eight = lines[b8]
    nine = lines[b9]
    ten = lines[b10]
    eleven = lines[b11]
    twelve = lines[b12]
    thirteen = lines[b13]
    fourteen = lines[b14]
    fifteen = lines[b15]
    sixteen = lines[b16]

    word = lines[value]
    word = word.strip('\n')

    def enter():
        entry = str(answer.get())
        entry = entry.upper()
        if entry != word:
            global remaining
            remaining = remaining - 1
            box.showwarning('Incorrect', 'You have ' + str(remaining) + ' turn(s) remaining!')
            if remaining > 0:
                turns.configure(text = 'Turns: ' + str(remaining))
            if remaining == 0:
                turns.configure(text = 'Turns: ' + str(remaining))
                enter.configure(state = DISABLED)
                box.showwarning('Game Over!', 'You have had all of your turns!')
                window.destroy()
                window.quit()
                
        else:
            box.showinfo('Well Done!', 'You completed the hard game')
            window.destroy()
            window.quit()

    answer = Entry(window)
    enter = Button(text = 'Enter', command = enter)
    turns = Label(text = 'Turns: ' + str(remaining), bg = 'orange')
    label1.configure(text = one)
    label2.configure(text = two)
    label3.configure(text = three)
    label4.configure(text = four)
    label5.configure(text = five)
    label6.configure(text = six)
    label7.configure(text = seven)
    label8.configure(text = eight)
    label9.configure(text = nine)
    label10.configure(text = ten)
    label11.configure(text = eleven)
    label12.configure(text = twelve)
    label13.configure(text = thirteen)
    label14.configure(text = fourteen)
    label15.configure(text = fifteen)
    label16.configure(text = sixteen)
    turns.grid(row = 1 , column = 1, padx = 5, pady = 5)
    answer.grid(row = 6, column = 1, columnspan = 4, padx = 5, pady = 5)
    enter.grid(row = 7, column = 2, columnspan = 2, pady = 5)
    window.update()
    
    
exit = Button(text = 'Exit', command = quit)
easy = Button(text = 'Easy', command = easy)
hard = Button(text = 'Hard', command = hard)
info = Label(text = 'Python Memory Game: Select either\n the hard mode or the easy mode\n to play remember the words\n and when the words change\n type in the missing word.')
easy.grid(row = 1, column = 1, pady = 5)
hard.grid(row = 1, column = 2, pady = 5)
exit.grid(row = 1, column = 3, pady = 5)
info.grid(row = 2, column = 1, pady = 5, columnspan = 3)

window.mainloop()
