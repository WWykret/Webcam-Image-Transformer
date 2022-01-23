import tkinter as tk
from PIL import ImageTk
from camera import Camera
from imageTransformers import IImageTransformer, ImageTransformerBuilder
import os.path

class App:
    def __init__(self, title: str, webcam: Camera, default_image_transformer: IImageTransformer):
        self.webcam = webcam
        self.img_transformer = default_image_transformer

        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title(title)

        self.setupUI()

        self.update_img()

        self.root.mainloop()

    def apply_transformations(self):
        new_transformation_builder = ImageTransformerBuilder()
        
        if self.flipXChBox.get() == 1:
            new_transformation_builder.flip_on_axis('y')
        if self.flipYChBox.get() == 1:
            new_transformation_builder.flip_on_axis('x')
        if self.showEdgesChBox.get() == 1:
            new_transformation_builder.detect_edges()
        if self.makeNegativeChBox.get() == 1:
            new_transformation_builder.negate_image()

        self.img_transformer = new_transformation_builder.build()

    def save_image(self):
        counter = 0
        
        while os.path.isfile(f'images/camera_saved_{counter}.jpg'):
            counter += 1

        if not os.path.isdir('images'):
            os.mkdir('images')
        
        self.webcam.get_camera_frame(self.img_transformer).save(f'images/camera_saved_{counter}.jpg')

    def update_img(self):
        new_cam_img = ImageTk.PhotoImage(self.webcam.get_camera_frame(self.img_transformer))
        self.cam_img_label.configure(image=new_cam_img)
        self.cam_img_label.image = new_cam_img

        self.root.after(1000 // self.webcam.get_framerate(), self.update_img)

    def setupUI(self):
        self.canvas = tk.Canvas(self.root)
        self.canvas.grid(columnspan=2, padx = 10, pady = 10)

        cam_img = ImageTk.PhotoImage(self.webcam.get_default_img(self.img_transformer))
        self.cam_img_label = tk.Label(self.root, image=cam_img)
        self.cam_img_label.image = cam_img
        self.cam_img_label.grid(columnspan=2, column = 0, row = 0)

        self.flipXChBox = tk.IntVar()
        self.flipYChBox = tk.IntVar()
        self.showEdgesChBox = tk.IntVar()
        self.makeNegativeChBox = tk.IntVar()

        self.transformBox1 = tk.Checkbutton(self.root, text='Filp vertically', variable=self.flipXChBox, onvalue=1, offvalue=0)
        self.transformBox1.grid(column=0, row = 1, sticky = 'w')

        self.transformBox2 = tk.Checkbutton(self.root, text='Filp horizontaly', variable=self.flipYChBox, onvalue=1, offvalue=0)
        self.transformBox2.grid(column=1, row = 1, sticky = 'w')

        self.transformBox3 = tk.Checkbutton(self.root, text='Show edges', variable=self.showEdgesChBox, onvalue=1, offvalue=0)
        self.transformBox3.grid(column=0, row = 2, sticky = 'w')

        self.transformBox4 = tk.Checkbutton(self.root, text='Invert colors', variable=self.makeNegativeChBox, onvalue=1, offvalue=0)
        self.transformBox4.grid(column=1, row = 2, sticky = 'w')

        self.saveBtn = tk.Button(self.root, text='Save image', command=self.save_image)
        self.saveBtn.grid(column=0, row=3, sticky = 'nesw')

        self.applyBtn = tk.Button(self.root, text='Apply filters', command=self.apply_transformations)
        self.applyBtn.grid(column=1, row=3, sticky = 'nesw')