from tkinter import *  
  
top = Tk()  
top.geometry("720x480")  
frame = Frame(top, borderwidth=5, relief='solid')  
frame.pack()  
  
topframe = Frame(top, borderwidth=5, relief='solid', padx=300, pady=150)  
topframe.pack(side = TOP)  
  
bottomframe = Frame(top, borderwidth=5, relief='solid', padx=300, pady=50)  
bottomframe.pack(side = BOTTOM)  

  
  
button_left = Button(bottomframe, text="buttons", fg="blue", activebackground = "blue")  
button_left.pack(side = LEFT ) 

button_right = Button(bottomframe, text="buttons", fg="blue", activebackground = "blue")  
button_right.pack(side = RIGHT ) 
  
image_panel = Button(topframe, text="image", fg="black", activebackground = "white")  
image_panel.pack(side = TOP)  
  
top.mainloop()
