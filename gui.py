import tkinter as tk
from main import load_model_from_file


def start_drawing(event):
    canvas.x = event.x
    canvas.y = event.y


def draw(event):
    canvas.create_line(canvas.x, canvas.y, event.x, event.y, width=5)
    canvas.x = event.x
    canvas.y = event.y


def handle_clear():
    canvas.delete('all')


root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

canvas.bind("<Button-1>", start_drawing)  # Rozpoczęcie rysowania po naciśnięciu lewego przycisku myszy
canvas.bind("<B1-Motion>", draw)  # Rysowanie przy poruszaniu myszą z wciśniętym lewym przyciskiem

clear_button = tk.Button(root, text="Clear", command=handle_clear)
clear_button.pack()

execute_recognizing_function_button = tk.Button(root, text='Recognizing', command=lambda: load_model_from_file())
execute_recognizing_function_button.pack()

info_label = tk.Label(root, text="Draw a digit")
info_label.pack()

result = load_model_from_file()

text_variable = tk.StringVar()
text_variable.set(result)

entry = tk.Entry(root, textvariable=text_variable)
entry.pack()

root.title('Number')

root.mainloop()
