from tkinter import *

root = Tk() 
frame = Frame(root) 
frame.pack() 
bottomframe = Frame(root) 
bottomframe.pack( side = BOTTOM ) 
redbutton = Button(frame, text = 'Bheem', fg ='red') 
redbutton.pack( side = LEFT) 
greenbutton = Button(frame, text = 'Raju', fg='brown') 
greenbutton.pack( side = LEFT ) 
bluebutton = Button(frame, text ='Chutaki', fg ='blue') 
bluebutton.pack( side = LEFT ) 
blackbutton = Button(bottomframe, text ='Kaliya', fg ='black') 
blackbutton.pack( side = BOTTOM) 
root.mainloop() 
