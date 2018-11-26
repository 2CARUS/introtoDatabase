import tkinter as tk
from mysql.connector import (connection)

# make a page
class Page(tk.Frame):
    # Frame is a rectangular area of a window
    # inherit page from Frame as a simple superclass to other Pages
    # it's only method is show(), which simply pulls it to the top
    #   of the viewing stack

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        #auto-generated initializer method
        # note: all tkinter objects need a master Frame/Window/Whatever
        # with which to latch onto. see ROOT
    
    def show(self):
        self.lift()



# Simple record pull
class Page1(Page):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)

    pass



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
        #   page1 = page(self)
        #   ...

        # initialize naviagation frames
        buttonframe = tk.Frame(self)    # to hold buttons
        containter = tk.Frame(self)     # to hold form
        buttonframe.grid(row=0, column=0, sticky = 'W')
        

### Initialize 

'''
This file could be imported somewhere else later
A python convention is to check if it's the main,
then execute what should be main-type code stuff
'''

if __name__ == "__main__":
    root = tk.Tk()
    # ROOT
    # proper tkinter programs have a root which the other
    #   frames(pieces of window) and widgets (things in frames)
    #   are rooted into
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()