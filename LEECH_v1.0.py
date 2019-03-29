from tkinter import *
import re
import urllib.request

#GLOBAL VARIABLES HERE
url = ""
response = " "
html_read = " "
html_decode = " "
output = " "
flag = 0

#HOME HERE
home = Tk()
home.title("LEECH v1.0")
home.resizable(0,1)


#FUNCTIONS HERE
def display(type):
	global output
	global flag
	if output == " ":
		output = "NO OUTPUT FOUND"
	#OUTPUT WINDOW
	output_window = Tk()
	output_window.title(type)
	output_window.resizable(0,0)
	#OUTPUT LABEL
	output_label = Label(output_window, text=output)
	output_label.grid(sticky=W)
	output_window.mainloop()
	flag = 1

def url_open():
	global url
	global flag
	global response
	global html_read
	global html_decode 

	url = url_entry.get()
	response = urllib.request.urlopen(url)
	html_read = response.read()
	html_decode = html_read.decode()

def email(event):
	global url
	global flag
	global response
	global html_read
	global html_decode 
	global output

	url_open()
	email_directory = re.findall("\w{1,20}@\w{1,10}.\w{1,5}", html_decode) 
	output = " "
	for i in email_directory:
		output += i + "\n"
	display("EMAIL OUTPUT")

def proxy(event):
	global url
	global response
	global html_read
	global html_decode 
	global output
	global flag
	
	url_open()
	proxy_directory = re.findall("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\w{1,4}", html_decode) 
	output = " "
	for i in proxy_directory:
		output += i + "\n"
	display("PROXY OUTPUT")

#FRAMES HERE
top_frame = Frame(home)			#FOR INPUT AREA
top_frame.pack()

bottom_frame = Frame(home)
bottom_frame.pack(side="bottom")

#TOP-FRAME  WIDGETS HERE(ACCORDING TO APPEARANCE)
title_label = Label(top_frame, text="****DATA LEECHER****")
title_label.grid(sticky=W)

entry_label = Label(top_frame, text="Enter URL Here :")
entry_label.grid(row=1, sticky=W)

url_entry = Entry(top_frame)
url_entry.grid(row=2,sticky=W)

choice_label = Label(top_frame, text="Click Button accordingly: ")
choice_label.grid(row=3, sticky=W)

email_button = Button(top_frame, text="Leech Email")
email_button.bind("<Button-1>", email)
email_button.grid(row=4, column=0,sticky=W)

proxy_button = Button(top_frame, text="Leech Proxy")
proxy_button.bind("<Button-1>", proxy)
proxy_button.grid(row=4,column=1, sticky=W)

home.mainloop()
