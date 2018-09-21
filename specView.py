from tkinter import *
from tkinter import filedialog
import numpy as np




class Window(Frame):

    def __init__(self, master=None):
        
        Frame.__init__(self, master)   

        self.master = master

        self.init_window()

    #Creation of init_window
    def init_window(self):

        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Open", command=self.openFile)
        file.add_command(label="Exit", command=self.exit)
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)

    
    def exit(self):
        exit()

    def openFile(self):
        global spectrum
        #Open file to read spectrum
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("dat files","*.dat"),("all files","*.*")))
        print (root.filename)
        #add data to the global spectrum

        try:
            spectrum=np.genfromtxt(root.filename,delimiter='\t', invalid_raise = False, names=True)

        except Warning as e:
           print (e)

        self.channelConv()

    
    def channelConv(self):
        j=0
        global spectrum
        
        iE_=[]
        L5_=[]
        L4_=[]
        L3_=[]
        L2_=[]
        L1_=[]
        Ax_=[]
        H1_=[]
        H2_=[]
        H3_=[]
        H4_=[]
         
        while j<len(spectrum):
            dataLine=spectrum[j]
            dataString=str(dataLine)
            dataLine=(dataString[1:-1])

            print (dataLine)

            #Loop through my_data and produce 11 arrays
            splitString=dataLine.split(',')
            
            iE_.append(float(splitString[0]))
            L5_.append(float(splitString[1]))
            L4_.append(float(splitString[2]))
            L3_.append(float(splitString[3]))
            L2_.append(float(splitString[4]))
            L1_.append(float(splitString[5]))
            Ax_.append(float(splitString[6]))
            H1_.append(float(splitString[7]))
            H2_.append(float(splitString[8]))
            H3_.append(float(splitString[9]))
            H4_.append(float(splitString[10]))

        
        
            j=j+1


        global iE
        global L5
        global L4
        global L3
        global L2
        global L1
        global Ax
        global H1
        global H2
        global H3
        global H4

        
        

        iE=iE_
        L5=L5_
        L4=L4_
        L3=L3_
        L2=L2_
        L1=L1_
        Ax=Ax_
        H1=H1_
        H2=H2_
        H3=H3_
        H4=H4_


        
# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()
