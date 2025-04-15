from tkinter import *
def button(num):
    global equation_text
    equation_text=equation_text+str(num)
    equation_label.set(equation_text)
 
 
def equls():
    
    global equation_text
    try:
        total=str(eval(equation_text))
        equation_label.set(total)
        equation_text=total
    except ZeroDivisionError:
        equation_label.set(' division by zero')
        equation_text=''
    except SyntaxError:
        equation_label.set(' SyntaxError')
        equation_text=''

        

def clear():
    global equation_text
    equation_label.set('') 
    equation_text=''

windos=Tk()
windos.title('CALCULATOR')
windos.geometry('500x500')
equation_text=''

equation_label=StringVar()

label=Label(windos,textvariable=equation_label,font=('consolas',21),bg='white',width=24,height=2)
label.pack()


frame=Frame(windos)
frame.pack()

button1=Button(frame,text=1,height=2,width=6,font=('Arial',18),command=lambda:button(1),bg='white')
button1.grid(row=0,column=0)

button2=Button(frame,text=2,height=2,width=6,font=('Arial',18),command=lambda:button(2),bg='white')
button2.grid(row=0,column=1)

button3=Button(frame,text=3,height=2,width=6,font=('Arial',18),command=lambda:button(3),bg='white')
button3.grid(row=0,column=2)

button4=Button(frame,text=4,height=2,width=6,font=('Arial',18),command=lambda:button(4),bg='white')
button4.grid(row=1,column=0)

button5=Button(frame,text=5,height=2,width=6,font=('Arial',18),command=lambda:button(5),bg='white')
button5.grid(row=1,column=1)

button6=Button(frame,text=6,height=2,width=6,font=('Arial',18),command=lambda:button(6),bg='white')
button6.grid(row=1,column=2)

button7=Button(frame,text=7,height=2,width=6,font=('Arial',18),command=lambda:button(7),bg='white')
button7.grid(row=2,column=0)

button8=Button(frame,text=8,height=2,width=6,font=('Arial',18),command=lambda:button(8),bg='white')
button8.grid(row=2,column=1)

button9=Button(frame,text=9,height=2,width=6,font=('Arial',18),command=lambda:button(9),bg='white')
button9.grid(row=2,column=2)

button0=Button(frame,text=0,height=2,width=6,font=('Arial',18),command=lambda:button(0),bg='white')
button0.grid(row=3,column=0)

dot=Button(frame,text='.',height=2,width=6,font=('Arial',18),command=lambda:button('.'),bg='white')
dot.grid(row=3,column=1)

equal=Button(frame,text='=',height=2,width=6,font=('Arial',18),command=equls)
equal.grid(row=3,column=2)

plus=Button(frame,text='+',height=2,width=6,font=('Arial',18),command=lambda:button('+'),bg='white')
plus.grid(row=0,column=3)

min=Button(frame,text='-',height=2,width=6,font=('Arial',18),command=lambda:button('-'),bg='white')
min.grid(row=1,column=3)

multi=Button(frame,text='*',height=2,width=6,font=('Arial',18),command=lambda:button('*'),bg='white')
multi.grid(row=2,column=3)

taghsim=Button(frame,text='/',height=2,width=6,font=('Arial',18),command=lambda:button('/'),bg='white')
taghsim.grid(row=3,column=3)

clearb=Button(text='clear',height=2,width=9,font=('Arial',18),command=clear,bg='white')
clearb.pack()

windos.mainloop()

