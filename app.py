import io
import pickle
import tkinter as tk

import numpy as np
from PIL import Image


class DigitRecognitionApp:
    
    def __init__(self):

        self.root = tk.Tk()
        self.root.title('Digit Recognition')

        self.canvas = tk.Canvas(self.root, width=300, height=300, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.handle_clear)
        self.clear_button.pack()

        self.execute_recognizing_function_button = tk.Button(self.root, text='Recognize',
                                                             command=self.recognize)
        self.execute_recognizing_function_button.pack()

        self.save_button = tk.Button(self.root, text='Save', command=self.save_drawing)
        self.save_button.pack()

        self.info_label = tk.Label(self.root, text="Draw a digit")
        self.info_label.pack()

        self.text_variable = tk.StringVar()
        self.result_label = tk.Label(self.root, textvariable=self.text_variable)
        self.result_label.pack()

        self.root.mainloop()

    def start_drawing(self, event):
        self.canvas.x = event.x
        self.canvas.y = event.y

    def draw(self, event):
        self.canvas.create_line(self.canvas.x, self.canvas.y, event.x, event.y, width=5)
        self.canvas.x = event.x
        self.canvas.y = event.y

    def get_image(self):
        ps_data = self.canvas.postscript(colormode='gray')
        img = Image.open(io.BytesIO(ps_data.encode('utf-8')))
        return img

    def handle_clear(self):
        self.canvas.delete('all')

    def recognize(self):
        img = self.get_image()
        model = pickle.load(open('svm_model.pkl', 'rb'))
        img = img.resize((8, 8))
        img = img.convert('L')
        img_array = np.array(img)
        img_vector = img_array.flatten()
        img_vector = img_vector.reshape(1, -1)
        prediction = model.predict(img_vector)
        self.text_variable.set(str(prediction)[0])

    def save_drawing(self):
        image = self.get_image()
        image.save("drawing.png", "PNG")


app = DigitRecognitionApp()
