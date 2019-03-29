import re
from tkinter import *
from os import path
from tkinter import filedialog
import urllib.request


home = Tk()
home.title("LEECH v2.0")
home.attributes("-alpha", 0.0)
home.configure(background="black")

#ENTRY FIELD
data_entry = Entry(home)
data_entry.configure(width=40)
data_entry.place(y=30, x=50) 

##FUNCTION TO BROWSE FILE 
def open_file(event):
	global file_address
	file_address = filedialog.askopenfilename()
	data_entry.insert(0, file_address)
	return file_address


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
		#global master
		
		#MAKING TITLE LABEL
		title_label = Label(master, text="****WELCOME TO THE LEECHER v2.1****", fg="pink", bg="black") 
		title_label.place(y=5,x=80)


		#MAKING BROWSE BUTTON
		browse_button = Button(master, text="BROWSE", fg = "yellow" , bg="black")
		browse_button.bind("<Button-1>", open_file)
		browse_button.configure(width=10)
		browse_button.place(y=55, x=146)
		
	##OPTIONS FOR METHOD TYPE
		#CHOICE LABEL
		method_choice_label = Label(master, text="~CHOOSE METHOD~", fg="pink", bg="black")
		method_choice_label.place(y=100, x=140)

		#RADIOBUTTONS FOR CHOICE
		Radiobutton(master, text="LEECH FROM URL       ", fg="cyan", bg="black",variable = method_choice, value=1 ).place(y=120, x=5, height=20)
		Radiobutton(master, text="LEECH FROM LOCAL FILE", fg="cyan", bg="black",variable = method_choice, value=2 ).place(y=120 ,x=242, height=21)

	##OPTIONS FOR DATA TYPE
		#CHOICE LABEL
		data_choice_label = Label(master, text="~CHOOSE TYPE TO LEECH~", fg="pink", bg="black")
		data_choice_label.place(y=150, x=120)

		#RADIOBUTTONS FOR CHOICE
		Radiobutton(master, text="LEECH EMAIL\t", fg="cyan", bg="black",variable = data_choice, value=1 ).place(y=170, x=5, height=20)
		Radiobutton(master, text="LEECH PROXY:PORT\t      ",fg="cyan", bg="black", variable = data_choice, value=2 ).place(y=170, x=242, height=21)

	##BUTTON FOR LEECH
		leech_button = Button(master, text="LEECH", fg="yellow", bg="black")
		leech_button.bind("<Button-1>", self.display)
		leech_button.configure(width=10)
		leech_button.place(y=200, x=146)

###ALL UTILITY FUNCTIONS HERE

	##FUNCTION TO GET URL
	def get_URL(self):
		#global master
		global data_entry
		global URL
		
		URL = ""
		URL = data_entry.get()
		return URL

	##FUNCTION TO GET FILE ADDRESS
	def get_address(self):
		#global master
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
		global file
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

		output_label = Label(new_window, text=data, fg="red", bg="black")
		output_label.pack()
		new_window.resizable(0,0)		#TO MAKE WINDOW NON-EXPANDABLE
		new_window.mainloop()


##URL LOCAL EMAIL PROXY

	def display(self, event):
		global method_choice
		#global master
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
home.configure(width=405, height=240)
home.resizable(0,0)
home.mainloop()