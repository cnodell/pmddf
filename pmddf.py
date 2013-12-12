#!/usr/local/bin/python

#Import Tkinter
from Tkinter import *
from tkFileDialog import *
from tkMessageBox import *
import subprocess

#Create the application class
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        
        self.input_button = Button(self, text = "Input File", command = self.in_dialog)
        self.input_button.grid(row = 2, column = 0, sticky = W)
        
        self.input_entry = Entry(self)
        self.input_entry.grid(row = 2, column = 1, columnspan = 2, sticky = W)
        
        self.output_button = Button(self, text = "Output File", command = self.out_dialog)
        self.output_button.grid(row = 3, column = 0, sticky = W)
        
        self.output_entry = Entry(self)
        self.output_entry.grid(row = 3, column = 1, columnspan = 2, sticky = W)
        
        self.size_label = Label (self, text = "Paper Size")
        self.size_label.grid(row = 4, column = 0, sticky = W)
        
        self.size_options = StringVar(self)
        self.size_options.set("A4") # default value
        self.size_entry = OptionMenu(self, self.size_options, "A4", "Letter")
        self.size_entry.grid(row = 4, column = 1, columnspan = 2, sticky = W)
        
        self.orientation_label = Label (self, text = "Paper Orientation")
        self.orientation_label.grid(row = 5, column = 0, sticky = W)
        
        self.orientation_options = StringVar(self)
        self.orientation_options.set("Portrait") # default value
        self.orientation_entry = OptionMenu(self, self.orientation_options, "Portrait", "Landscape")
        self.orientation_entry.grid(row = 5, column = 1, columnspan = 2, sticky = W)
        
        self.duplex_label = Label (self, text = "Duplex")
        self.duplex_label.grid(row = 6, column = 0, sticky = W)
        
        self.duplex_options = StringVar(self)
        self.duplex_options.set("Single Sided") # default value
        self.duplex_entry = OptionMenu(self, self.duplex_options, "Single Sided", "Double Sided")
        self.duplex_entry.grid(row = 6, column = 1, columnspan = 2, sticky = W)
        
        self.tmargin_label = Label (self, text = "Top Margin")
        self.tmargin_label.grid(row = 7, column = 0, sticky = W)
        
        self.tmargin_entry = Entry(self)
        self.tmargin_entry.grid(row = 7, column = 1, columnspan = 2, sticky = W)
        
        self.bmargin_label = Label (self, text = "Bottome Margin")
        self.bmargin_label.grid(row = 8, column = 0, sticky = W)
        
        self.bmargin_entry = Entry(self)
        self.bmargin_entry.grid(row = 8, column = 1, columnspan = 2, sticky = W)
        
        self.lmargin_label = Label (self, text = "Left/Insode Margin")
        self.lmargin_label.grid(row = 9, column = 0, sticky = W)
        
        self.lmargin_entry = Entry(self)
        self.lmargin_entry.grid(row = 9, column = 1, columnspan = 2, sticky = W)
        
        self.rmargin_label = Label (self, text = "Right/Outside Margin")
        self.rmargin_label.grid(row = 10, column = 0, sticky = W)
        
        self.rmargin_entry = Entry(self)
        self.rmargin_entry.grid(row = 10, column = 1, columnspan = 2, sticky = W)
        
        self.numbers_label = Label (self, text = "Page Numbers")
        self.numbers_label.grid(row = 11, column = 0, sticky = W)
        
        self.numbers_options = StringVar(self)
        self.numbers_options.set("On") # default value
        self.numbers_entry = OptionMenu(self, self.numbers_options, "On", "Off")
        self.numbers_entry.grid(row = 11, column = 1, columnspan = 2, sticky = W)
        
        self.toc_label = Label (self, text = "Table of Contents")
        self.toc_label.grid(row = 12, column = 0, sticky = W)
        
        self.toc_options = StringVar(self)
        self.toc_options.set("Off") # default value
        self.toc_entry = OptionMenu(self, self.toc_options, "On", "Off")
        self.toc_entry.grid(row = 12, column = 1, columnspan = 2, sticky = W)
        
        self.quitButton = Button ( self, text="Quit", command=self.quit )
        self.quitButton.grid(row = 13, column = 0)
        
        self.create_button = Button(self, text = "Create", command = self.create)
        self.create_button.grid(row = 13, column = 2)

    def in_dialog(self):
        self.input_entry.insert(0, askopenfilename())
    
    def out_dialog(self):
        self.output_entry.insert(0, asksaveasfilename())

    def create(self):
        
        in_file = self.input_entry.get()
        out_file = self.output_entry.get()
        size = self.size_options.get()
        orientation = self.orientation_options.get()
        duplex = self.duplex_options.get()
        tmargin = self.tmargin_entry.get()
        bmargin = self.bmargin_entry.get()
        lmargin = self.lmargin_entry.get()
        rmargin = self.rmargin_entry.get()
        numbers = self.numbers_options.get()
        toc = self.toc_options.get()
        
        command = ['pandoc', in_file, '-o', out_file,]
        if size == 'A4':
            command.append('-V')
            command.append('papersize:a4paper')
        if duplex == 'Double Sided':
            command.append('-V')
            command.append('classoption:twoside')
        if orientation == 'Landscape':
            command.append('-V')
            command.append('geometry:landscape')
        if tmargin:
            command.append('-V')
            command.append('geometry:top=' + tmargin)
        if bmargin:
            command.append('-V')
            command.append('geometry:bottom=' + bmargin)
        if lmargin:
            command.append('-V')
            command.append('geometry:left=' + lmargin)
        if rmargin:
            command.append('-V')
            command.append('geometry:right=' + rmargin)
        if numbers == 'Off':
            command.append('-V')
            command.append('header-includes=\pagenumbering{gobble}')
        if toc == 'On':
            command.append('--table-of-contents')
        
        exitcode = subprocess.call(command)
        
        if exitcode == 0:
            showinfo("Success!", "PDf has been created!")
        else:
            showwarning("Creation Error", "Could not create PDF. Please verify all values are entered correctly.")

#Start Applicatipn

#Create app object from Application class
app = Application()

#Define app attributes
app.master.title("pmddf")

#start app event loop
app.mainloop()