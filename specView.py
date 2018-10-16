import matplotlib
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import numpy as np
from tkinter import filedialog
from scipy import signal

#matplotlib.use("TkAgg")

N=0
root = tk.Tk()
fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack()
ax = fig.add_subplot(111)
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()

######################################################
        
class GraphFrame(tk.Frame):

    def __init__(self, master=None):
        
        tk.Frame.__init__(self, master)   
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("SpecView")

        self.pack(fill=tk.NONE)

        # Create the menus
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        #File - Open, and Exit
        file = tk.Menu(menu)
        file.add_command(label="Open", command=self.openFile)
        file.add_command(label="Exit", command=self.exit)
        menu.add_cascade(label="File", menu=file)

        #Edit - does noting at the moment
        edit = tk.Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)
    
    def exit(self):
        exit()

    def openFile(self):
        global spectrum
        #Open file to read spectrum
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("dat files","*.dat"),("all files","*.*")))

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
        #Make the channels global
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
        global N

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

        N=len(iE)
        print (N,"N")
        
        p=GraphFrame.plot()
        
        peaks, properties = signal.find_peaks(L2, prominence=(None, 0.6))
        
        print (peaks, properties["prominences"].max())
    
        #print (peakind, Ax_[peakind], iE_[peakind])
        
    def plot():

        ax.clear()
        #Check to see what checkboxes are ticked.
        if Controls.L5_checked.get():
            ax.plot(iE,L5,color='green')
        
        if Controls.L4_checked.get():
            ax.plot(iE,L4,color='red')

        if Controls.L3_checked.get():
            ax.plot(iE,L3,color='blue')

        if Controls.L2_checked.get():
            ax.plot(iE,L2,color='cyan')

        if Controls.L1_checked.get():
            ax.plot(iE,L1,color='black')

        if Controls.Ax_checked.get():
            ax.plot(iE,Ax,color='magenta')            

        if Controls.H1_checked.get():
            ax.plot(iE,H1,color='yellow')

        if Controls.H2_checked.get():
            ax.plot(iE,H2,color='0.25')              

        if Controls.H3_checked.get():
            ax.plot(iE,H3,color='0.5')  

        if Controls.H4_checked.get():
            ax.plot(iE,H4,color='0.75')
            
        fig.canvas.draw_idle()
        root.update()
        return 1

    def UpdatePlot():
        #Check to see if a scan is loaded. 
        print ("N", N)
        if (N>0):
            p=GraphFrame.plot()

######################################################
            
class Controls(tk.Frame):
    
    def __init__(self, root):
        tk.Frame.__init__(self, root)

    def callback(*args):
        print ("variable changed!")
        GraphFrame.UpdatePlot()
        
    L5_checked = tk.IntVar()
    L5_checked.trace("w", callback)
    L5_checked.set(0)
    
    L4_checked = tk.IntVar()
    L4_checked.trace("w", callback)
    L4_checked.set(1)

    L3_checked = tk.IntVar()
    L3_checked.trace("w", callback)
    L3_checked.set(0)

    L2_checked = tk.IntVar()
    L2_checked.trace("w", callback)
    L2_checked.set(1)

    L1_checked = tk.IntVar()
    L1_checked.trace("w", callback)
    L1_checked.set(0)

    Ax_checked = tk.IntVar()
    Ax_checked.trace("w", callback)
    Ax_checked.set(1)
    
    H1_checked = tk.IntVar()
    H1_checked.trace("w", callback)
    H1_checked.set(0)

    H2_checked = tk.IntVar()
    H2_checked.trace("w", callback)
    H2_checked.set(0)

    H3_checked = tk.IntVar()
    H3_checked.trace("w", callback)
    H3_checked.set(0)

    H4_checked = tk.IntVar()
    H4_checked.trace("w", callback)
    H4_checked.set(0)

    c1=tk.Checkbutton(root, text="L5", onvalue=1, offvalue=0, variable=L5_checked)
    c2=tk.Checkbutton(root, text="L4", onvalue=1, offvalue=0, variable=L4_checked)
    c3=tk.Checkbutton(root, text="L3", onvalue=1, offvalue=0, variable=L3_checked)
    c4=tk.Checkbutton(root, text="L2", onvalue=1, offvalue=0, variable=L2_checked)
    c5=tk.Checkbutton(root, text="L1", onvalue=1, offvalue=0, variable=L1_checked)
    c6=tk.Checkbutton(root, text="Ax", onvalue=1, offvalue=0, variable=Ax_checked)
    c7=tk.Checkbutton(root, text="H1", onvalue=1, offvalue=0, variable=H1_checked)
    c8=tk.Checkbutton(root, text="H2", onvalue=1, offvalue=0, variable=H2_checked)
    c9=tk.Checkbutton(root, text="H3", onvalue=1, offvalue=0, variable=H3_checked)
    c10=tk.Checkbutton(root, text="H4", onvalue=1, offvalue=0, variable=H4_checked)
    
    c1.pack(side="left", fill="x", expand='true')
    c2.pack(side="left", fill="x", expand='true')
    c3.pack(side="left", fill="x", expand='true')
    c4.pack(side="left", fill="x", expand='true')
    c5.pack(side="left", fill="x", expand='true')
    c6.pack(side="left", fill="x", expand='true')
    c7.pack(side="left", fill="x", expand='true')
    c8.pack(side="left", fill="x", expand='true')
    c9.pack(side="left", fill="x", expand='true')
    c10.pack(side="left", fill="x", expand='true')
    
######################################################       

root.geometry("800x600")

graph = GraphFrame(root)
controls=Controls(root)

graph.pack(side="left", fill="x")
controls.pack(side="bottom", fill="x")

root.mainloop()
