from tkinter import *
from tkinter import messagebox
from math import sqrt

def discriminant(a,b,c):
    return b**2-4*a*c

def rewenie():
    is_valid=True
    for entry in [entry_a,entry_b,entry_c]:
        if entry.get():
            entry.config(bg='lightblue')
        else:
            entry.config(bg='red')
            is_valid=False
    if is_valid:
        try:
            a=float(entry_a.get())
            b=float(entry_b.get())
            c=float(entry_c.get())
            D=discriminant(a,b,c)
            solution_text.config(text=f'Дискриминант (D) = {D:.2f}\n')
            if D>0:
                x1=(-b+sqrt(D))/(2*a)
                x2=(-b-sqrt(D))/(2*a)
                solution_text.config(text=(solution_text['text']+f'Уравнение имеет два корня:\nx1 = {x1:.2f}\nx2 = {x2:.2f}'))
            elif D==0:
                x1=-b/(2*a)
                solution_text.config(text=(solution_text['text']+f'Уравнение имеет один корень:\nx = {x1:.2f}'))
            else:
                solution_text.config(text=(solution_text['text']+'Уравнение не имеет действительных корней.'))
        except ValueError:
            messagebox.showerror('Ошибка', 'Введите числа!')
            solution_text.config(text='')

root=Tk()
root.geometry('600x300')
root.title('Квадратные уравнения')

title_frame=Frame(root,bg='lightblue',height=50)
title_frame.pack(padx=10,pady=10,fill='x',expand=True)
title_label=Label(title_frame,text='Решение квадратного уравнения',bg='lightblue',font="Candara 16")
title_label.pack(side='top',fill='x')

entry_a=Entry(root,width=5,font="Candara 16",bg='lightblue')
entry_a.place(x=20,y=100,width=120, height=30)
entry_b=Entry(root,width=5,font="Candara 16",bg='lightblue')
entry_b.place(x=220, y=100, width=120, height=30)
entry_c=Entry(root,width=5,font="Candara 16",bg='lightblue')
entry_c.place(x=420,y=100,width=120,height=30)

label_a=Label(root,text="x² +",bg='white',font="Candara 16")
label_a.place(x=150,y=100)
label_b=Label(root,text="x +",bg='white',font="Candara 16")
label_b.place(x=350, y=100)
label_c=Label(root,text="= 0",bg='white',font="Candara 16")
label_c.place(x=550,y=100)

rewenie_button=Button(root,text="Решить",command=rewenie,bg='green',font="Candara 16")
rewenie_button.place(x=480,y=150,width=100,height=40)

solution_frame=Frame(root,bg='yellow',height=50)
solution_frame.pack(padx=20,pady=10,fill='x',expand=True)
solution_title=Label(solution_frame,text='Решение',bg='yellow',font="Candara 12")
solution_title.pack(side='top',fill='x')
solution_text=Label(solution_frame,text='',bg='yellow',font="Candara 12",anchor='w')
solution_text.pack(side='bottom',fill='x')

root.mainloop()