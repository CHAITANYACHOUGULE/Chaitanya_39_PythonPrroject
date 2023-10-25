from tkinter import *
master = Tk(screenName='Student form',) 
Label(master, text='First Name',).grid(row=0) 
Label(master, text='Last Name').grid(row=1)

var1 = IntVar() 
Checkbutton(master, text='male', variable=var1).grid(row=2, sticky=W) 
var2 = IntVar() 
Checkbutton(master, text='female', variable=var2).grid(row=3, sticky=W)


Label(master, text='Department').grid(row=4)
Label(master, text='Unique id').grid(row=5)
Label(master, text='Division').grid(row=6)
Label(master, text='Roll no').grid(row=7)
Label(master, text='Batch').grid(row=8)


Label(master, text='gmail').grid(row=9) 
Label(master, text='mob').grid(row=10)
Label(master, text='address').grid(row=11)
 





e1 = Entry(master) 
e2 = Entry(master) 
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e10 = Entry(master)
e11= Entry(master)
e12= Entry(master)

e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)
e9.grid(row=8, column=1)
e10.grid(row=9, column=1)
e11.grid(row=10, column=1)
e12.grid(row=11, column=1)

 
mainloop() 
