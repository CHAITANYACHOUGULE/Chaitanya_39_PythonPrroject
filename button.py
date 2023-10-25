import tkinter as tk 
r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, text='Stop', width=15, command=r.destroy,activeforeground='blue',activebackground='orange') 

button.pack() 
r.mainloop() 
