import tkinter as tk
import random

def create_random_shape(canvas_width, canvas_height):
    shape_type = random.choice(['square', 'circle', 'triangle'])
    x = random.randint(0, canvas_width)
    y = random.randint(0, canvas_height)
    size = random.randint(10, 50)
    if shape_type == 'square':
        shape = canvas.create_rectangle(x, y, x+size, y+size, fill='red')
    elif shape_type == 'circle':
        shape = canvas.create_oval(x, y, x+size, y+size, fill='blue')
    else:
        shape = canvas.create_polygon(x, y, x+size, y+size, x+size/2, y+size*3/4, fill='green')
    return shape

def generate_shape():
    canvas.delete('all')
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    shape = create_random_shape(canvas_width, canvas_height)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack(fill='both', expand=True)

button = tk.Button(root, text='Сгенерировать', command=generate_shape)
button.pack()

root.mainloop()
