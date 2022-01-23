import tkinter as tk
# from tkinter import *
# from tkinter import ttk
from PIL import Image, ImageTk

img = Image.open("wojak.gif").resize((400, 400))

def bar():
    pass

def bar2():
    pass

root = tk.Tk()

canvas = tk.Canvas(root, width = 400, height = 400)
canvas.grid(columnspan=2, padx = 10, pady = 10)

cam_img = ImageTk.PhotoImage(Image.open("wojak.gif").resize((400, 400)))
cam_img_label = tk.Label(image=cam_img)
cam_img_label.image = cam_img
cam_img_label.grid(columnspan=2, column = 0, row = 0)

def foo():
    pass

flipX = tk.IntVar()
flipY = tk.IntVar()
showEdges = tk.IntVar()
makeNegative = tk.IntVar()

transformBox1 = tk.Checkbutton(root, text="Filp vertically", variable=flipX, onvalue=1, offvalue=0, command=foo)
transformBox1.grid(column=0, row = 1, sticky = "w")

transformBox2 = tk.Checkbutton(root, text="Filp horizontaly", variable=flipY, onvalue=1, offvalue=0, command=foo)
transformBox2.grid(column=1, row = 1, sticky = "w")

transformBox3 = tk.Checkbutton(root, text="Show edges", variable=showEdges, onvalue=1, offvalue=0, command=foo)
transformBox3.grid(column=0, row = 2, sticky = "w")

transformBox4 = tk.Checkbutton(root, text="Invert colors", variable=makeNegative, onvalue=1, offvalue=0, command=foo)
transformBox4.grid(column=1, row = 2, sticky = "w")

saveBtn = tk.Button(root, text="Save image", command=bar)
saveBtn.grid(column=0, row=3, sticky = "nesw")

applyBtn = tk.Button(root, text="Apply filters", command=bar)
applyBtn.grid(column=1, row=3, sticky = "nesw")

root.mainloop()

# import cv2
# from PIL import Image

# cv2.namedWindow("preview")
# vc = cv2.VideoCapture(0)

# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False

# while rval:
#     cv2.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     if key == 27: # exit on ESC
#         break

# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# im_pil = Image.fromarray(frame)
# im_pil.rotate(45).show()

# vc.release()
# cv2.destroyWindow("preview")