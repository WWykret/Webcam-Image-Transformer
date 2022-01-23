import tkinter as tk
import cv2
from PIL import Image, ImageTk

class App:
    def __init__(self, title: str, framerate: int):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title('camera converter')

        self.setupUI()
        
        self.framerate = framerate
        self.vc = cv2.VideoCapture(0)
        self.read_cam_input()

        self.root.mainloop()

    def foo(self):
        pass

    def read_cam_input(self):
        if self.vc.isOpened():
            _, frame = self.vc.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cam_frame = Image.fromarray(frame)
        else:
            cam_frame = Image.open('loading.png')

        new_cam_img = ImageTk.PhotoImage(cam_frame)
        self.cam_img_label.configure(image=new_cam_img)
        self.cam_img_label.image = new_cam_img

        self.root.after(1000 // self.framerate, self.read_cam_input)

    def setupUI(self):
        self.canvas = tk.Canvas(self.root)
        self.canvas.grid(columnspan=2, padx = 10, pady = 10)

        cam_img = ImageTk.PhotoImage(Image.open('loading.png'))
        self.cam_img_label = tk.Label(self.root, image=cam_img)
        self.cam_img_label.image = cam_img
        self.cam_img_label.grid(columnspan=2, column = 0, row = 0)

        self.flipXChBox = tk.IntVar()
        self.flipYChBox = tk.IntVar()
        self.showEdgesChBox = tk.IntVar()
        self.makeNegativeChBox = tk.IntVar()

        self.transformBox1 = tk.Checkbutton(self.root, text='Filp vertically', variable=self.flipXChBox, onvalue=1, offvalue=0, command=self.foo)
        self.transformBox1.grid(column=0, row = 1, sticky = 'w')

        self.transformBox2 = tk.Checkbutton(self.root, text='Filp horizontaly', variable=self.flipYChBox, onvalue=1, offvalue=0, command=self.foo)
        self.transformBox2.grid(column=1, row = 1, sticky = 'w')

        self.transformBox3 = tk.Checkbutton(self.root, text='Show edges', variable=self.showEdgesChBox, onvalue=1, offvalue=0, command=self.foo)
        self.transformBox3.grid(column=0, row = 2, sticky = 'w')

        self.transformBox4 = tk.Checkbutton(self.root, text='Invert colors', variable=self.makeNegativeChBox, onvalue=1, offvalue=0, command=self.foo)
        self.transformBox4.grid(column=1, row = 2, sticky = 'w')

        self.saveBtn = tk.Button(self.root, text='Save image', command=self.foo)
        self.saveBtn.grid(column=0, row=3, sticky = 'nesw')

        self.applyBtn = tk.Button(self.root, text='Apply filters', command=self.foo)
        self.applyBtn.grid(column=1, row=3, sticky = 'nesw')