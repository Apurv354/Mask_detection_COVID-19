from tkinter import *
from PIL import Image, ImageTk
import mask_detection

class Window(Frame):

	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title("COVID-19 Surveillance Project")
		self.pack(fill = BOTH, expand = YES)
		
		runButton1 = Button(self, text="Mask Detection", command = self.mask, bg = "#ff3300", activebackground = "#00ff99")
		runButton1.place(height = 50, width = 200, x = 50, y = 540)

		runButton2 = Button(self, text="Social Distancing", command = self.social, bg = "#ff3300", activebackground = "#00ff99" )
		runButton2.place(height = 50, width = 200,x = 350, y = 540)
		
		quitButton = Button(self, text="Exit", command = self.client_exit, bg = "#ff3300")
		quitButton.place(height = 50, width = 200,x = 200, y = 600)
		
		self.showImg()
		
		menu = Menu(self.master)
		self.master.config(menu = menu)

		file = Menu(menu)
		file.add_command(label = 'Exit', command = self.client_exit)
		menu.add_cascade(label = 'File', menu = file)

		edit = Menu(menu)
		edit.add_command(label = 'About', command = self.about_app)
		edit.add_command(label = 'Team', command = self.showTxt)
		menu.add_cascade(label = 'Edit', menu = edit)

	def client_exit(self):
		print("Exit")
		exit()

	def mask(self):
		mask_detection.main()

	def social(self):
		print("In Progress")
		
	def showImg(self):
		load = Image.open('mask_ui.png')
		render = ImageTk.PhotoImage(load)

		img = Label(self, image = render)
		img.image = render
		img.place(x = 50, y=20, height = 500, width = 500)

	def showTxt(self):
		text = Label(self, text = 'Welcome')	
		text.pack()

	def about_app(self):
		text = Label(self, text = 'This application is helping people to take neccesary precautions for COVID-19')	
		text.pack()


root = Tk()
root.geometry("600x700")
app = Window(root)
root.mainloop()