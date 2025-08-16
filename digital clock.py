import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%I:%M:%S %p')  
    label.config(text=string)  
    label.after(1000, time) 

label = tk.Label(root, font=('calibri', 50, 'bold'), background='red', foreground='black')  
label.pack(anchor='center')  
time()  
root.mainloop()

