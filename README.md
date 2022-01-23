# Webcam Image Transformer

Simple application allowing capturing, transforming in real time and saving image from webcam.

## Table of contents
* [General info](#general-info)
* [Implementation ideas](#implementation-ideas)
* [Run](#run)
* [Technologies](#technologies)
* [Examples of program effects](#examples-of-program-effects)
* [Status](#status)

## General info

This program allows user to select a combination of up to for transformations
- symmetry about the x axis
- symmetry about the x axis
- edge detection
- color inversion

Selected transformations are then applied on the input from the camera in order for the user to be able to see the result in real time.

## Implementation ideas

My main goal was to create simple desktop app for modifying webcam input. With that in mind I wanted to learn working with GUI in python and practice some of the popular design patterns in this language.

I used tkinter checkboxes for user to check what transformations (if any) should be applied on the webcam image, however transformations are not applied until `apply` button is pressed.

## Run

If you don't have NumPy, Tkinter, OpenCV-Python or Pillow installed, use the command:
```bash
pip install numpy tk opencv-python pillow
```
To get started with my program, navigate to a directory where you want to use the project, then clone it with:
```bash
git clone 
```
If you don't want to use git clone for whatever reason, you can manually download it, and move the folder somewhere convenient. Then, open up your terminal, and go to the correct directory. Then just run the program:
```bash
python3 main.py
```

## Technologies

The program was written in Python using Tkinter for creating GUI, OpenCV-Python for capturing webcam input and Pillow for operations on images obtained from webcam.

## Examples of program effects

#### Example. 1 - No filters 
![example1](https://github.com/WWykret/Webcam-Image-Transformer/blob/main/examples/example1.jpg)

## Status

I consider this project to be finisned and will probably not work on it anymore.