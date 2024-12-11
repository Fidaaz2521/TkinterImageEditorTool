#1
import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import ttk
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageGrab


#2
root = tk.Tk()
root.geometry("1000x600")
root.title("Image Drawing Tool")
root.config(bg="white")

pen_color = "black"
pen_size = 5
file_path = ""


#@6
def add_image():
    global file_path
    file_path = filedialog.askopenfilename(
        initialdir="C:\tkinter image editor (P1)\pics")
    global image
    image = Image.open(file_path)
    canvas.config(width=image.width, height=image.height) 
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")




#@15

def save_canvas_as_image(canvas, shift_right, shift_down):
    # Get the window coordinates relative to the screen
    x0 = canvas.winfo_rootx()
    y0 = canvas.winfo_rooty()
    
    # Get the dimensions of the canvas
    canvas.update()  # Ensure the canvas is updated with any pending events
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    
    # Calculate the size of the bounding box (adjust as needed)
    capture_width = 750# Capture the entire width of the canvas
    capture_height = 600
    # Calculate the coordinates for the bounding box with shift towards right
    x1 = x0 + capture_width + shift_right
    y1 = y0 + capture_height + shift_down
    x0 = x0 + shift_right
    y0 = y0 + shift_down
    
    
    
    # Ask user for file to save
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("All Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
    
    if file_path:
        # Capture the canvas content as an image
        image = ImageGrab.grab(bbox=(x0, y0, x1, y1))
        
        
    
        # Determine file extension based on file name
        file_extension = file_path.split(".")[-1].lower()
        
        # Save the image with the correct file extension
        image.save(file_path, file_extension.upper())
    
#@7
def draw(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')

#@8
def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]

#@10
def change_size(size):
    global pen_size
    pen_size = size
    
#@11
def clear_canvas():
    canvas.delete("all")
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")


#@13
def apply_filter(filter):
    image = Image.open(file_path)
   
    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")
    return image 
   
 
   
    
#@14
def clr_fltr():
    image = Image.open(file_path)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")
    

#4
left_frame = tk.Frame(root, width=200, height=600, bg="light Blue")
left_frame.pack(side="left", fill="y")

#5
canvas = tk.Canvas(root, width=750, height=600)
canvas.pack()

#6
image_button = tk.Button(left_frame, text="Add Image",command=add_image, bg="light Blue")
image_button.pack(pady=15)


#8
color_button = tk.Button(left_frame, text="Change Pen Color", command=change_color, bg="light Blue")
color_button.pack(pady=5)

#9
pen_size_frame = tk.Frame(left_frame, bg="white")
pen_size_frame.pack(pady=5)

#10
pen_size_1 = tk.Radiobutton(pen_size_frame, text="Small", value=3, command=lambda: change_size(3), bg="light Blue")
pen_size_1.pack(side="left")

pen_size_2 = tk.Radiobutton(pen_size_frame, text="Medium", value=5, command=lambda: change_size(5), bg="light Blue")
pen_size_2.pack(side="left")
pen_size_2.select()#to make it a default size

pen_size_3 = tk.Radiobutton(pen_size_frame, text="Large", value=7, command=lambda: change_size(7), bg="light Blue")
pen_size_3.pack(side="left")


#11
clear_button = tk.Button(left_frame, text="Clear",command=clear_canvas, bg="pink")
clear_button.pack(pady=10)


#12
filter_label = tk.Label(left_frame, text="Select Filter", bg="light Blue")
filter_label.pack()
filter_combobox = ttk.Combobox(left_frame, values=["Black and White", "Blur","Emboss", "Sharpen", "Smooth"])
filter_combobox.pack()

#13
filter_combobox.bind("<<ComboboxSelected>>",lambda event: apply_filter(filter_combobox.get()))

#14
clr_filter_btn = tk.Button(left_frame, text=" Clear Filter", command=clr_fltr, bg="pink")
clr_filter_btn.pack(pady=10)



#15
savelabel = tk.Label(left_frame, text="Click Below To Save Your Filtered Image ", bg="light Blue")
savelabel.pack()



def save_image():
    save_canvas_as_image(canvas, shift_right=100, shift_down=40)
    
# Create a button to trigger saving the image
save_button = tk.Button(left_frame, text="Save Image", command=save_image, bg = "pink")
save_button.pack(pady=10)

#7
canvas.bind("<B1-Motion>", draw)


#3
root.mainloop()