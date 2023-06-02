import tkinter as tk

from Person import *
from Member import *

import sqlite3


win = tk.Tk()
win.geometry("640x780")
win.title("Form members")

"""
@brief Send form to database.
"""
def send_form():
	_name = person.name.get()
	_second_name = person.second_name.get()
	_birthday = person.birthday.get()
	_country = person.country.get()
	_city = person.city.get()
	_address = person.address.get()
	_phone = person.phone.get()
	_email = person.email.get()


	cur.execute('INSERT INTO data_members VALUES(?, ?, ?, ?, ?, ?, ?, ?)', (_name, _second_name, _birthday, _country, _city, _address, _phone, _email))
	base.commit() 




base = sqlite3.connect('conf.db')
cur = base.cursor()


lbl_name = tk.Label(win, text="Name", padx=20, pady=10).grid(row=0, column=0, sticky="w")
lbl_second_name = tk.Label(win, text="Second name", padx=20, pady=10).grid(row=1, column=0, sticky="w")
lbl_birthday = tk.Label(win, text="Birthday", padx=20, pady=10).grid(row=2, column=0, sticky="w")
lbl_country = tk.Label(win, text="Country", padx=20, pady=10).grid(row=3, column=0, sticky="w")
lbl_city = tk.Label(win, text="City", padx=20, pady=10).grid(row=4, column=0, sticky="w")
lbl_address = tk.Label(win, text="Address", padx=20, pady=10).grid(row=5, column=0, sticky="w")
lbl_phone = tk.Label(win, text="Phone", padx=20, pady=10).grid(row=6, column=0, sticky="w")
lbl_email = tk.Label(win, text="Email", padx=20, pady=10).grid(row=7, column=0, sticky="w")


lbl_education = tk.Label(win, text="education", padx=20, pady=10).grid(row=0, column=2, sticky="w")
lbl_direct = tk.Label(win, text="direct", padx=20, pady=10).grid(row=1, column=2, sticky="w")
lbl_company = tk.Label(win, text="company", padx=20, pady=10).grid(row=2, column=2, sticky="w")
lbl_department = tk.Label(win, text="department", padx=20, pady=10).grid(row=3, column=2, sticky="w")
lbl_position = tk.Label(win, text="position", padx=20, pady=10).grid(row=4, column=2, sticky="w")
lbl_country = tk.Label(win, text="country", padx=20, pady=10).grid(row=5, column=2, sticky="w")
lbl_city = tk.Label(win, text="city", padx=20, pady=10).grid(row=6, column=2, sticky="w")
lbl_address = tk.Label(win, text="address", padx=20, pady=10).grid(row=7, column=2, sticky="w")
lbl_member = tk.Label(win, text="member", padx=20, pady=10).grid(row=8, column=2, sticky="w")
lbl_date_request = tk.Label(win, text="date_request", padx=20, pady=10).grid(row=9, column=2, sticky="w")
lbl_date_answer = tk.Label(win, text="date_answer", padx=20, pady=10).grid(row=10, column=2, sticky="w")
lbl_theme = tk.Label(win, text="theme", padx=20, pady=10).grid(row=11, column=2, sticky="w")
lbl_thesis = tk.Label(win, text="thesis", padx=20, pady=10).grid(row=12, column=2, sticky="w")
lbl_date_arriving = tk.Label(win, text="date_arriving", padx=20, pady=13).grid(row=13, column=2, sticky="w")
lbl_hotel = tk.Label(win, text="hotel", padx=20, pady=10).grid(row=14, column=2, sticky="w")
lbl_date_departure = tk.Label(win, text="date_departure", padx=20, pady=15).grid(row=15, column=2, sticky="w")


person = Person()

person.name = tk.Entry(win)
person.name.grid(row=0, column=1, sticky="w")

person.second_name = tk.Entry(win)
person.second_name.grid(row=1, column=1, sticky="w")

person.birthday = tk.Entry(win)
person.birthday.grid(row=2, column=1, sticky="w")

person.country = tk.Entry(win)
person.country.grid(row=3, column=1, sticky="w")

person.city = tk.Entry(win)
person.city.grid(row=4, column=1, sticky="w")

person.address = tk.Entry(win)
person.address.grid(row=5, column=1, sticky="w")

person.phone = tk.Entry(win)
person.phone.grid(row=6, column=1, sticky="w")

person.email = tk.Entry(win)
person.email.grid(row=7, column=1, sticky="w")

# person.education = tk.Entry(win)
# person.education.grid(row=0, column=3, sticky="w")

# person.direct = tk.Entry(win)
# person.direct.grid(row=1, column=3, sticky="w")

# person.company = tk.Entry(win)
# person.company.grid(row=2, column=3, sticky="w")

# person.department = tk.Entry(win)
# person.department.grid(row=3, column=3, sticky="w")

# person.position = tk.Entry(win)
# person.position.grid(row=4, column=3, sticky="w")

# person.country = tk.Entry(win)
# person.country.grid(row=5, column=3, sticky="w")

# person.city = tk.Entry(win)
# person.city.grid(row=6, column=3, sticky="w")

# person.address = tk.Entry(win)
# person.address.grid(row=7, column=3, sticky="w")

# person.member = tk.Entry(win)
# person.member.grid(row=8, column=3, sticky="w")

# person.date_request = tk.Entry(win)
# person.date_request.grid(row=9, column=3, sticky="w")

# person.date_answer = tk.Entry(win)
# person.date_answer.grid(row=10, column=3, sticky="w")

# person.theme = tk.Entry(win)
# person.theme.grid(row=11, column=3, sticky="w")

# person.thesis = tk.Entry(win)
# person.thesis.grid(row=12, column=3, sticky="w")

# person.date_arriving = tk.Entry(win)
# person.date_arriving.grid(row=13, column=3, sticky="w")

# person.hotel = tk.Entry(win)
# person.hotel.grid(row=14, column=3, sticky="w")

# person.date_departure = tk.Entry(win)
# person.date_departure.grid(row=15, column=3, sticky="w")


btn_send_form = tk.Button(win, text="Send", command=send_form, state="normal").grid(row=18, column=0, sticky="w")

base = sqlite3.connect('conf.db')
cur = base.cursor()

base.execute( 'CREATE TABLE IF NOT EXISTS {} (name, second_name, birthday, country, city, address, phone, email)' .format('data_members') )
base.commit()

win.mainloop()

# END_PROGRAM.