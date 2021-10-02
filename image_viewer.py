# imported everthing from tkinter
from tkinter import *
# imported messagebox from tkinter
from tkinter import messagebox
# imported font from tkinter
import tkinter.font as font
# imported os for getting path and image names
import os
# imported PIL to view jpeg images
from PIL import ImageTk, Image

# function to delete image from os
def delete_from_os():
	global path
	global images_in_path
	# used os remove to delete the image
	os.remove(path + images_in_path[7])

# function to display warning message and call delete_from_os is chose to delete 
def delete_command():
	# created a variable to store answer 
	selected_option = messagebox.askyesno('Delete?', 'Are you sure?')
	# if answer is yes
	if selected_option == True:
		# called delete from os function
		delete_from_os()
		# display message that the file is deleted
		messagebox.showinfo('Done', 'Successfully deleted')

		# call next button so that the viewer will show next image directly after deleting the current

# created the window 
root = Tk()
# changed background color to grey
root.configure(bg='grey')

# created the top frame for displaying images
image_frame = Frame(root, borderwidth=8, relief='solid', width=1700, height=800)
image_frame.grid(row=0, column=0, padx=70, pady=15, ipadx=30, ipady=25)

# created the bottom frame for displying the button
button_frame = Frame(root, borderwidth=7, relief='solid', width=600, height=60, bg='light cyan')
button_frame.grid(row=1, column=0, padx=100, pady=5)

# added title to the window
root.title('Image Viewer')

# used geometry to display window in fixed size and position on desktop
# format is geometry(width x height+space from left+spcae from up)
# root.geometry('1280x1024+500+200')

# commnd to open window maximized 
root.state('zoomed')


# fetched current path using os 
path = os.getcwd()
# printed just for checking
print('Path: ', path)

# fetched files in current path
files_in_path = list(os.listdir(path))
# printed just for checking
print('Files in path', files_in_path)

# created empty list to store images in path
images_in_path = []

# iterated in the files and searched for image formats, if image found the appended to images_in_path 
for images in files_in_path:
	if 'jpg' in images or 'png' in images or 'jpeg' in images:
		# prepended(adding at beginning) \\ with the image name
		images_in_path.append('\\'+images)
# printed just for checking
print('Images in path', images_in_path)

# loaded the image from the list 
image = Image.open(path + images_in_path[4])
# resized image to fit the window
image = image.resize((1700, 800), Image.ANTIALIAS)
# converted to photoimage
photo = ImageTk.PhotoImage(image)

# label to display the image 
# width and height decides the width and height of the label and borderwidth creates a border, relief makes the border solid
image_label = Label(root, image=photo,width=1700, height=800, relief='solid')
# displayed label on window
image_label.grid(row=0, column=0, columnspan=3)

# buttons
# previous button
previous_button = Button(button_frame, text='<',width=3, height=1, borderwidth=3, relief='solid', activebackground='RoyalBlue1',activeforeground='black')
# defined font style
format_font_previous_button = font.Font(size=20)
# applied font style to button
previous_button['font'] = format_font_previous_button
# displayed the previous button
previous_button.grid(row=0, column=0, padx=50, pady=10, ipadx=5, ipady=5)

# delete button
delete_button = Button(button_frame, text='X',width=3, height=1, borderwidth=3, relief='solid', activebackground='red',activeforeground='black', command=delete_command)
# defined font style
format_font_delete_button = font.Font(size=20)
# applied font style to button
delete_button['font'] = format_font_previous_button
# displayed the delete button
delete_button.grid(row=0, column=1, padx=50, pady=10, ipadx=5, ipady=5)

# next button
next_button = Button(button_frame, text='>',width=3, height=1, borderwidth=3, relief='solid', activebackground='RoyalBlue1',activeforeground='black')
# defined font style
format_font_next_button = font.Font(size=20)
# applied font style to button
next_button['font'] = format_font_previous_button
# displayed the next button
next_button.grid(row=0, column=2, padx=50, pady=10, ipadx=5, ipady=5)








# displaying the window
root.mainloop()
