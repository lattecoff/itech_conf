import tkinter as tk

from Person import *
from Member import *


win = tk.Tk()
win.geometry("640x380")
win.title("Form members")


# lbl_name = tk.Label(win, text="Name", padx=20, pady=10).grid(row=0, column=0, stick="w")
# lbl_second_name = tk.Label(win, text="Second Name", padx=20, pady=10).grid(row=1, column=0, stick="w")
# lbl_birthday = tk.Label(win, text="Birthday", padx=20, pady=10).grid(row=2, column=0, stick="w")
# lbl_organization = tk.Label(win, text="Organization", padx=20, pady=10).grid(row=3, column=0, stick="w")
# lbl_position = tk.Label(win, text="Position", padx=20, pady=10).grid(row=4, column=0, stick="w")

# name = tk.Entry(win).grid(row=0, column=1, stick="w")
# second_name = tk.Entry(win).grid(row=1, column=1, stick="w")
# birthday = tk.Entry(win).grid(row=2, column=1, stick="w")
# organization = tk.Entry(win).grid(row=3, column=1, stick="w")
# position = tk.Entry(win).grid(row=4, column=1, stick="w")


lbl_name = tk.Label(win, text="Name", padx=20, pady=10).grid(row=0, column=0, stick="w")
lbl_second_name = tk.Label(win, text="Second name", padx=20, pady=10).grid(row=1, column=0, stick="w")
lbl_birthday = tk.Label(win, text="Birthday", padx=20, pady=10).grid(row=2, column=0, stick="w")
lbl_country = tk.Label(win, text="Country", padx=20, pady=10).grid(row=3, column=0, stick="w")
lbl_city = tk.Label(win, text="City", padx=20, pady=10).grid(row=4, column=0, stick="w")
lbl_address = tk.Label(win, text="Address", padx=20, pady=10).grid(row=5, column=0, stick="w")
lbl_phone = tk.Label(win, text="Phone", padx=20, pady=10).grid(row=6, column=0, stick="w")
lbl_email = tk.Label(win, text="Email", padx=20, pady=10).grid(row=7, column=0, stick="w")

# id = 
name = tk.Entry(win).grid(row=0, column=1, stick="w")
second_name = tk.Entry(win).grid(row=1, column=1, stick="w")
birthday = tk.Entry(win).grid(row=2, column=1, stick="w")
country = tk.Entry(win).grid(row=3, column=1, stick="w")
city = tk.Entry(win).grid(row=4, column=1, stick="w")
address = tk.Entry(win).grid(row=5, column=1, stick="w")
phone = tk.Entry(win).grid(row=6, column=1, stick="w")
email = tk.Entry(win).grid(row=7, column=1, stick="w")



win.mainloop()


