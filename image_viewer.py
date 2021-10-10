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

# function to read the directory and load images
def read_images():
	# fetched current path using os 
	global path 
	path = os.getcwd()
	# printed just for checking
	print('Path: ', path)
	
	# fetched files in current path
	files_in_path = list(os.listdir(path))
	# printed just for checking
	print('Files in path', files_in_path)
	
	# created empty list to store images in path
	global images_in_path
	images_in_path = []
	
	# iterated in the files and searched for image formats, if image found the appended to images_in_path 
	for images in files_in_path:
		if 'jpg' in images or 'png' in images or 'jpeg' in images:
			# prepended(adding at beginning) \\ with the image name
			images_in_path.append('\\'+images)
	# printed just for checking
	print('Images in path', images_in_path)
	print('Length of list images_in_path ', len(images_in_path))
	
	# printed for cheking the current image
	print('Current image path ', path + images_in_path[n])
	# loaded the image from the list
	image = Image.open(path + images_in_path[n])
	
	# resized image to fit the window
	image = image.resize((1700, 800), Image.ANTIALIAS)
	# converted to photoimage
	global photo
	photo = ImageTk.PhotoImage(image)

	# called function label_for_image to add the image to label and display in window
	label_for_image()
	
	
# function to create and display label
def label_for_image():
	# label to display the image 
	# width and height decides the width and height of the label and borderwidth creates a border, relief makes the border solid
	image_label = Label(root, image=photo,width=1700, height=800, relief='solid')
	# displayed label on window
	image_label.grid(row=0, column=0, columnspan=3)

	
# fucntion to show next image
def next_command():
	global n
	global images_in_path
	global image
	# incremented n by 1 to go to next image in list
	if n >= 0:
		n = n + 1

	# called read_images to read and display the image
	read_images()
	# printed for checking
	print('n = ', n)
	
	# added one extra to n as the index starts from 0
	n_plus_one = n + 1

	# if n or smaller than length of list containing the images then disable next button and enable back button
	if n_plus_one == len(images_in_path):
		next_button['state'] = 'disabled'
		previous_button['state'] = 'active' # trex for switching back forward
	# else enable both
	else:
	 	next_button['state'] = 'normal'
	 	previous_button['state'] = 'normal' # trex for switching back forward

	# if images_in_path[-1]:
	# 	next_button['state'] = 'disabled'
	# # else enabled
	# else:
	#  	next_button['state'] = 'normal'


# fucntion to show previous image
def back_command():
	global n
	global images_in_path
	global image
	# decrement n by 1 only when n is not equal to 0, to go to previous image in the list
	if n != 0:
		n = n - 1
	
	# called read_images to read and display the image
	read_images()
	# printed for checking 
	print('n = ', n)	

	# if n is 0 or smaller than 0 then disable the previous button keeping the next button enabled
	if n <= 0:
		previous_button['state'] = 'disabled'
		next_button['state'] = 'active' # trex for switching back forward
	# else if n is greater or equal to 1 then enable both
	elif n >= 1:
	 	previous_button['state'] = 'normal'
	 	next_button['state'] = 'normal' # trex for switching back forward

	# if images_in_path[0]:
	# 	previous_button['state'] = 'disabled'
	# # else keep enabled
	# else:
	#  	previous_button['state'] = 'normal'

# function to delete image from os
def delete_from_os():
	global path
	global images_in_path
	# used os remove to delete the image at nth index of the list
	os.remove(path + images_in_path[n])


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


# declared n as global and assigned 0
global n
n = 0
# called function read images to read and display images
read_images()



# buttons
# previous button
previous_button = Button(button_frame, text='<',width=3, height=1, borderwidth=3, relief='solid', activebackground='RoyalBlue1',activeforeground='black', command=back_command)
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
next_button = Button(button_frame, text='>',width=3, height=1, borderwidth=3, relief='solid', activebackground='RoyalBlue1',activeforeground='black', command=next_command)
# defined font style
format_font_next_button = font.Font(size=20)
# applied font style to button
next_button['font'] = format_font_previous_button
# displayed the next button
next_button.grid(row=0, column=2, padx=50, pady=10, ipadx=5, ipady=5)






# displaying the window
root.mainloop()
