import tkinter as tk
import pandas as pd # may be needed to display information from SQL
from mysql.connector import (connection)

theme = {
    '0':'#1a1e26',  # dusk
    '1':'#383f51',  # charcoal
    '2':'#dddbf1',  # azurish white
    '3':'#3c4f76',  # independence
    '4':'#d1beb0',  # dark vanilla
    '5':'#ab9f9d'   # rose quartz
}

# make a page
class Page(tk.Frame):
    # Frame is a rectangular area of a window
    # inherit page from Frame as a simple superclass to other Pages

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        '''
        auto-generated initializer method
         note: all tkinter objects need a master Frame/Window/Whatever
         with which to latch onto. see ROOT
        ''' 
    
    def show(self):
        self.lift()
        '''
        show will do the lift method, which lifts to the top of window
        stack
        '''  

# Home Page
class Home(Page):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        # initializing photo banner
        banner = tk.PhotoImage(file="house.png")
        banner_label = tk.Label(self, image=banner)
        banner_label.image = banner
        banner_label.pack(side='top',fill='both',expand=True)

# Simple record pull
class PKLookup(Page):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        label = tk.Label(self, text='This the primary key lookup')
        label.pack(side='top',fill='both',expand=True)



# Main view window (initializes everything else)

class MainView(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        
        '''
        This mainview class may or may not be
        an actual main view. Instead of calling
        self.title(), it tries to pull from the toplevel
        structure (which could be itself) and change
        that title
        '''
        self.winfo_toplevel().title("Toolhouse Search")


        # initialize pages
        p1 = Home(self)
        p2 = PKLookup(self)
        #   ...
        
        # initialize naviagation frames
        buttonframe = tk.Frame(self)    # to hold buttons
        container = tk.Frame(self)      # to hold the page-content stuff
        buttonframe.pack(side="top", fill="x", expand=False)    # pack the buttons up top
        container.pack(side="top", fill="both", expand=True)    # put contianer underneath

        # placing pages inside content container
        p1.place(in_=container)
        p2.place(in_=container, x=0,y=0,relwidth=.7,relheight=1)
        
        # create buttons to navigate to pages
        b1 = tk.Button(buttonframe, text='Home',command=p1.lift)
        b2 = tk.Button(buttonframe, text='Single Tool Lookup',command=p2.lift)

        # packing buttons into button frame
        b1.pack(side='left')
        b2.pack(side='left')


        p1.show()
### Initialize 

'''
This file could be imported somewhere else later
A python convention is to check if it's the main,
then execute what should be main-type code stuff
'''


if __name__ == "__main__":
    square_side = 565
    size = str(square_side) + "x" + str(square_side)
    root = tk.Tk()
    # ROOT
    # proper tkinter programs have a root which the other
    #   frames(pieces of window) and widgets (things in frames)
    #   are rooted into
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry(size)
    root.mainloop()