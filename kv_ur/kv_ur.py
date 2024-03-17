import tkinter as tk
from tkinter import messagebox
from math import sqrt

# Function to calculate discriminant
def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

# Function called when 'Solve' button is pressed
def solve():
    # Validate the entries and change background color if necessary
    is_valid = True
    for entry in [entry_a, entry_b, entry_c]:
        if entry.get():
            entry.config(bg='lightblue')
        else:
            entry.config(bg='red')
            is_valid = False

    # If all entries are valid, calculate the solution
    if is_valid:
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            D = calculate_discriminant(a, b, c)

            # Output the discriminant
            solution_text.config(text=f'Дискриминант (D) = {D:.2f}\n')

            # Check the discriminant to determine the number and type of roots
            if D > 0:
                # Two real roots
                x1 = (-b + sqrt(D)) / (2*a)
                x2 = (-b - sqrt(D)) / (2*a)
                solution_text.config(text=(solution_text['text'] + f'Уравнение имеет два корня:\nx1 = {x1:.2f}\nx2 = {x2:.2f}'))
            elif D == 0:
                # One real root
                x1 = -b / (2*a)
                solution_text.config(text=(solution_text['text'] + f'Уравнение имеет один корень:\nx = {x1:.2f}'))
            else:
                # Complex roots
                solution_text.config(text=(solution_text['text'] + 'Уравнение не имеет действительных корней.'))

        except ValueError:
            messagebox.showerror('Error', 'Please enter valid numbers')
            solution_text.config(text='')

# Main window
root = tk.Tk()
root.geometry('600x300')
root.title('Квадратные уравнения')

# Frame for the title with lightblue background without a black border
title_frame = tk.Frame(root, bg='lightblue', height=50)
title_frame.pack(padx=10, pady=10, fill='x', expand=True)
title_label = tk.Label(title_frame, text='Решение квадратного уравнения', bg='lightblue', font=('Arial', 16))
title_label.pack(side='top', fill='x')

# Coefficient entry fields with lightblue background
entry_a = tk.Entry(root, width=5, font=('Arial', 16), bg='lightblue')
entry_a.place(x=20, y=100, width=120, height=30)
entry_b = tk.Entry(root, width=5, font=('Arial', 16), bg='lightblue')
entry_b.place(x=220, y=100, width=120, height=30)
entry_c = tk.Entry(root, width=5, font=('Arial', 16), bg='lightblue')
entry_c.place(x=420, y=100, width=120, height=30)

# Equation parts labels
label_a = tk.Label(root, text="x² +", bg='white', font=('Arial', 16))
label_a.place(x=150, y=100)
label_b = tk.Label(root, text="x +", bg='white', font=('Arial', 16))
label_b.place(x=350, y=100)
label_c = tk.Label(root, text="= 0", bg='white', font=('Arial', 16))
label_c.place(x=550, y=100)

# Solve button
solve_button = tk.Button(root, text="Решить", command=solve, bg='green', font=('Arial', 16))
solve_button.place(x=480, y=150, width=100, height=40)

# Solution label with "Решение" and formatted output
solution_frame = tk.Frame(root, bg='yellow', height=50)
solution_frame.pack(padx=20, pady=10, fill='x', expand=True)
solution_title = tk.Label(solution_frame, text='Решение', bg='yellow', font=('Arial', 12))
solution_title.pack(side='top', fill='x')
solution_text = tk.Label(solution_frame, text='', bg='yellow', font=('Arial', 12), anchor='w')
solution_text.pack(side='bottom', fill='x')

root.mainloop()