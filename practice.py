from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Интерфейс для массива")
root.geometry("350x190")

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx =.5, rely=.1, anchor="c")

def numbers():
	mass_1 = []
	volley = message.get()
	volley2 = int(volley)
	zero = 0
	for volley in range(volley2):
		if volley % 2:
			mass_1.insert(0, volley)
	for zero in range(volley2):
		if zero % 2:
			zero = zero * 0
			mass_1.append(zero)

	messagebox.showinfo("Python GUI", mass_1)

message_button = Button(text="Input Number", command = numbers)
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()