import re
from tkinter import *
from os import path
import urllib.request


home = Tk()
home.title("LEECH v2.0")

#MAKING FRAME FOR ALL THE OPTIONS
top_frame = Frame(home)
top_frame.pack()

#ENTRY FIELD
data_entry = Entry(top_frame)
data_entry.grid(row=1, column=0, sticky=W) 

##VARIABLES TO BE USED IN PROGRAM
file_address = ""
URL = ""
method_choice = IntVar()
data_choice = IntVar()
output_data = ""

class myLeech:
	def __init__(self, master):
		##GLOBAL VARIABLE DEFINITION SECTION
		global method_choice
		global top_frame
		

		#MAKING TITLE LABEL
		title_label = Label(top_frame, text="****WELCOME TO THE LEECHER v2.0****", fg="red") 
		title_label.grid(row=0,column=0,sticky=W)

		
	##OPTIONS FOR METHOD TYPE
		#CHOICE LABEL
		method_choice_label = Label(top_frame, text="CHOOSE METHOD :", fg="red")
		method_choice_label.grid(row=2, sticky=W)

		#RADIOBUTTONS FOR CHOICE
		Radiobutton(top_frame, text="LEECH FROM URL", variable = method_choice, value=1 ).grid(row=3, sticky=W)
		Radiobutton(top_frame, text="LEECH FROM LOCAL FILE", variable = method_choice, value=2 ).grid(row=3, column=1, sticky=W)

	##OPTIONS FOR DATA TYPE
		#CHOICE LABEL
		data_choice_label = Label(top_frame, text="CHOOSE TYPE TO LEECH :", fg="red")
		data_choice_label.grid(row=4, sticky=W)

		#RADIOBUTTONS FOR CHOICE
		Radiobutton(top_frame, text="LEECH EMAIL", variable = data_choice, value=1 ).grid(row=5, sticky=W)
		Radiobutton(top_frame, text="LEECH PROXY:PORT", variable = data_choice, value=2 ).grid(row=5, column=1, sticky=W)

	##BUTTON FOR LEECH
		leech_button = Button(top_frame, text="LEECH", fg="green", bg="black")
		leech_button.bind("<Button-1>", self.display)
		leech_button.grid(row=7, column=0, sticky=E)

###ALL UTILITY FUNCTIONS HERE

	##FUNCTION TO GET URL
	def get_URL(self):
		global top_frame
		global data_entry
		global URL
		
		URL = ""
		URL = data_entry.get()
		return URL

	##FUNCTION TO GET FILE ADDRESS
	def get_address(self):
		global top_frame
		global data_entry
		global file_address

		file_address = ""
		file_address = data_entry.get()
		return file_address


	def open_URL(self):
		response = urllib.request.urlopen(self.get_URL())
		html = response.read()
		html_data = html.decode()
		return html_data

	def leech_email_from_URL(self):
		global output_data

		email_list = re.findall("\w{1,20}@\w{1,10}.\w{1,5}", self.open_URL())
		output_data=""

		for i in email_list:
			output_data += i + "\n"

		return output_data

	def leech_email_from_file(self):
		global output_data

		if path.exists(self.get_address()) == False:
			output_data = "FILE NOT FOUND !!!"
		else:
			with open("%s"%(self.get_address()), "r") as data_file:
				email_list = re.findall("\w{1,20}@\w{1,10}.\w{1,5}", data_file.read())
			output_data = ""
			for i in email_list:
				output_data += i + "\n"
		
		return output_data

	def leech_proxy_from_URL(self):
		global output_data

		proxy_list = re.findall("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,4}", self.open_URL())
		output_data=""

		for i in proxy_list:
			output_data += i + "\n"

		return output_data
			


	def leech_proxy_from_file(self):
		global output_data

		if path.exists(self.get_address()) == False:
			output_data = "FILE NOT FOUND !!!"
		else:
			with open("%s"%(self.get_address()), "r") as data_file:
				proxy_list = re.findall("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,4}", data_file.read())
			output_data = ""
			for i in proxy_list:
				output_data += i + "\n"
		
		return output_data


	def new_window_open(self, title_tag, data):
		new_window = Tk()
		new_window.title(title_tag) 

		output_label = Label(new_window, text=data, fg="black")
		output_label.pack()
		new_window.resizable(0,0)		#TO MAKE WINDOW NON-EXPANDABLE
		new_window.mainloop()


##URL LOCAL EMAIL PROXY

	def display(self, event):
		global method_choice
		global top_frame
		global data_entry

		if method_choice.get() == 1 and data_choice.get() == 1:
			self.new_window_open("EMAIL LEECHED FROM URL", self.leech_email_from_URL())
		elif method_choice.get() == 1 and data_choice.get() == 2: 	
			self.new_window_open("PROXY LEECHED FROM URL", self.leech_proxy_from_URL())
		elif method_choice.get() == 2 and data_choice.get() == 1:
			self.new_window_open("EMAIL LEECHED FROM LOCAL FILE", self.leech_email_from_file())
		elif method_choice.get() == 2 and data_choice.get() == 2:
			self.new_window_open("PROXY LEECHED FROM LOCAL FILE", self.leech_proxy_from_file())
		else:
			self.new_window_open("XXXXXX", "ERROR!!! CHOOSE RIGHT OPTIONS")

my_object = myLeech(home)
home.resizable(0,0)
home.mainloop()
